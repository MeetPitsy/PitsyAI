'''
  _____                                               
_/ ____\____ _______  _____             ____    ____  
\   __\\__  \\_  __ \/     \   ______  /    \  / ___\ 
 |  |   / __ \|  | \/  Y Y  \ /_____/ |   |  \/ /_/  >
 |__|  (____  /__|  |__|_|  /         |___|  /\___  / 
            \/            \/               \//_____/  
Quote Calculator v2023.02
Creator: Ryan Dinubilo
Created: 3/4/23
Revised: 3/9/23
Changelog:
v1.0
- Created calculator
v1.1 
- Added support for crops and spraying sessions
v1.2
- Added savings algorthm, graph support, more metric displays
'''


#Import Libraries
import streamlit as st
import pandas as pd
import numpy as np
import streamlit.components.v1 as components
import time
from millify import millify

#Load sidebar logo and disclaimer
logo = st.sidebar.image("https://cdn.shopify.com/s/files/1/0624/6072/3426/files/logoincircle_100x.png?v=1662346828")
title = st.sidebar.header("Pitsy Lab Calculator")
body = st.sidebar.write("This calculator will provide you with a comprehensive analysis of the benefits of using our robotics products.")
links = st.sidebar.write("To learn more, visit our [website](https://meetpitsy.com)")

#Calculation Variables and User Input
acres = st.sidebar.slider("How many units are you trying to produce?", 1, 500000)
acresInt = int(acres)

cropType = st.sidebar.selectbox("What type of product?", ["Lotion", "Shampoo", "Conditioner", "Soap", "Cherries", "Citrus", "Hops", "Pollen Application", "Row Crops (Strawberries)", "Table Grapes", "Tree Nuts", "Wine Grapes"])

advancedSettings = st.sidebar.checkbox("Advanced Settings")


#Miles of standard size 12ft width rows per acre
milesOfRowPerAcre = 0.79

#Current estimate for number of acres covered by a single Amiga?
acresPerAmiga = 20

#Operation speed in miles per hour
operationSpeed = 2

#Human operator cost per hour
humanOperatorCostPerHour = 24.5

#85 HP Tractor Overhead per hour
tractorOverheadPerHour = 34.9

#85 HP Tractor Overhead per year
tractorOverheadPerYear = 10470

#human working hours
humanWorkingHours = 8

#Autonomy working hours
autonomyWorkingHours = 20

#tractors requi
tractorsRequiredPerEvent = 1


if advancedSettings:
  milesofRowPerAcreUser = st.sidebar.number_input("Production time using Pitsy Automation per unit(default=0.40 seconds unit/produce)", value=0.40)
  operationSpeedUser = st.sidebar.number_input("Production time using Pitsy Automation (default=0.40 seconds)", value=0.40)

  humanCostPerHourUser = st.sidebar.number_input("Vendor Quotes (default=$6.40)", value=6.40)


calculateButton = st.sidebar.button("Calculate")

if calculateButton:

    #Savings algorithm
    N = acres
    
    df = pd.DataFrame({ 'Units made (product)' : range(1, N + 1, 1), 
                        'Standard Contract Manufacturer Cost ($)' : np.linspace(13.79, N*13.79 +1, N),
                        'Pitsy Cost ($)' : np.linspace(2.63, N*2.63+1, N)})

    #calculations
    orchardMiles = acres*milesOfRowPerAcre

    #hours to travers full orchard
    ttcOrchard = orchardMiles/operationSpeed

    #drivers required to complete operation
    driversRequired = ttcOrchard/humanWorkingHours

    #Human cost to complete operation
    humanTotalCost = (ttcOrchard/acres)*(humanOperatorCostPerHour)

    #Driver cost per operation
    driverTotalCost = acres*humanTotalCost

    #Number of drivers needed to complete operation
    driversNeeded = acres/8

    #Calculations
    amigaCostPerAcre = (ttcOrchard/acres)*6.67
    amigaCostPerHourRounded = round(amigaCostPerAcre, 2)
    amigaTotal = amigaCostPerAcre*acres
    amigaTotalRounded = round(amigaTotal)

    tractorCostPerHour = (ttcOrchard/acres)*tractorOverheadPerHour
    tractorCostPerHourRounded = round(tractorCostPerHour, 2)

    tractorTotal = tractorOverheadPerHour*acres
    tractorTotalRoudned =round(tractorTotal)

    #Difference savings
    savings = tractorTotal - amigaTotal
    savingsRounded = round(savings)

    st.header(f"You save: :green[${savingsRounded}] by switching to Pitsy automation")

    #input display
    col1, col2 = st.columns(2)
    col1.metric("units made", acres)
    col2.metric("production time", cropType)

    #First row of columns for miles to traverse full orchard
    col1, col2 = st.columns(2)
    col1.metric("Time it takes to run a full production", millify(orchardMiles), help=f"Covering {acres} formulation at 1.40 per unit of a standard 0.40 seconds production time")
    col2.metric("Time to create full batch", millify(ttcOrchard), help=f'At an operation sped of 0.40 seconds per unit')

    st.write('##')

    #Amiga Calculation
    #Third row of columns for cost 
    col1, col2 = st.columns(2)
    col1.metric("🦾 Pitsy Cost Per Unit", f'$ {amigaCostPerHourRounded}', help=f'Total pitsy cost, divided by a $4.50 per unit cost over a lifetime of 0.40 seconds per unit')
    col2.metric("🦾 Total Pitsy Operating Cost", f'$ {amigaTotalRounded}', help=f'Covering {acres} units at $1.40 per unit')
    
    # #Second row of columns for cost 
    # col1, col2 = st.columns(2)
    # humanCost = round(humanTotalCost, 2)
    # col1.metric(label="👤 Driver Operating Cost Per Acre", value=f'$ {humanCost}', help=f'Hours to traverse orchard divided by orchard size, times the driver pay per hour')

    # driverTotal = humanCost*acres
    # driverTotalRoudned =round(driverTotal,2)
    # col2.metric("Total Driver Operating Cost", f'$ {driverTotalRoudned}')

    st.write('##')
    #Third row of columns for cost 
    col1, col2 = st.columns(2)
    col1.metric("Pitsy Operating Cost Per Unit", f'$ {tractorCostPerHourRounded}', help=f'Hours to formulate full batch divided by amount of units per batch, times the pitsy robot cost per hour')
    col2.metric("Total Standard Contract Manufactruer Operating Cost", f'$ {tractorTotalRoudned}', help=f'Covering {acres} total batches at $4.50 per unit')

    #Area graph of cost
    st.area_chart(data=df, x="Units produced (units)")