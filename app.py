import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import streamlit as st

med_data = pd.read_csv('insurance.csv')

med_data.replace({'sex':{'male':0,'female':1}},inplace=True)
med_data.replace({'smoker':{'yes':0,'no':1}},inplace=True)
med_data.replace({'region':{'southeast':0,'southwest':1,'northwest':2,'northeast':3}},inplace=True)

X = med_data.drop('charges',axis=1)
y = med_data['charges']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=2)
lg = LinearRegression()
lg.fit(X_train,y_train)
y_pred = lg.predict(X_test)

def convert_to_numeric(value, options):
    return options.index(value)

def main():
    st.title("Medical Insurance Cost Prediction")
    #st.markdown("<h1 class='title'>Health Insurance Cost Prediction</h1>", unsafe_allow_html=True)


    #st.sidebar.header("Input Parameters")
    age = st.number_input("Enter age", min_value=0, step=1)
    sex = st.selectbox("Select sex", ["Female", "Male"])
    bmi = st.number_input("Enter BMI", min_value=0.0, step=0.1)
    children = st.number_input("Enter number of children", min_value=0, step=1)
    smoker = st.selectbox("Are you a smoker?", ["No", "Yes"])
    region = st.selectbox("Select region", ["Northeast", "Northwest", "Southeast", "Southwest"])

    sex = convert_to_numeric(sex, ["Female", "Male"])
    smoker = convert_to_numeric(smoker, ["No", "Yes"])
    region = convert_to_numeric(region, ["Northeast", "Northwest", "Southeast", "Southwest"])


    
    sex = 0 if sex == "Female" else 1
    smoker = 0 if smoker == "No" else 1

    
    if st.button("Predict"):
        
        np_data = np.array([[age, sex, bmi, children, smoker, region]])

       
        prediction = lg.predict(np_data)

        
        st.success(f"Predicted Medical Insurance Cost: ${prediction[0]:.2f}")

        st.image("insurance.jpeg", use_column_width=True)
        st.markdown("[Learn more about factors affecting insurance costs](https://www.healthcare.gov/how-plans-set-your-premiums/)")


if __name__ == "__main__":
    main()