# We will work with liner regression in this project. We will use the sklearn library to implement linear regression on a dataset.

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv("data.csv")

x = data[["years_of_experience"]]
y = data["salary"]

# Create a linear regression model
model = LinearRegression()
model.fit(x, y)

data["predicted_salary"] = model.predict(x)
print("model coeffcient : " , round(model.coef_[0], 2))
print("model intercept : " , round(model.intercept_, 2))

plt.scatter(x,y, color = "blue" , label = "Actual Salary")

plt.plot(x, data["predicted_salary"], color = "red" , label = "Predicted Salary")
plt.xlabel("Years of Experience")
plt.ylabel("Salary")
plt.title("Linear Regression: Salary vs Years of Experience")
plt.legend()
plt.grid()
plt.tight_layout()
plt.show()

