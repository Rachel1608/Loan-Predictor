import streamlit as st
import pickle
import numpy as np

# Load the model
with open('logistic_regression_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define a function to make predictions
def predict_loan_status(data):
    # Use the model to make predictions
    predictions = model.predict(data)
    return predictions

# Create a Streamlit app
st.title("Loan Status Predictor")

# Create a form to input data
st.subheader("Enter data to predict loan status:")

Gender = st.selectbox("Select Gender", ["Male", "Female"])
Married = st.selectbox("Select Marital Status", ["Yes", "No"])
Dependents = st.selectbox("Select Number of Dependents", ["0", "1", "2", "3+"])
Education = st.selectbox("Select Education Level", ["Graduate", "Not Graduate"])
Self_Employed = st.selectbox("Select Employment Status", ["Yes", "No"])
ApplicantIncome = st.number_input("Enter Applicant Income")
CoapplicantIncome = st.number_input("Enter Coapplicant Income")
LoanAmount = st.number_input("Enter Loan Amount")
Loan_Amount_Term = st.number_input("Enter Loan Amount Term")
Credit_History = st.selectbox("Select Credit History", ["Yes", "No"])
Property_Area = st.selectbox("Select Property Area", ["Urban", "Rural", "Semiurban"])

# Create a button to make predictions
if st.button("Predict"):
    # Convert categorical variables to numerical variables
    Gender = 1 if Gender == "Male" else 0
    Married = 1 if Married == "Yes" else 0
    Dependents = int(Dependents.replace("+", ""))
    Education = 1 if Education == "Graduate" else 0
    Self_Employed = 1 if Self_Employed == "Yes" else 0
    Credit_History = 1 if Credit_History == "Yes" else 0
    Property_Area = 2 if Property_Area == "Urban" else 1 if Property_Area == "Rural" else 0
    
    # Create a numpy array with numerical values
    data = np.array([[Gender, Married, Dependents, Education, Self_Employed, ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History, Property_Area]])
    
    # Make predictions
    predictions = predict_loan_status(data)
    # Display the 
    if prediction[0]==1:
        st.write('Prediction status: Yes')
    else:
        st.write('Prediction status: No')