
import streamlit as st
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import StandardScaler
import numpy as np
import os
from sklearn.preprocessing import LabelEncoder
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier



model_load_path = "rfm.pkl"
with open(model_load_path, 'rb') as file:
    unpickled_model = pickle.load(file)
    
# Define the custom CSS style
custom_style = """
<style>
.frame {
    border: length 1000px, width 800px, white;
    padding: 10px;
}

.title {vc
    font-family: Arial, sans-serif;
    color: ;
    font-size: 24px;
    font-weight: bold;
}

.label {
    font-size: 16px;
    margin-bottom: 5px;
}

.input {
    padding: 5px;
    border: 1px solid #ccc;
    border-radius: 4px;
    width: 200px;
}

.button {
    background-color: blue;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    font-weight: bold;
}

.button:hover {
    background-color: red;
}
</style>
"""

st.markdown(custom_style, unsafe_allow_html=True)

# Add the title with custom style
st.markdown('<div class="frame"><h1>Loan Default Predictor</h1></div>', unsafe_allow_html=True)


# Collect user inputs for prediction
# Collect user inputs for prediction as integers
PaidDay = st.number_input('Enter the Paid Day', step=1, value=1)
PaidMonth = st.number_input('Enter the Paid Month', step=1, value=1)
PaidYear = st.number_input('Enter the Paid Year', step=1, value=2023)
DueDay = st.number_input('Enter the Due Day', step=1, value=1)
DueMonth = st.number_input('Enter the Due Month', step=1, value=1)
DueYear = st.number_input('Enter the Due Year', step=1, value=2023)


# ... (your other code)

# with open("knn.pkl", 'rb') as file:
#     unpickled_model = pickle.load(file)
# Add a button to make predictions
if st.button('Predict'):
   

    # Step 5: Prepare the user input as a DataFrame
    user_input = pd.DataFrame({
        "PaidOnYear": [PaidYear],
        "PaidOnMonth": [PaidMonth],
        "PaidOnDay": [PaidDay],
        "DueYear": [DueYear],
        "DueMonth": [DueMonth],
        "DueDay": [DueDay]
    })



    # Step 6: Scale the user input using the same scaler used during training


    # scaler = StandardScaler()
    # scaler.fit(user_input)
    # ScaledX = pd.DataFrame(scaler.transform(user_input), index=user_input.index, columns=user_input.columns)
    
    # Step 7: Make predictions using the loaded model (unpickled_model)
    default_prediction = unpickled_model.predict(user_input)
    if default_prediction  == 0:
        default_prediction = "Not Default"
    else:
        default_prediction = "Default"
    
    # Step 8: Display the predicted result (default_prediction)
    st.write("The predicted result is:",default_prediction)
    
   


