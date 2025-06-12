import streamlit as st
import joblib
import numpy as np

#Load the saved regression model
model = joblib.load('regression_model.joblib')

#streamlit app UI
st.title('Job Package Prediction Based on CGPA')
st.write('Enter your CGPA to predict the expected job package: ')

#user
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)

#Predict button
if st.button("Predict Package"):
    # Prepare input data for the model
    input_data=np.array([[cgpa]])

    #Predict the package
    prediction = model.predict(input_data)
    predicted_value= float(prediction[0]) #convert NumPy value to float

    #show the result
    st.success(f"Predicted package: {predicted_value:,.2f}LPA")