# NZEB Hybrid Renewable Energy System API

A Flask-based REST API for simulating and analyzing Net Zero Energy Building (NZEB) systems with hybrid renewable energy sources. The system integrates **Solar PV**, **Wind Turbine**, **Biogas**, and **Battery Storage** technologies with comprehensive financial and environmental impact analysis.

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)
[![Flask Version](https://img.shields.io/badge/flask-3.0.0-green)](https://flask.palletsprojects.com/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.2-orange)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technology Stack](#technology-stack)
- [System Architecture](#system-architecture)
- [Installation](#installation)
- [API Documentation](#api-documentation)
- [Energy Models Explained](#energy-models-explained)
- [Usage Examples](#usage-examples)
- [Response Format](#response-format)
- [Project Structure](#project-structure)
- [Scenario Modeling](#scenario-modeling)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

This API simulates a comprehensive Hybrid Renewable Energy System (HRES) for Net Zero Energy Buildings. It calculates energy generation from multiple renewable sources, manages battery storage, performs financial analysis, and evaluates environmental impact through CO₂ emission reduction.

### Key Capabilities

- **Multi-Source Energy Generation**: Solar PV, Wind Turbine, and Biogas
- **Smart Battery Management**: Charging and discharging optimization
- **Financial Analysis**: Life Cycle Cost (LCC) and Levelized Cost of Energy (LCOE)
- **Environmental Impact**: CO₂ emission reduction calculations
- **Scenario Modeling**: Grid outage simulations and system resilience analysis
- **Regression Analysis**: Machine learning predictions for PV output optimization

---

## Features

### Energy Generation
- ☀️ **Solar PV Energy Calculation** - Based on panel area, efficiency, and irradiance
- 💨 **Wind Turbine Power Output** - With cut-in, rated, and cut-out wind speed modeling
- 🔥 **Biogas Energy Production** - From organic feedstock with methane yield modeling
- ⚡ **Real-time Energy Balance** - Load demand vs. generation analysis

### Energy Storage
- 🔋 **Battery Storage System** - With charging/discharging efficiency
- 📊 **State of Charge (SoC) Tracking** - Real-time battery status monitoring
- ⚖️ **Smart Energy Management** - Automatic excess storage and deficit compensation

### Financial Analysis
- 💰 **Life Cycle Cost Analysis (LCCA)** - Complete system cost evaluation
- 📈 **Levelized Cost of Energy (LCOE)** - Per-unit energy cost calculation
- 🎯 **Investment Analysis** - ROI and payback period insights

### Environmental Impact
- 🌱 **CO₂ Emission Reduction** - Quantified environmental benefits
- ♻️ **Renewable Energy Offset** - Displaced fossil fuel calculations

### Advanced Features
- 🔬 **Regression Analysis** - ML-based prediction models
- 🎭 **Scenario Modeling** - Grid outage and resilience testing
- 📊 **Data Visualization Ready** - Structured data for charts and graphs

---

## Technology Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| **Python** | 3.8+ | Core programming language |
| **Flask** | 3.0.0 | Web framework |
| **Flask-CORS** | 4.0.0 | Cross-origin resource sharing |
| **NumPy** | 1.26.2 | Numerical computing |
| **scikit-learn** | 1.3.2 | Machine learning algorithms |

---

## System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                     NZEB HRES System                        │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌──────────┐  ┌───────────┐  ┌─────────┐                │
│  │ Solar PV │  │   Wind    │  │ Biogas  │                │
│  │  Array   │  │  Turbine  │  │Generator│                │
│  └────┬─────┘  └─────┬─────┘  └────┬────┘                │
│       │              │              │                      │
│       └──────────────┼──────────────┘                      │
│                      │                                     │
│               ┌──────▼──────┐                              │
│               │   Energy    │                              │
│               │  Management │                              │
│               │   System    │                              │
│               └──────┬──────┘                              │
│                      │                                     │
│         ┌────────────┼────────────┐                        │
│         │            │            │                        │
│    ┌────▼────┐  ┌───▼────┐  ┌───▼────┐                   │
│    │ Battery │  │  Load  │  │  Grid  │                   │
│    │ Storage │  │ Demand │  │ Backup │                   │
│    └─────────┘  └────────┘  └────────┘                   │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Habeeb-Ajibola/nzeb-backend.git
   
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   
   - **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install flask flask-cors numpy scikit-learn
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Access the API**:
   ```
   http://localhost:5001
   ```

---

## API Documentation

### Endpoint: NZEB Model Simulation

**URL**: `POST /api/nzeb_model`

**Description**: Runs a complete NZEB hybrid renewable energy system simulation with all energy sources, battery management, financial analysis, and environmental impact assessment.

---

### Request Body Structure

```json
{
  "solar_inputs": {
    "area_pv": 100,
    "efficiency_pv": 0.18,
    "irradiance": 0.8
  },
  "wind_inputs": {
    "air_density": 1.225,
    "swept_area": 50,
    "power_coefficient": 0.4,
    "wind_speed": 8,
    "v_cut_in": 3,
    "v_rated": 12,
    "v_cut_out": 25,
    "p_rated": 10,
    "delta_t": 1
  },
  "biogas_inputs": {
    "methane_yield": 0.3,
    "mass_feedstock": 100,
    "efficiency_bg": 0.35,
    "hhv_ch4": 10
  },
  "load_demand": 50,
  "grid_energy": 0,
  "battery_inputs": {
    "capacity": 100,
    "initial_soc": 0.5,
    "eta_c": 0.9,
    "eta_d": 0.9
  },
  "lcca_inputs": {
    "c_init": 50000,
    "c_om": 2000,
    "c_rep": 10000,
    "s": 5000,
    "r": 0.05,
    "n": 20
  },
  "co2_inputs": {
    "emission_factor": 0.82
  },
  "scenario": "grid_outage"
}
```

---

### Input Parameters Explained

#### 1. Solar PV Inputs

| Parameter | Type | Description | Unit | Example |
|-----------|------|-------------|------|---------|
| `area_pv` | float | Total area of solar panels | m² | 100 |
| `efficiency_pv` | float | PV module efficiency | ratio (0-1) | 0.18 |
| `irradiance` | float | Solar irradiance | kW/m² | 0.8 |

#### 2. Wind Turbine Inputs

| Parameter | Type | Description | Unit | Example |
|-----------|------|-------------|------|---------|
| `air_density` | float | Air density | kg/m³ | 1.225 |
| `swept_area` | float | Turbine blade swept area | m² | 50 |
| `power_coefficient` | float | Turbine efficiency | ratio (0-1) | 0.4 |
| `wind_speed` | float | Current wind speed | m/s | 8 |
| `v_cut_in` | float | Minimum operational wind speed | m/s | 3 |
| `v_rated` | float | Rated wind speed | m/s | 12 |
| `v_cut_out` | float | Maximum safe wind speed | m/s | 25 |
| `p_rated` | float | Rated power output | kW | 10 |
| `delta_t` | float | Time interval | hours | 1 |

#### 3. Biogas Inputs

| Parameter | Type | Description | Unit | Example |
|-----------|------|-------------|------|---------|
| `methane_yield` | float | Methane production per VS | m³/kg VS | 0.3 |
| `mass_feedstock` | float | Organic feedstock mass | kg/day | 100 |
| `efficiency_bg` | float | Biogas generator efficiency | ratio (0-1) | 0.35 |
| `hhv_ch4` | float | Higher heating value of methane | kWh/m³ | 10 |

#### 4. Load and Grid

| Parameter | Type | Description | Unit | Example |
|-----------|------|-------------|------|---------|
| `load_demand` | float | Energy demand | kWh | 50 |
| `grid_energy` | float | Energy from grid | kWh | 0 |

#### 5. Battery Storage Inputs

| Parameter | Type | Description | Unit | Example |
|-----------|------|-------------|------|---------|
| `capacity` | float | Battery capacity | kWh | 100 |
| `initial_soc` | float | Initial state of charge | ratio (0-1) | 0.5 |
| `eta_c` | float | Charging efficiency | ratio (0-1) | 0.9 |
| `eta_d` | float | Discharging efficiency | ratio (0-1) | 0.9 |

#### 6. Life Cycle Cost Analysis (LCCA) Inputs

| Parameter | Type | Description | Unit | Example |
|-----------|------|-------------|------|---------|
| `c_init` | float | Initial investment cost | currency | 50000 |
| `c_om` | float | Annual O&M cost | currency/year | 2000 |
| `c_rep` | float | Replacement cost | currency | 10000 |
| `s` | float | Salvage value | currency | 5000 |
| `r` | float | Discount rate | ratio (0-1) | 0.05 |
| `n` | int | System lifetime | years | 20 |

#### 7. CO₂ Emission Inputs

| Parameter | Type | Description | Unit | Example |
|-----------|------|-------------|------|---------|
| `emission_factor` | float | Grid emission factor | kg CO₂/kWh | 0.82 |

#### 8. Scenario (Optional)

| Parameter | Type | Description | Values |
|-----------|------|-------------|--------|
| `scenario` | string | Simulation scenario | `"grid_outage"` or `null` |

---

## Energy Models Explained

### 1. Solar PV Energy Model

Calculates energy output from solar photovoltaic panels.

**Formula**:
```
E_PV(t) = A_PV × η_PV × G(t)
```

Where:
- `E_PV(t)` = Solar PV energy output [kWh]
- `A_PV` = Total panel area [m²]
- `η_PV` = PV module efficiency [ratio]
- `G(t)` = Solar irradiance at time t [kW/m²]

**Implementation**:
```python
def calculate_pv_energy(area, efficiency, irradiance):
    return area * efficiency * irradiance
```

---

### 2. Wind Turbine Power Model

Calculates power output based on wind speed with operational constraints.

**Formula**:
```
         ⎧ 0                           if v < v_cut_in or v > v_cut_out
P_WT(v) = ⎨ 0.5 × ρ × A × v³ × Cp     if v_cut_in ≤ v ≤ v_rated
         ⎩ P_rated                    if v_rated < v ≤ v_cut_out
```

Where:
- `P_WT(v)` = Wind turbine power output [kW]
- `ρ` = Air density [kg/m³]
- `A` = Swept area [m²]
- `v` = Wind speed [m/s]
- `Cp` = Power coefficient [ratio]
- `P_rated` = Rated power [kW]

**Energy Output**:
```
E_WT(t) = P_WT(v(t)) × Δt
```

---

### 3. Biogas Energy Model

Calculates energy from biogas generation using organic feedstock.

**Formula**:
```
E_BG(t) = η_BG × V_CH4 × HHV_CH4
```

Where:
- `V_CH4 = Y_CH4 × M_feedstock` (methane volume production)
- `η_BG` = Biogas generator efficiency [ratio]
- `HHV_CH4` = Higher heating value of methane [kWh/m³]

---

### 4. Total Energy Generation

Sum of all renewable energy sources:

```
E_total(t) = E_PV(t) + E_WT(t) + E_BG(t)
```

---

### 5. Energy Balance

Calculates excess or deficit energy:

```
E_excess(t) = E_total(t) + E_grid(t) - E_load(t)
```

- **Positive value**: Excess energy (can charge battery or export to grid)
- **Negative value**: Energy deficit (discharge battery or import from grid)

---

### 6. Battery Storage Model

Smart battery management system with:

**Charging**:
```
E_stored = min(E_excess × η_c, (1 - SoC) × C_battery)
```

**Discharging**:
```
E_discharged = min(E_deficit / η_d, SoC × C_battery)
```

Where:
- `SoC` = State of Charge [ratio]
- `C_battery` = Battery capacity [kWh]
- `η_c` = Charging efficiency
- `η_d` = Discharging efficiency

---

### 7. Life Cycle Cost (LCC)

Total cost of ownership over system lifetime:

```
LCC = C_init + Σ[(C_O&M(y) + C_rep(y) - S(y)) / (1 + r)^y]
```

---

### 8. Levelized Cost of Energy (LCOE)

Cost per unit of energy produced:

```
LCOE = LCC / Σ[E_total(y) / (1 + r)^y]
```

---

### 9. CO₂ Emission Reduction

Environmental impact quantification:

```
ΔCO₂ = E_offset × EF
```

Where:
- `E_offset` = Energy displaced from fossil sources [kWh]
- `EF` = Emission factor [kg CO₂/kWh]

---

## Usage Examples

### Python Example

```python
import requests
import json

# API endpoint
url = "http://localhost:5001/api/nzeb_model"

# Simulation parameters
payload = {
    "solar_inputs": {
        "area_pv": 100,
        "efficiency_pv": 0.18,
        "irradiance": 0.8
    },
    "wind_inputs": {
        "air_density": 1.225,
        "swept_area": 50,
        "power_coefficient": 0.4,
        "wind_speed": 8,
        "v_cut_in": 3,
        "v_rated": 12,
        "v_cut_out": 25,
        "p_rated": 10,
        "delta_t": 1
    },
    "biogas_inputs": {
        "methane_yield": 0.3,
        "mass_feedstock": 100,
        "efficiency_bg": 0.35,
        "hhv_ch4": 10
    },
    "load_demand": 50,
    "grid_energy": 0,
    "battery_inputs": {
        "capacity": 100,
        "initial_soc": 0.5,
        "eta_c": 0.9,
        "eta_d": 0.9
    },
    "lcca_inputs": {
        "c_init": 50000,
        "c_om": 2000,
        "c_rep": 10000,
        "s": 5000,
        "r": 0.05,
        "n": 20
    },
    "co2_inputs": {
        "emission_factor": 0.82
    }
}

# Send request
response = requests.post(url, json=payload)

# Parse results
if response.status_code == 200:
    results = response.json()
    
    print("=== Energy Generation ===")
    print(f"Solar PV: {results['energy_generation']['solar_pv_kWh']:.2f} kWh")
    print(f"Wind Turbine: {results['energy_generation']['wind_turbine_kWh']:.2f} kWh")
    print(f"Biogas: {results['energy_generation']['biogas_kWh']:.2f} kWh")
    print(f"Total: {results['energy_generation']['total_generated_kWh']:.2f} kWh")
    
    print("\n=== Financial Analysis ===")
    print(f"LCC: ${results['financial_analysis']['life_cycle_cost_LCC']:.2f}")
    print(f"LCOE: ${results['financial_analysis']['levelized_cost_of_energy_LCOE']:.4f}/kWh")
    
    print("\n=== Environmental Impact ===")
    print(f"CO₂ Reduction: {results['environmental_impact']['co2_emission_reduction_kg']:.2f} kg")
    
    print("\n=== Battery Status ===")
    print(f"State of Charge: {results['battery_status']['state_of_charge_percent']:.2f}%")
else:
    print(f"Error: {response.json()}")
```

---

### JavaScript (Node.js/Fetch) Example

```javascript
const fetch = require('node-fetch');

const url = 'http://localhost:5001/api/nzeb_model';

const payload = {
  solar_inputs: {
    area_pv: 100,
    efficiency_pv: 0.18,
    irradiance: 0.8
  },
  wind_inputs: {
    air_density: 1.225,
    swept_area: 50,
    power_coefficient: 0.4,
    wind_speed: 8,
    v_cut_in: 3,
    v_rated: 12,
    v_cut_out: 25,
    p_rated: 10,
    delta_t: 1
  },
  biogas_inputs: {
    methane_yield: 0.3,
    mass_feedstock: 100,
    efficiency_bg: 0.35,
    hhv_ch4: 10
  },
  load_demand: 50,
  grid_energy: 0,
  battery_inputs: {
    capacity: 100,
    initial_soc: 0.5,
    eta_c: 0.9,
    eta_d: 0.9
  },
  lcca_inputs: {
    c_init: 50000,
    c_om: 2000,
    c_rep: 10000,
    s: 5000,
    r: 0.05,
    n: 20
  },
  co2_inputs: {
    emission_factor: 0.82
  }
};

fetch(url, {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(payload)
})
  .then(response => response.json())
  .then(data => {
    console.log('=== Energy Generation ===');
    console.log(`Solar PV: ${data.energy_generation.solar_pv_kWh.toFixed(2)} kWh`);
    console.log(`Wind: ${data.energy_generation.wind_turbine_kWh.toFixed(2)} kWh`);
    console.log(`Biogas: ${data.energy_generation.biogas_kWh.toFixed(2)} kWh`);
    
    console.log('\n=== Financial Analysis ===');
    console.log(`LCC: $${data.financial_analysis.life_cycle_cost_LCC.toFixed(2)}`);
    console.log(`LCOE: $${data.financial_analysis.levelized_cost_of_energy_LCOE.toFixed(4)}/kWh`);
  })
  .catch(error => console.error('Error:', error));
```

---

### cURL Example

```bash
curl -X POST http://localhost:5001/api/nzeb_model \
  -H "Content-Type: application/json" \
  -d '{
    "solar_inputs": {
      "area_pv": 100,
      "efficiency_pv": 0.18,
      "irradiance": 0.8
    },
    "wind_inputs": {
      "air_density": 1.225,
      "swept_area": 50,
      "power_coefficient": 0.4,
      "wind_speed": 8,
      "v_cut_in": 3,
      "v_rated": 12,
      "v_cut_out": 25,
      "p_rated": 10,
      "delta_t": 1
    },
    "biogas_inputs": {
      "methane_yield": 0.3,
      "mass_feedstock": 100,
      "efficiency_bg": 0.35,
      "hhv_ch4": 10
    },
    "load_demand": 50,
    "grid_energy": 0,
    "battery_inputs": {
      "capacity": 100,
      "initial_soc": 0.5,
      "eta_c": 0.9,
      "eta_d": 0.9
    },
    "lcca_inputs": {
      "c_init": 50000,
      "c_om": 2000,
      "c_rep": 10000,
      "s": 5000,
      "r": 0.05,
      "n": 20
    },
    "co2_inputs": {
      "emission_factor": 0.82
    }
  }'
```

---

## Response Format

### Successful Response (200 OK)

```json
{
  "energy_generation": {
    "solar_pv_kWh": 14.4,
    "wind_turbine_kWh": 10.24,
    "biogas_kWh": 4.375,
    "total_generated_kWh": 29.015
  },
  "energy_balance": {
    "load_demand_kWh": 50,
    "grid_energy_kWh": 0,
    "excess_or_curtailed_energy_kWh": -20.985
  },
  "battery_status": {
    "state_of_charge_percent": 26.65
  },
  "financial_analysis": {
    "life_cycle_cost_LCC": 74468.85,
    "levelized_cost_of_energy_LCOE": 0.0292
  },
  "environmental_impact": {
    "co2_emission_reduction_kg": 23.79
  },
  "scenario_modeling_results": {
    "grid_outage": {
      "message": "Simulation for grid outage scenario.",
      "excess_energy_during_outage_kWh": -20.985,
      "system_uptime_percentage": 58.03
    }
  },
  "regression_analysis": {
    "irradiance_data": [0.1, 0.2, 0.4, 0.6, 0.8, 1.0],
    "pv_output_data": [1.8, 3.6, 7.2, 10.8, 14.4, 18.0],
    "predicted_pv_output": [1.8, 3.6, 7.2, 10.8, 14.4, 18.0]
  }
}
```

### Error Response (400 Bad Request)

```json
{
  "error": "Missing required input data"
}
```

```json
{
  "error": "Missing key in input data: solar_inputs"
}
```

### Error Response (500 Internal Server Error)

```json
{
  "error": "An unexpected error occurred: <error details>"
}
```

---

## Project Structure

```
nzeb-hres-api/
│
├── app.py                  # Main Flask application
├── models.py              # Energy calculation models
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── LICENSE               # MIT License
├── .gitignore           # Git ignore rules

```

---

## Scenario Modeling

### Grid Outage Scenario

Test system resilience during grid failures by setting `"scenario": "grid_outage"` in the request.

**What it tests**:
- System performance with zero grid energy
- Battery dependency
- Renewable energy sufficiency
- System uptime percentage

**Example**:
```json
{
  "scenario": "grid_outage",
  ...other parameters...
}
```

**Response**:
```json
{
  "scenario_modeling_results": {
    "grid_outage": {
      "message": "Simulation for grid outage scenario.",
      "excess_energy_during_outage_kWh": -20.985,
      "system_uptime_percentage": 58.03
    }
  }
}
```

---

## Dependencies

Create a `requirements.txt` file with:

```txt
Flask==3.0.0
flask-cors==4.0.0
numpy==1.26.2
scikit-learn==1.3.2
```

---

## Future Enhancements

- [ ] Real-time weather data integration
- [ ] Multiple battery bank support
- [ ] Grid tie-in with net metering
- [ ] Time-series analysis (hourly, daily, monthly)
- [ ] Advanced ML models (Random Forest, Neural Networks)
- [ ] Demand-side management algorithms
- [ ] Multi-building campus simulation
- [ ] Database integration for historical data
- [ ] WebSocket support for real-time monitoring
- [ ] Interactive dashboard frontend
- [ ] PDF report generation
- [ ] Export to CSV/Excel functionality
- [ ] RESTful CRUD operations for system configurations
- [ ] User authentication and multi-tenancy
- [ ] Docker containerization
- [ ] Cloud deployment support (AWS/Azure/GCP)
- [ ] API rate limiting and caching
- [ ] Comprehensive unit and integration tests
- [ ] CI/CD pipeline setup
- [ ] Swagger/OpenAPI documentation

---

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/YourFeature
   ```
3. **Make your changes** with clear, descriptive commits:
   ```bash
   git commit -m 'Add advanced wind speed forecasting'
   ```
4. **Add tests** for new functionality
5. **Ensure all tests pass**:
   ```bash
   python -m pytest tests/
   ```
6. **Push to your branch**:
   ```bash
   git push origin feature/YourFeature
   ```
7. **Open a Pull Request** with a detailed description

### Code Standards

- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include type hints where applicable
- Write unit tests for new features
- Update documentation

---

## Troubleshooting

### Common Issues

**Issue**: Module not found error

**Solution**: Install all dependencies:
```bash
pip install -r requirements.txt
```

---

**Issue**: Port 5001 already in use

**Solution**: Change port in `app.py`:
```python
app.run(debug=True, port=5002)
```

---

**Issue**: CORS errors in browser

**Solution**: CORS is enabled by default. Verify your frontend is making requests to the correct URL and check browser console for specific errors.

---

**Issue**: Invalid input data error

**Solution**: Ensure all required fields are present in the request body. Check the [Input Parameters](#input-parameters-explained) section for required fields.

---

**Issue**: Division by zero in LCOE calculation

**Solution**: Ensure energy generation values are non-zero. Check solar irradiance, wind speed, and biogas feedstock values.

---

**Issue**: Battery SoC outside valid range

**Solution**: Ensure `initial_soc` is between 0 and 1, and charging/discharging efficiencies (`eta_c`, `eta_d`) are between 0 and 1.

---

## Testing

### Run Unit Tests

```bash
# Install pytest
pip install pytest

# Run all tests
pytest tests/

# Run specific test file
pytest tests/test_models.py

# Run with coverage
pytest --cov=. tests/
```

### Example Test Structure

```python
# tests/test_models.py
import pytest
from models import calculate_pv_energy, Battery

def test_pv_energy_calculation():
    energy = calculate_pv_energy(area=100, efficiency=0.18, irradiance=0.8)
    assert energy == 14.4

def test_battery_charging():
    battery = Battery(capacity=100, initial_soc=0.5, eta_c=0.9, eta_d=0.9)
    battery.charge(10)
    assert battery.soc > 0.5
```

---

## Performance Considerations

### Optimization Tips

1. **Batch Requests**: For multiple simulations, consider batch processing
2. **Caching**: Implement Redis for frequently accessed calculations
3. **Async Processing**: Use Celery for long-running simulations
4. **Database**: Store results in PostgreSQL/MongoDB for analysis
5. **Load Balancing**: Use Nginx for production deployments

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for complete details.

```
MIT License

Copyright (c) 2025 [Your Name]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software...
```

---

## Acknowledgments

- Inspired by sustainable energy research and Net Zero Energy Building initiatives
- Built for university campus energy management systems
- Mathematical models based on renewable energy engineering principles
- Thanks to the open-source community for Flask, NumPy, and scikit-learn

---

## Citation

If you use this API in your research, please cite:

```bibtex
@software{nzeb_hres_api,
  title = {NZEB Hybrid Renewable Energy System API},
  author = {Habeeb},
  year = {2025},
  url = {https://github.com/yourusername/nzeb-hres-api}
}
```

---

## Contact

**Project Maintainer**:Habeeb

**Email**: ismailbadmusha@gmail.com

**Project Link**: [https://github.com/yourusername/nzeb-hres-api](https://github.com/yourusername/nzeb-hres-api)

**Issue Tracker**: [https://github.com/yourusername/nzeb-hres-api/issues](https://github.com/yourusername/nzeb-hres-api/issues)

For questions, bug reports, or feature requests, please open an issue on GitHub.

---

<div align="center">

**Version**: 1.0.0  
**Last Updated**: November 2025

Made with ❤️ for sustainable energy solutions

[![Stars](https://img.shields.io/github/stars/yourusername/nzeb-hres-api?style=social)](https://github.com/yourusername/nzeb-hres-api)
[![Forks](https://img.shields.io/github/forks/yourusername/nzeb-hres-api?style=social)](https://github.com/yourusername/nzeb-hres-api)

</div>