import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data.csv')
# print(df.head())
# print(df.info())

# data cleaning
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(df.columns.tolist())
# print(df)

# numeric columns cleaning
df['price'] = (df['price'].astype(str).str.replace(',', '').astype(int))
df['rate_per_sqft'] = (df['rate_per_sqft'].astype(str).str.replace(',', '').astype(int))
# print(df.info())

# categorical columns cleaning
df['status'] = df['status'].str.lower().str.strip()
df['locality'] = df['locality'].str.lower().str.strip()
df['rera_approval'] = df['rera_approval'].str.lower().str.strip()
df['rera_approval'] = df['rera_approval'].map({'approved by rera': True, 'not approved by rera': False})
df['property_type'] = df['property_type'].str.lower().str.strip()
df['builder_name'] = df['builder_name'].str.lower().str.strip()
df['flat_type'] = df['flat_type'].str.lower().str.strip()
df['society'] = df['society'].str.lower().str.strip()
df['company_name'] = df['company_name'].str.lower().str.strip()
df = df.drop_duplicates()


print(df.head())
print(df.info())

# download as excel file 
df.to_excel('clean_data.xlsx', index=False)