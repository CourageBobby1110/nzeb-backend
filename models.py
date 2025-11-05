import math

# --- 1. System Overview (Overall Energy Balance Model) ---


def calculate_total_energy_generated(e_pv, e_wt, e_bg):
    """Calculates the total energy generated from all renewable sources."""
    return e_pv + e_wt + e_bg


def calculate_energy_balance(e_generated, e_grid, e_load):
    """
    Calculates the excess or curtailed energy.
    E_excess(t) = E_PV(t) + E_WT(t) + E_BG(t) + E_grid(t) - E_L(t)
    """
    return e_generated + e_grid - e_load


# --- 2. Solar PV Energy Output Model ---


def calculate_pv_energy(area, efficiency, irradiance):
    """
    Calculates the energy output from the solar PV system.
    E_PV(t) = A_PV * η_PV * G(t)
    Args:
        area (float): Area of the solar panel [m²].
        efficiency (float): Efficiency of the PV module (e.g., 0.18).
        irradiance (float): Solar irradiance at a given time [kW/m²].
    Returns:
        float: Energy from Solar PV [kWh].
    """
    return area * efficiency * irradiance


# --- 3. Wind Turbine Power Output ---


def calculate_wind_power(rho, area, cp, v, v_cut_in, v_rated, v_cut_out, p_rated):
    """
    Calculates the power output of a wind turbine based on wind speed.
    P_WT(v)
    Args:
        rho (float): Air density [kg/m³].
        area (float): Swept area of the turbine blades [m²].
        cp (float): Power coefficient.
        v (float): Wind speed [m/s].
        v_cut_in (float): Cut-in wind speed [m/s].
        v_rated (float): Rated wind speed [m/s].
        v_cut_out (float): Cut-out wind speed [m/s].
        p_rated (float): Rated power of the turbine [kW].
    Returns:
        float: Power output from the wind turbine [kW].
    """
    if v < v_cut_in or v > v_cut_out:
        return 0.0
    elif v_cut_in <= v <= v_rated:
        # Power is in Watts, convert to kW by dividing by 1000
        return (0.5 * rho * area * (v**3) * cp) / 1000
    elif v_rated < v <= v_cut_out:
        return p_rated
    return 0.0


def calculate_wind_energy(
    rho, area, cp, v, v_cut_in, v_rated, v_cut_out, p_rated, delta_t
):
    """
    Calculates the energy output from the wind turbine over a time interval.
    E_WT(t) = P_WT(v(t)) * Δt
    Args:
        delta_t (float): Time interval in hours.
    Returns:
        float: Energy from the wind turbine [kWh].
    """
    power_kw = calculate_wind_power(
        rho, area, cp, v, v_cut_in, v_rated, v_cut_out, p_rated
    )
    return power_kw * delta_t


# --- 4. Biogas (Methane) Energy Model ---


def calculate_biogas_energy(y_ch4, m_feedstock, eta_bg, hhv_ch4):
    """
    Calculates the energy output from the biogas system.
    E_BG(t) = η_BG * V_CH4 * HHV_CH4
    Args:
        y_ch4 (float): Methane yield [m³/kg VS].
        m_feedstock (float): Mass of feedstock [kg/day].
        eta_bg (float): Efficiency of the burner/generator.
        hhv_ch4 (float): Higher heating value of methane [kWh/m³].
    Returns:
        float: Energy from Biogas [kWh/day].
    """
    v_ch4 = y_ch4 * m_feedstock
    # Convert from kWh/day to kWh for the given time interval (assuming per hour for consistency)
    return eta_bg * v_ch4 * hhv_ch4 / 24


# --- 5. Battery Storage Model ---


class Battery:
    """
    A simple model for a battery storage system.
    """

    def __init__(self, capacity, initial_soc, eta_c, eta_d):
        self.capacity = capacity  # kWh
        self.soc = initial_soc  # State of Charge (0.0 to 1.0)
        self.eta_c = eta_c  # Charging efficiency
        self.eta_d = eta_d  # Discharging efficiency

    def charge(self, energy_kwh):
        """
        Charges the battery with a given amount of energy.
        Returns the actual energy stored.
        """
        space_available = (1 - self.soc) * self.capacity
        energy_to_store = energy_kwh * self.eta_c

        actual_charge = min(space_available, energy_to_store)
        self.soc += actual_charge / self.capacity
        return actual_charge / self.eta_c  # Return energy consumed for charging

    def discharge(self, energy_kwh):
        """
        Discharges the battery to provide a given amount of energy.
        Returns the actual energy provided.
        """
        energy_available = self.soc * self.capacity * self.eta_d
        actual_discharge = min(energy_available, energy_kwh)

        self.soc -= (actual_discharge / self.eta_d) / self.capacity
        return actual_discharge


# --- 6. Life Cycle Cost Analysis (LCCA) ---


def calculate_lcc(c_init, c_om, c_rep, s, r, n):
    """
    Calculates the Life Cycle Cost (LCC).
    LCC = C_init + Σ (C_O&M(y) + C_rep(y) - S(y)) / (1 + r)^y
    """
    total_costs = c_init
    # Simplified: Assuming constant annual costs
    for y in range(1, n + 1):
        # Assuming replacement cost and salvage value happen at the end of life
        annual_cost = c_om
        if y == n:
            annual_cost += c_rep - s
        total_costs += annual_cost / ((1 + r) ** y)
    return total_costs


def calculate_lcoe(lcc, e_total_per_year, r, n):
    """
    Calculates the Levelized Cost of Energy (LCOE).
    LCOE = LCC / Σ (E_total(y) / (1 + r)^y)
    """
    total_discounted_energy = 0
    for y in range(1, n + 1):
        # You could add a degradation factor for energy output here
        total_discounted_energy += e_total_per_year / ((1 + r) ** y)

    if total_discounted_energy == 0:
        return float("inf")  # Avoid division by zero

    return lcc / total_discounted_energy


# --- 7. CO₂ Emission Reduction ---


def calculate_co2_reduction(e_offset, ef):
    """
    Calculates the CO₂ emission reduction.
    ΔCO₂ = E_offset * EF
    Args:
        e_offset (float): Energy displaced from a high-emission source [kWh].
        ef (float): Emission factor of the displaced source [kg CO₂/kWh].
    Returns:
        float: CO₂ emission reduction [kg CO₂].
    """
    return e_offset * ef
