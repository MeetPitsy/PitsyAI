import mols2grid
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from rdkit import Chem
from rdkit.Chem.Descriptors import ExactMolWt

st.set_page_config(page_title="Pitsy Studio Labs", layout="wide")

st.title("Pitsy Studio Labs")

lab_options = [
    "Select a lab",
    "Inventory Kits",
    "Manufacturing Modules",
    "Pitsy Labs App",
    "Customizable Lab Experience",
    "Ontology",
    "Value Proposition",
]
selected_lab = st.selectbox("Choose a lab:", lab_options)

@st.cache(allow_output_mutation=True)
def download_dataset():
    """Loads once then cached for subsequent runs"""
    df = pd.read_csv(
        "https://www.cureffi.org/wp-content/uploads/2013/10/drugs.txt", sep="\t"
    ).dropna()
    return df

def calc_mw(smiles_string):
    """Given a smiles string (ex. C1CCCCC1), calculate and return the molecular weight"""
    mol = Chem.MolFromSmiles(smiles_string)
    return ExactMolWt(mol)

if selected_lab == "Inventory Kits":
    st.write("Welcome to the Inventory Kits lab!")
    # Add Inventory Kits lab code here

elif selected_lab == "Manufacturing Modules":
    st.write("Welcome to the Manufacturing Modules lab!")
    # Add Manufacturing Modules lab code here

elif selected_lab == "Pitsy Labs App":
    st.write("Welcome to the Pitsy Labs App lab!")
    # Add Pitsy Labs App lab code here

elif selected_lab == "Customizable Lab Experience":
    st.write("Welcome to the Customizable Lab Experience lab!")
    # Add Customizable Lab Experience lab code here

elif selected_lab == "Ontology":
    st.write("Welcome to the Ontology lab!")
    # Add Ontology lab code here

elif selected_lab == "Value Proposition":
    st.write("Welcome to the Value Proposition lab!")
    # Add Value Proposition lab code here

elif selected_lab == "Select a lab":
    st.write("Please choose a lab from the dropdown menu.")

else:
    df = download_dataset().copy()
    df["mol_weight"] = df.apply(lambda x: calc_mw(x["smiles"]), axis=1)

    weight_cutoff = st.slider(
        label="Show compounds that weigh below:",
        min_value=0,
        max_value=500,
        value=150,
        step=10,
    )

    df_result = df[df["mol_weight"] < weight_cutoff]
    st.write(df_result)

    raw_html = mols2grid.display(df_result, mapping={"smiles": "SMILES"})._repr_html_()
    components.html(raw_html, width=900, height=900, scrolling=True)
