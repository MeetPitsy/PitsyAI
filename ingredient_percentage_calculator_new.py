import pandas as pd

# Traditional natural deodorant ingredients
traditional_data = {
    'Ingredient': ['Aluminum Chlorohydrate', 'Aluminum Zirconium Tetrachlorohydrex', 'Baking Soda', 'Cornstarch',
                   'Arrowroot Powder', 'Potassium Alum', 'Tea Tree Oil', 'Lavender Oil', 'Eucalyptus Oil',
                   'Aloe Vera', 'Chamomile Extract', 'Calendula Extract', 'Probiotics', 'Coconut Oil', 'Shea Butter',
                   'Palm Oil', 'Cetyl Alcohol', 'Stearyl Alcohol'],
    'Function': ['Antiperspirant', 'Antiperspirant', 'Odor neutralizer, Absorbent', 'Absorbent', 'Absorbent',
                 'Mineral salt, Antimicrobial', 'Antimicrobial', 'Antimicrobial, Fragrance', 'Antimicrobial, Fragrance',
                 'Soothing, Moisturizing', 'Soothing, Anti-inflammatory', 'Soothing, Anti-inflammatory',
                 'Odor control, Skin microbiome balance', 'Moisturizing, Antimicrobial', 'Moisturizing, Soothing',
                 'Moisturizing, Emollient', 'Emollient, Thickening agent', 'Emollient, Thickening agent'],
    'Relevant Characteristics': ['May cause skin irritation in sensitive individuals',
                                 'May cause skin irritation in sensitive individuals',
                                 'May cause skin irritation or rash in some people', 'Generally safe for most skin types',
                                 'Generally safe for most skin types', 'Low risk of irritation, may not be as effective',
                                 'May cause allergic reactions or irritation', 'May cause allergic reactions or irritation',
                                 'May cause allergic reactions or irritation', 'Generally safe for most skin types',
                                 'Generally safe for most skin types', 'Generally safe for most skin types',
                                 'Generally safe, may not work for everyone', 'May cause skin irritation or acne in some people',
                                 'Generally safe for most skin types', 'Environmental concerns, harmful supply chain',
                                 'May cause skin irritation in sensitive individuals',
                                 'May cause skin irritation in sensitive individuals']
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
pitsy_df = pd
