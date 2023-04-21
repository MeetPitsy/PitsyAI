import streamlit as st

def main():
    st.title("Pitsy Custom CPG Product Creation")
    
    st.header("1. Choose a CPG Product")
    cpg_product = st.selectbox("Select a product to customize:", ["Deodorant", "Shampoo", "Body Wash", "Lotion"])
    
    if cpg_product:
        st.header("2. Branding Lab")
        branding_option = st.radio("Select a branding option:", ["Pitsy Studios", "Custom Branding"])
        
        if branding_option == "Pitsy Studios":
            st.write("Pitsy Studios branding will be applied to your product.")
        else:
            st.write("Design your custom branding here.")
            # Add custom branding options here (e.g., color schemes, design templates)

        st.header("3. Product Lab")
        if cpg_product == "Deodorant":
            st.write("Pitsy Deodorants Formulation:")
            value_propositions = [
                "Genderless",
                "Compostable packaging",
                "All-natural ingredients",
                "Vegan",
                "Long-lasting protection",
                "No baking soda"
            ]
            for value_prop in value_propositions:
                st.write(f"- {value_prop}")

        # Add value proposition options here for other products (e.g., vegan, eco-friendly, hypoallergenic)

        st.header("4. Select Materials")
        material_options = {
            "Impacked": "https://www.impackedpackaging.com/",
            "Eco Packables": "https://www.ecopackables.com/?gclid=Cj0KCQjwxYOiBhC9ARIsANiEIfZ6b5k4-K_IHbagql6fEihm8M6Sqlb2J4U_Ew8ItyrGVk0GRmnUuwcaArmUEALw_wcB"
        }
        selected_material = st.selectbox("Select a material:", list(material_options.keys()))
        if st.button("Visit Material Supplier"):
            st.write(f"Click the link to visit {selected_material}'s website: {material_options[selected_material]}")

        st.header("5. Ingredient Selection")
        ingredient_options = ["Native Ingredients", "Salt and Stone Ingredients", "Pitsy's Formulation"]
        selected_ingredient = st.selectbox("Select an ingredient option:", ingredient_options)
        
        st.header("6. Choose Manufacturing")
        manufacturing_option = st.radio("Select a manufacturing option:", ["Pitsy Automation", "Other"])
        
        st.header("7. Formulation Choice")
        formulation_choice = st.selectbox("Select a formulation:", ["Traditional Natural", "Pitsy Signature Blend"])

        st.header("8. Fragrance Selection")
        if cpg_product == "Deodorant":
            awesome_fragrances = {
                "Aqua Breeze": "Fresh, clean scent with notes of citrus, aquatic, or herbal elements",
                "Floral Fantasy": "Delicate and feminine, featuring flower extracts like rose, jasmine, or lavender",
                "Earthy Embrace": "Woody, earthy, and warm, with notes of sandalwood, cedarwood, and patchouli",
                "Fruit Fusion": "Lively and fruity, with scents such as peach, apple, strawberry, and tropical fruits",
                "Exotic Enchantment": "Spicy, oriental, or exotic, incorporating cinnamon, ginger, cardamom, vanilla, amber, or oud",
                "Active Energy": "Invigorating and energizing for an active lifestyle, featuring peppermint, menthol, or green tea",
                "Pure & Simple": "Unscented, suitable for sensitive skin or those who prefer no added fragrances",
            }
            fragrance_choice = st.selectbox("Select a fragrance:", list(awesome_fragrances.keys()))
            st.write(awesome_fragrances[fragrance_choice])
        else:
            fragrance_choice = st.selectbox("Select a fragrance:", ["Santal", "Coconut", "Amber"])
        
        st.header("9. Unit Quantity")
        unit_quantity = st.number_input("Enter the number of units:", min_value=1, max_value=10000)
        
        st.header("10. Sales and Marketing Collaboration")
        collaborate = st.checkbox("Would you like to collaborate with Pitsy's Sales and Marketing team?")
        
        if st.button("Confirm and Begin Batching"):
            st.success("Your custom CPG product has been submitted for production!")
            # Add production and delivery logic here

if __name__ == "__main__":
    main()
