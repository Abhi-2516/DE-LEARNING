# making UI from streamlit

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import streamlit as st

data = pd.read_csv("data.csv")

x = data[["years_of_experience"]]
y = data["salary"]

# Create a linear regression model
model = LinearRegression()
model.fit(x, y)

st.title("Salary Prediction App")

st.write("This app predicts the salary based on years of experience using a linear regression model.")

st.write("Enter the years of experience to predict the salary:")
years_of_experience = st.number_input("Years of Experience", min_value=0.0 , max_value=50.0 , step=0.1)

if years_of_experience > 0:
    predicted_salary = model.predict([[years_of_experience]])[0]
    st.success(f"Predicted Salary: {predicted_salary:,.2f}") 
    
st.subheader("Regression Line")

fig, ax = plt.subplots()
ax.scatter(x, y, color="blue", label="Actual Data")
ax.plot(x, model.predict(x), color="red", label="Regression line")
ax.set_xlabel("Years of experience")
ax.set_ylabel("Salary")
ax.set_title("Salary vs Experience")
ax.legend()

st.pyplot(fig)
    

    

