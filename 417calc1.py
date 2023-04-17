import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import sys

# Title and introduction
st.title("Pitsy Automation vs. Contract Manufacturers Cost Comparison")
st.write("This scatter plot demonstrates the cost-effectiveness of Pitsy Automation at scale compared to other contract manufacturers.")

# Data for the scatter plot
units_produced = [1000, 5000, 10000, 20000, 50000]
pitsy_costs = [2.00, 1.90, 1.80, 1.70, 1.60]
gar_labs_costs = [2.50, 2.20, 1.95, 1.90, 1.85]
goodkind_co_costs = [3.50, 3.30, 3.10, 3.00, 2.90]

# Ensure units_produced is a list of integers
units_produced = [int(unit) for unit in units_produced]

# Streamlit slider
num_units = st.slider("Number of Units", min_value=min(units_produced), max_value=max(units_produced), value=int(units_produced[0]), step=int(units_produced[1] - units_produced[0]))

# Interpolate costs for the selected number of units
pitsy_cost = np.interp(num_units, units_produced, pitsy_costs)
gar_labs_cost = np.interp(num_units, units_produced, gar_labs_costs)
goodkind_co_cost = np.interp(num_units, units_produced, goodkind_co_costs)

# Scatter plot
fig, ax = plt.subplots()

ax.scatter(units_produced, pitsy_costs, label='Pitsy Automation', marker='o')
ax.scatter(units_produced, gar_labs_costs, label='Gar Labs', marker='o')
ax.scatter(units_produced, goodkind_co_costs, label='Goodkind Co', marker='o')

ax.plot(num_units, pitsy_cost, marker='X', markersize=10, linestyle='', color='blue', label=f"Pitsy {num_units} units")
ax.plot(num_units, gar_labs_cost, marker='X', markersize=10, linestyle='', color='orange', label=f"Gar Labs {num_units} units")
ax.plot(num_units, goodkind_co_cost, marker='X', markersize=10, linestyle='', color='green', label=f"Goodkind Co {num_units} units")

ax.set_xlabel('Units Produced')
ax.set_ylabel('Cost per Unit')
ax.set_title('Pitsy Automation vs. Contract Manufacturers Cost Comparison')
ax.legend()

st.pyplot(fig)

st.title("AI Manufacturing Assistant")

st.sidebar.image("https://cdn.shopify.com/s/files/1/0624/6072/3426/files/logoincircle_100x.png?v=1662346828")

ingredientType = st.sidebar.multiselect("What type of ingredients are you using?", ("Coconut Oil", "Shea Butter", "Candelilla Wax", "Arrowroot Powder", "Kaolin Clay", "Zinc", "Castor Oil", "Vitamin E", "Activated Charcoal", "Fragrance"))

units = st.sidebar.slider("How many units are you trying to produce per batch?", 1, 100000)

st.write("Use the sidebar on the left to begin")

CostPerUnit = st.sidebar.number_input("Enter Your Cost Per Unit")

#Cost per unit of Gar Labs, MOQ = 5,000
GarLabs5k = 1.79

#Cost per unit of goodkind co, MOQ = 10,000
Goodkind_Co10k = 3.50

#Current estimate for number of units covered by a single Pitsy?
unitsPerPitsy = 20

#Operation speed in miles per hour
operationSpeed = 2

#Human operator cost per hour
humanOperatorCostPerHour = 24.5

if st.sidebar.button('Calculate'):
    # [ ... code above ... ]
    
    # Pitsy Calculation
    st.write('##')
    # Third row of columns for cost
    col1, col2 = st.columns(2)
    col1.metric("🦾 Cost Per Unit", f'$ {CostPerUnit}', help=f'Total Pitsy cost, divided by a 10 year lifetime with 300 work-hours per year')
    col2.metric("🦾 Total Pitsy Operating Cost", 'TBD', help=f'Covering {units} units at $2.63 per unit')
    
    # #Second row of columns for cost
    # [ ... code commented out ... ]

    st.write('##')
    # Third row of columns for cost
    col1, col2 = st.columns(2)
    col1.metric("Conventional Manufacturer Operating Cost", 'TBD', help=f'Hours to traverse orchard divided by orchard size, times the Conventional Manufacturer cost per hour')
    col2.metric("Total Conventional Manufacturer Operating Cost", 'TBD', help=f'Covering {units} units at $13.79 per unit')

    # Area graph of cost
    #st.area_chart(data=df, x="units covered (units)")

    # New calculator to compare Pitsy Automation with other contract manufacturers
