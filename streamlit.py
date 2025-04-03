import streamlit as st
import pandas as pd
import joblib
import lightgbm as lgb  

@st.cache_resource
def load_model():
    return joblib.load('best_lgbm_model.joblib')

model = load_model()

# User Inputs
gender = st.selectbox('Gender', ['Male', 'Female'])
age = st.number_input('Age', min_value=18, max_value=100, value=30)
driving_license = st.selectbox('Driving License', [0, 1])
region_code = st.number_input('Region Code', min_value=0, value=28)
previously_insured = st.selectbox('Previously Insured', [0, 1])
annual_premium = st.number_input('Annual Premium', min_value=0, value=30000)
policy_sales_channel = st.number_input('Policy Sales Channel', min_value=1, max_value=163, value=23)
vintage = st.number_input('Vintage (in days)', min_value=0, max_value=300, value=150)
vehicle_age_lt_1_year = st.selectbox('Vehicle age < 1 year', [0, 1])
vehicle_age_gt_2_years = st.selectbox('Vehicle age > 2 years', [0, 1])
vehicle_damage_yes = st.selectbox('Vehicle Damage', [0, 1])

if st.button('Predict'):
    # Creating input DataFrame
    input_data = pd.DataFrame([[
        gender, age, driving_license, region_code, previously_insured,
        annual_premium, policy_sales_channel, vintage, vehicle_age_lt_1_year,
        vehicle_age_gt_2_years, vehicle_damage_yes]],
                            columns=['Gender', 'Age', 'Driving_License', 'Region_Code', 'Previously_Insured',
                            'Annual_Premium', 'Policy_Sales_Channel', 'Vintage', 'Vehicle_Age_LT_1_Year',
                            'Vehicle_Age_GT_2_Years', 'Vehicle_Damage'])

    # Encoding categorical variables
    input_data['Gender'] = input_data['Gender'].map({'Male': 0, 'Female': 1})

prediction=model.predict(input_data)
probability=model.predict_proba(Input_data)[0][1]

st.write(f'Prediction:{"Interested" if prediction[0]==1 else "Not Interested"}')
st.write(f'Probability of being interested:{probability:.2f}')
