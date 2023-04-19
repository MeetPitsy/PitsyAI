import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def determine_sentiment(characteristic):
    positive_words = ['safe', 'soothing', 'balance', 'moisturizing']
    negative_words = ['irritation', 'rash', 'allergic reactions', 'harmful', 'concerns', 'acne']

    sentiment = 'Positive'
    for word in negative_words:
        if word in characteristic.lower():
            sentiment = 'Negative'
            break

    return sentiment

def plot_combined_sentiment_distribution(traditional_df, pitsy_df):
    traditional_sentiment_counts = traditional_df['Sentiment'].value_counts()
    pitsy_sentiment_counts = pitsy_df['Sentiment'].value_counts()

    labels = ['Positive', 'Negative']
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, traditional_sentiment_counts, width, label='Traditional', color='b')
    rects2 = ax.bar(x + width/2, pitsy_sentiment_counts, width, label='Pitsy', color='g')

    ax.set_title('Sentiment Distribution in Deodorant Ingredients')
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Count')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    st.pyplot(fig)
    plt.clf()

traditional_data = {
    'Ingredient': [
        'Aluminum Chlorohydrate', 'Aluminum Zirconium Tetrachlorohydrex', 'Baking Soda', 'Cornstarch', 'Arrowroot Powder',
        'Potassium Alum', 'Tea Tree Oil', 'Lavender Oil', 'Eucalyptus Oil', 'Benzyl Acetate', 'Polyglyceryl-3 Stearate',
        'Methyl Benzoate', 'Hexyl Cinnamal', 'Magnesium Ascorbyl Phosphate', 'Behenyl Alcohol', 'Palm Oil',
        'Cetyl Alcohol', 'Stearyl Alcohol'
    ],
    'Function': [
        'Antiperspirant', 'Antiperspirant', 'Odor neutralizer, Absorbent', 'Absorbent', 'Absorbent',
        'Mineral salt, Antimicrobial', 'Antimicrobial', 'Antimicrobial, Fragrance', 'Antimicrobial, Fragrance', 'Soothing, Moisturizing',
        'Soothing, Anti-inflammatory', 'Soothing, Anti-inflammatory', 'Odor control, Skin microbiome balance', 'Moisturizing, Antimicrobial',
        'Moisturizing, Soothing', 'Moisturizing, Emollient', 'Emollient, Thickening agent', 'Emollient, Thickening agent'
    ],
    'Relevant Characteristics': [
        'May cause skin irritation in sensitive individuals', 'May cause skin irritation in sensitive individuals',
        'May cause skin irritation or rash in some people', 'Generally safe for most skin types', 'Generally safe for most skin types',
        'Low risk of irritation, may not be as effective', 'May cause allergic reactions or irritation', 'May cause allergic reactions or irritation',
        'May cause allergic reactions or irritation', 'Generally safe for most skin types', 'Generally safe for most skin types',
        'Generally safe for most skin types', 'Generally safe, may not work for everyone', 'May cause skin irritation or acne in some people',
        'Generally safe for most skin types', 'Environmental concerns, harmful supply chain', 'May cause skin irritation in sensitive individuals',
        'May cause skin irritation in sensitive individuals'
    ],
    'Sentiment': [
        'Negative', 'Negative', 'Negative', 'Negative', 'Positive', 'Negative', 'Negative', 'Negative', 'Negative', 'Negative',
        'Negative', 'Negative', 'Negative', 'Negative', 'Negative', 'Negative', 'Negative', 'Negative'
    ]
}

# Pitsy deodorant ingredients
pitsy_data = {
    'Ingredient': ['Coconut Oil', 'Shea Butter', 'Candelilla Wax', 'Arrowroot Powder', 'Kaolin Clay', 'Zinc',
                    'Castor Oil', 'Vitamin E', 'Magnesium Hydroxide', 'Activated Charcoal'],
    'Function': ['Moisturizing, Antimicrobial', 'Moisturizing, Soothing', 'Texture, Emollient', 'Absorbent',
                    'Absorbent, Gentle exfoliation', 'Odor neutralizer, Antimicrobial', 'Moisturizing, Emollient',
                    'Antioxidant, Moisturizing', 'Odor neutralizer, pH balancing', 'Absorbent, Odor neutralizer'],
    'Relevant Characteristics': ['May cause skin irritation or acne in some people', 'Generally safe for most skin types',
                                    'Plant-based alternative to beeswax; generally safe', 'Generally safe for most skin types',
                                    'Generally safe for most skin types', 'Generally safe, may cause irritation in high concentrations',
                                    'Generally safe for most skin types', 'Generally safe, rare allergic reactions',
                                    'Generally safe for most skin types', 'Generally safe for most skin types']
}

traditional_df = pd.DataFrame(traditional_data)
pitsy_df = pd.DataFrame(pitsy_data)

traditional_df['Sentiment'] = traditional_df['Relevant Characteristics'].apply(determine_sentiment)
pitsy_df['Sentiment'] = pitsy_df['Relevant Characteristics'].apply(determine_sentiment)

st.title("Comparison of Sentiment in Traditional Natural Deodorant and Pitsy Deodorant Ingredients")

# Display combined sentiment bar chart
plot_combined_sentiment_distribution(traditional_df, pitsy_df)

# Display tables
st.subheader("Traditional Natural Deodorant Ingredients")
st.write(traditional_df)

st.subheader("Pitsy Deodorant Ingredients")
st.write(pitsy_df)

import streamlit as st
import pandas as pd

# ... (previous code for DataFrames and functions)

st.title("Deodorant Ingredients Comparison")

# Sidebar calculator
st.sidebar.title("Deodorant Calculator")
st.sidebar.write("Choose a base deodorant or build your own:")

option = st.sidebar.selectbox(
    "", ["Build your own", "Traditional Natural Deodorant", "Pitsy Deodorant"]
)

ingredients = list(set(traditional_df["Ingredient"].tolist() + pitsy_df["Ingredient"].tolist()))

if option == "Build your own":
    custom_deodorant = {}
    for ingredient in ingredients:
        percentage = st.sidebar.slider(ingredient, 0.0, 100.0, 0.0, 0.1)
        custom_deodorant[ingredient] = percentage
    st.sidebar.write("Custom Deodorant Composition:")
    st.sidebar.write(custom_deodorant)

elif option == "Traditional Natural Deodorant":
    st.sidebar.write("Traditional Natural Deodorant Composition:")
    st.sidebar.write("Enter your own percentages for the ingredients:")
    traditional_percentages = {}
    for ingredient in traditional_df["Ingredient"]:
        percentage = st.sidebar.slider(ingredient, 0.0, 100.0, 0.0, 0.1)
        traditional_percentages[ingredient] = percentage
    st.sidebar.write(traditional_percentages)

elif option == "Pitsy Deodorant":
    st.sidebar.write("Pitsy Deodorant Composition:")
    st.sidebar.write("Enter your own percentages for the ingredients:")
    pitsy_percentages = {}
    for ingredient in pitsy_df["Ingredient"]:
        percentage = st.sidebar.slider(ingredient, 0.0, 100.0, 0.0, 0.1)
        pitsy_percentages[ingredient] = percentage
    st.sidebar.write(pitsy_percentages)

# ... (previous code for data visualization)
