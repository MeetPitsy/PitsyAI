import streamlit as st

# Start the app
st.title("Ingredient Calculator")

# Define the ingredients with their default amounts
ingredients = {
    "Coconut Oil": 100,
    "Shea Butter": 50,
    "Candelillia Wax": 100,
    "Kaolin Clay": 2,
    "Arrowroot Powder": 100,
    "Zinc": 20,
    "Castor Oil": 10,
    "Magnesium Hydroxide": 100,
    "Activated Charcoal": 80,
}

# Add a sidebar for user input
st.sidebar.title("Enter ingredient amounts")

# Create sliders for each ingredient on the sidebar
for ingredient, amount in ingredients.items():
    ingredients[ingredient] = st.sidebar.slider(ingredient, 0, 1000, amount)

# Calculate the total amount of ingredients
total_amount = sum(ingredients.values())

# Display the results
st.write("Total amount of ingredients:")
st.write(total_amount)

# Show the breakdown of ingredients
st.write("Ingredient breakdown:")
for ingredient, amount in ingredients.items():
    st.write(f"{ingredient}: {amount}")