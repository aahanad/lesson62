import pandas as pd
data=pd.DataFrame({
    "Name":["sophie","lizzy","annabelle"],
    "Age":[12,13,11],
    "City":["Redmond","Kirkland","Bellevue"]
})
#Basic utilities to explore data:
#head– shows the first few rows
# describe() – gives summary statistics
# info() – shows data types and missing values
# shape – shows the number of rows and columns
# columns – lists all column names
print(data.head())
print(data.describe())
print(data.info())