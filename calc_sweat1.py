import streamlit as st

formulations = {
    "Pitsy": [
        "Coconut Oil",
        "Shea Butter",
        "Candelilla Wax",
        "Kaolin Clay",
        "Arrowroot Powder",
        "Magnesium Hydroxide",
        "Zinc",
        "Castor Oil",
        "Vitamin E",
        "Activated Charcoal",
        "Fragrance",
    ],
    "Native": [
        "Caprylic/Capric Triglyceride",
        "Tapioca Starch",
        "Ozokerite",
        "Sodium Bicarbonate (Baking Soda)",
        "Magnesium Hydroxide",
        "Cocos Nucifera (Coconut) Oil",
        "Cyclodextrin",
        "Butyrospermum Parkii (Shea) Butter",
        "Dextrose",
        "Lactic Acid",
        "Natural Fragrance",
    ],
    "Super Natural Super Sweat": [
        "Glycerin",
    "Aqua (water)",
    "Maranta Arundinacea Root (Arrowroot) Powder",
    "Propanediol",
    "Sodium Stearate",
    "Hydrated Silica",
    "Saccharomyces Ferment Filtrate",
    "Aloe Barbadensis Leaf Juice",
    "Maltodextrin",
    "Allantoin",
    "Salicylic Acid",
    "Sorbic Acid",
    "Charcoal",
    "Magnesium Hydroxide",
    "Benzyl Alcohol",
    "Potassium Sorbate",
    "Sodium Benzoate",
    "Cedrus Atlantica (Cedarwood) Bark Oil",
    "Thuja Occidentalis Leaf",
    "Pogostemon Cablin Oil (Patchouli Oil)"
    ],
}

st.title('Formulation Calculator')
selected_formulation = st.selectbox("Choose a formulation:", list(formulations.keys()))

st.write(f"Selected formulation: {selected_formulation}")
st.write("Ingredients:")
for ingredient in formulations[selected_formulation]:
    st.write(ingredient)

st.write('Please enter the amount of each ingredient in grams.')

total_amount = 0
ingredient_percentages = {}

with st.sidebar:
    st.header('Ingredients')
    ingredient_amounts = {}
    for ingredient in formulations[selected_formulation]:
        ingredient_amounts[ingredient] = st.number_input(ingredient, min_value=0.0, step=0.1)

    if st.button('Calculate Total'):
        total_amount = sum(ingredient_amounts.values())
        for ingredient, amount in ingredient_amounts.items():
            percentage = (amount / total_amount) * 100 if total_amount > 0 else 0
            ingredient_percentages[ingredient] = round(percentage, 2)

# Display the total amount and percentages in the main area
if total_amount > 0:
    st.write(f'Total amount of all ingredients: **{total_amount} grams**')
    st.write('Percentage of each ingredient:')
    for ingredient, percentage in ingredient_percentages.items():
        st.write(f'{ingredient}: {percentage}%')