st.title("Pitsy Automation vs. Contract Manufacturers Cost Comparison")

# Input fields
with st.sidebar:
    st.header("Cost Comparison Calculator")
    units_to_produce = st.slider("How many units are you trying to produce per batch?", 1, 100000, key='units_to_produce')
    pitsy_cost_per_unit = st.number_input("Enter Your Pitsy Cost Per Unit", key='pitsy_cost_per_unit')
    contract_manufacturer_cost_per_unit = st.number_input("Enter Contract Manufacturer Cost Per Unit", key='contract_manufacturer_cost_per_unit')

    # Calculate costs
    pitsy_total_cost = units_to_produce * pitsy_cost_per_unit
    contract_manufacturer_total_cost = units_to_produce * contract_manufacturer_cost_per_unit
    cost_difference = contract_manufacturer_total_cost - pitsy_total_cost

    # Display cost difference
    st.subheader("Cost Difference")
    st.write(f"Cost difference between Pitsy Automation and the contract manufacturer: ${cost_difference}")

# Cost per unit of other contract manufacturers
gar_labs_5k = 1.79
goodkind_co10k = 3.50

# Calculate costs
pitsy_total_cost = units_to_produce * pitsy_cost_per_unit
gar_labs_total_cost = units_to_produce * gar_labs_5k
botanical_gardens_total_cost = units_to_produce * goodkind_co10k

# Display cost comparison
st.write("Cost Comparison:")
cost_data = pd.DataFrame(
    {
        "Manufacturer": ["Pitsy Automation", "Gar Labs", "goodkind co"],
        "Total Cost": [pitsy_total_cost, gar_labs_total_cost, botanical_gardens_total_cost]
    }
)
st.table(cost_data)

# Display cost chart
st.write("Cost Comparison Chart:")
st.bar_chart(cost_data.set_index("Manufacturer"))

import streamlit as st
import pandas as pd

# Title and introduction
st.title("Pitsy Automation vs. Contract Manufacturers Cost Comparison")
st.write("This matrix demonstrates how Pitsy Automation becomes more cost-effective at scale compared to other contract manufacturers.")

# Matrix data
data = {
    "Units Produced": [1000, 5000, 10000, 20000, 50000],
    "Pitsy Automation": [2.00, 1.90, 1.80, 1.70, 1.60],
    "Gar Labs": [2.50, 2.20, 1.95, 1.90, 1.85],
    "goodkind co": [3.20, 3.00, 2.85, 2.75, 2.65]
}

matrix_df = pd.DataFrame(data)

# Display matrix
st.write("Cost per Unit Matrix:")
st.table(matrix_df)

# Create a narrative
st.write('As the number of units produced increases, Pitsy Automation becomes more cost-effective compared to other contract manufacturers like Gar Labs and goodkind co. For example, at 1,000 units, Pitsy Automation has a cost per unit of $2.00, while Gar Labs and goodkind co have costs per unit of $2.50 and $3.20, respectively. As production scales up to 50,000 units, Pitsy Automation\'s cost per unit decreases to $1.60, while Gar Labs\' and goodkind co\' costs per unit only decrease to $1.85 and $2.65, respectively. This demonstrates the cost-effectiveness of Pitsy Automation at scale compared to other contract manufacturers.')

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and introduction
st.title("Pitsy Automation vs. Contract Manufacturers Cost Comparison")
st.write("This line chart demonstrates the cost-effectiveness of Pitsy Automation at scale compared to other contract manufacturers.")

# Data for the line chart
units_produced = [1000, 5000, 10000, 20000, 50000]
pitsy_costs = [2.00, 1.90, 1.80, 1.70, 1.60]
gar_labs_costs = [2.50, 2.20, 1.95, 1.90, 1.85]
botanical_gardens_costs = [3.20, 3.00, 2.85, 2.75, 2.65]
goodkind_co_costs = [3.50, 3.30, 3.10, 3.00, 2.90]

# Line chart
fig, ax = plt.subplots()

ax.plot(units_produced, pitsy_costs, label='Pitsy Automation', marker='o')
ax.plot(units_produced, gar_labs_costs, label='Gar Labs', marker='o')
ax.plot(units_produced, botanical_gardens_costs, label='Botanical Gardens', marker='o')
ax.plot(units_produced, goodkind_co_costs, label='Goodkind Co', marker='o')

ax.set_xlabel('Units Produced')
ax.set_ylabel('Cost per Unit')
ax.set_title('Pitsy Automation vs. Contract Manufacturers Cost Comparison')
ax.legend()

import sys
st.write(f"Python version: {sys.version}")
