from flask import Flask, request, jsonify
from flask_cors import CORS
from models import (
    calculate_pv_energy,
    calculate_wind_energy,
    calculate_biogas_energy,
    calculate_total_energy_generated,
    calculate_energy_balance,
    calculate_lcc,
    calculate_lcoe,
    calculate_co2_reduction,
    Battery,
)
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)
CORS(app)  # This will allow your Next.js app to communicate with the backend


@app.route("/api/nzeb_model", methods=["POST"])
def nzeb_model():
    """
    Main endpoint to run the NZEB model simulation.
    It takes various inputs as a JSON object and returns the simulation results.
    """
    try:
        data = request.get_json()

        # 1. Input Validation (Basic)
        required_keys = [
            "solar_inputs",
            "wind_inputs",
            "biogas_inputs",
            "load_demand",
            "grid_energy",
            "battery_inputs",
            "lcca_inputs",
            "co2_inputs",
        ]
        if not all(key in data for key in required_keys):
            return jsonify({"error": "Missing required input data"}), 400

        # 2. Extracting inputs from the request
        solar_inputs = data["solar_inputs"]
        wind_inputs = data["wind_inputs"]
        biogas_inputs = data["biogas_inputs"]
        load_demand = data["load_demand"]  # E_L(t)
        grid_energy = data["grid_energy"]  # E_grid(t)
        battery_inputs = data["battery_inputs"]
        lcca_inputs = data["lcca_inputs"]
        co2_inputs = data["co2_inputs"]

        # --- Energy Generation Calculations ---
        e_pv = calculate_pv_energy(
            area=solar_inputs["area_pv"],
            efficiency=solar_inputs["efficiency_pv"],
            irradiance=solar_inputs["irradiance"],
        )

        e_wt = calculate_wind_energy(
            rho=wind_inputs["air_density"],
            area=wind_inputs["swept_area"],
            cp=wind_inputs["power_coefficient"],
            v=wind_inputs["wind_speed"],
            v_cut_in=wind_inputs["v_cut_in"],
            v_rated=wind_inputs["v_rated"],
            v_cut_out=wind_inputs["v_cut_out"],
            p_rated=wind_inputs["p_rated"],
            delta_t=wind_inputs["delta_t"],
        )

        e_bg = calculate_biogas_energy(
            y_ch4=biogas_inputs["methane_yield"],
            m_feedstock=biogas_inputs["mass_feedstock"],
            eta_bg=biogas_inputs["efficiency_bg"],
            hhv_ch4=biogas_inputs["hhv_ch4"],
        )

        total_energy_generated = calculate_total_energy_generated(e_pv, e_wt, e_bg)

        # --- Battery Simulation ---
        battery = Battery(
            capacity=battery_inputs["capacity"],
            initial_soc=battery_inputs.get("initial_soc", 0.5),
            eta_c=battery_inputs["eta_c"],
            eta_d=battery_inputs["eta_d"],
        )

        energy_from_generation = total_energy_generated
        energy_needed = load_demand

        if energy_from_generation > energy_needed:
            # Charge the battery with excess energy
            excess = energy_from_generation - energy_needed
            charge_amount = battery.charge(excess)
            energy_from_generation -= charge_amount
        elif energy_from_generation < energy_needed:
            # Discharge battery to meet the deficit
            deficit = energy_needed - energy_from_generation
            discharged_amount = battery.discharge(deficit)
            energy_from_generation += discharged_amount

        # --- Energy Balance Calculation ---
        e_excess = calculate_energy_balance(
            e_generated=total_energy_generated, e_grid=grid_energy, e_load=load_demand
        )

        # --- LCCA and LCOE Calculation ---
        total_energy_per_year = (
            total_energy_generated * 24 * 365
        )  # A simplified assumption

        lcc = calculate_lcc(
            c_init=lcca_inputs["c_init"],
            c_om=lcca_inputs["c_om"],
            c_rep=lcca_inputs["c_rep"],
            s=lcca_inputs["s"],
            r=lcca_inputs["r"],
            n=lcca_inputs["n"],
        )

        lcoe = calculate_lcoe(
            lcc=lcc,
            e_total_per_year=total_energy_per_year,
            r=lcca_inputs["r"],
            n=lcca_inputs["n"],
        )

        # --- CO2 Emission Reduction Calculation ---
        delta_co2 = calculate_co2_reduction(
            e_offset=total_energy_generated,  # Assuming all generated energy offsets diesel
            ef=co2_inputs["emission_factor"],
        )

        # --- Scenario Modeling (Example: Grid Outage) ---
        scenario_results = {}
        if data.get("scenario") == "grid_outage":
            # In a grid outage, grid energy is zero.
            e_excess_outage = calculate_energy_balance(
                e_generated=total_energy_generated, e_grid=0, e_load=load_demand
            )
            uptime = (
                (total_energy_generated / load_demand) * 100 if load_demand > 0 else 100
            )
            scenario_results["grid_outage"] = {
                "message": "Simulation for grid outage scenario.",
                "excess_energy_during_outage_kWh": e_excess_outage,
                "system_uptime_percentage": min(uptime, 100),
            }

        # --- Regression Analysis ---
        # Simulate data for regression: relationship between irradiance and PV output
        irradiance_samples = np.array([0.1, 0.2, 0.4, 0.6, 0.8, 1.0]).reshape(-1, 1)
        pv_output_samples = np.array(
            [
                calculate_pv_energy(
                    solar_inputs["area_pv"], solar_inputs["efficiency_pv"], i
                )
                for i in irradiance_samples.flatten()
            ]
        )

        model = LinearRegression()
        model.fit(irradiance_samples, pv_output_samples)

        regression_line = model.predict(irradiance_samples).tolist()

        regression_results = {
            "irradiance_data": irradiance_samples.flatten().tolist(),
            "pv_output_data": pv_output_samples.tolist(),
            "predicted_pv_output": regression_line,
        }

        # 3. Constructing the Response
        response = {
            "energy_generation": {
                "solar_pv_kWh": e_pv,
                "wind_turbine_kWh": e_wt,
                "biogas_kWh": e_bg,
                "total_generated_kWh": total_energy_generated,
            },
            "energy_balance": {
                "load_demand_kWh": load_demand,
                "grid_energy_kWh": grid_energy,
                "excess_or_curtailed_energy_kWh": e_excess,
            },
            "battery_status": {
                "state_of_charge_percent": battery.soc * 100,
            },
            "financial_analysis": {
                "life_cycle_cost_LCC": lcc,
                "levelized_cost_of_energy_LCOE": lcoe,
            },
            "environmental_impact": {"co2_emission_reduction_kg": delta_co2},
            "scenario_modeling_results": scenario_results,
            "regression_analysis": regression_results,
        }

        return jsonify(response), 200

    except KeyError as e:
        return jsonify({"error": f"Missing key in input data: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An unexpected error occurred: {str(e)}"}), 500


if __name__ == "__main__":
    app.run(debug=True, port=5001)
