"""
    generate our own dataset
    
"""
import pandas as pd
import numpy as np

np.random.seed(42)

years = np.random.uniform(0.5 , 10 , 100).round(2)

salary = (30000 + years * 6000 + np.random.normal(0 , 4000 , 100)).round(2)


df = pd.DataFrame({"years_of_experience" : years , "salary" : salary}).to_csv("data.csv" , index = False)

df.to_csv("exp_salaries.csv" , index = False)

print("Dataset generated and saved to exp_salaries.csv")

