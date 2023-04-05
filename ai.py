'''

 /$$$$$$$  /$$   /$$                               /$$$$$$  /$$$$$$
| $$__  $$|__/  | $$                              /$$__  $$|_  $$_/
| $$  \ $$ /$$ /$$$$$$   /$$$$$$$ /$$   /$$      | $$  \ $$  | $$  
| $$$$$$$/| $$|_  $$_/  /$$_____/| $$  | $$      | $$$$$$$$  | $$  
| $$____/ | $$  | $$   |  $$$$$$ | $$  | $$      | $$__  $$  | $$  
| $$      | $$  | $$ /$$\____  $$| $$  | $$      | $$  | $$  | $$  
| $$      | $$  |  $$$$//$$$$$$$/|  $$$$$$$      | $$  | $$ /$$$$$$
|__/      |__/   \___/ |_______/  \____  $$      |__/  |__/|______/
                                  /$$  | $$                        
                                 |  $$$$$$/                        
                                  \______/                         

PitsyAI v1.1
Creator: Sean Jenkins
Created On: 4/5/23
Revised On: 4/6/23

Change Log:
v1.0 
- Created Calculator

v1.1
- Added multi-select functionality to ingredients list
- Added Calculate button
'''

import streamlit as st

st.title("AI Manufacturing Assistant")

st.sidebar.image("https://cdn.shopify.com/s/files/1/0624/6072/3426/files/logoincircle_100x.png?v=1662346828")

ingredientType = st.sidebar.multiselect("What type of ingredients are you using?", ("Coconut Oil", "Shea Butter", "Candelilla Wax", "Arrowroot Powder", "Kaolin Clay", "Zinc", "Castor Oil", "Vitamin E", "Activated Charcoal", "Fragrance"))

st.sidebar.slider("How many units are you trying to produce per batch?", 1, 100000)

st.write("Use the sidebar on the left to begin")

if st.sidebar.button('Calculate'):
    st.write('No Output')