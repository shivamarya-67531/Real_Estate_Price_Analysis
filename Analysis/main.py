import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_excel('Analysis/clean_data.xlsx')
# print(df.info())

# Question 1: Which is the costliest flat in the dataset?
# costliest_flat = df.loc[df['price'].idxmax()]
# print("Costliest Flat Details:")
# costliest_flat_sentence = f"The costliest flat is a {costliest_flat['bhk_count']} BHK and type is {costliest_flat['property_type']} located in {costliest_flat['locality']}, built by {costliest_flat['builder_name']}. It is priced at {costliest_flat['price']/10000000:.2f} Crores and has an area of {costliest_flat['area']} sqft with a rate of {costliest_flat['rate_per_sqft']} per sqft. The flat is currently {costliest_flat['status']}."
# print(costliest_flat)
# print("\nCostliest Flat Description:")
# print(costliest_flat_sentence)


# Question 2: Which locality has the highest average price?
# locality_avg_price = df.groupby('locality')['price'].mean().idxmax()
# print("\nHighest Average Prices by Locality:", locality_avg_price)
# print(df.groupby('locality')['price'].mean().sort_values(ascending=False).head(10))


# Question 3: Which locality has the highest rate per sqft?
# locality_rate_per_sqft = df.groupby('locality')['rate_per_sqft'].mean().idxmax()
# print("\nHighest Rate per sqft by Locality:", locality_rate_per_sqft)
# print(df.groupby('locality')['rate_per_sqft'].mean().sort_values(ascending=False).head(10))


# Question 4: Do ready to move properties cost more than the under-construction properties?
# ready_to_move_avg_price = df[df['status'] == 'ready to move']['price'].mean()
# under_construction_avg_price = df[df['status'] == 'under construction']['price'].mean()
# if ready_to_move_avg_price > under_construction_avg_price:
#     print("\nYes, ready to move properties cost more than under-construction properties.")
# else:
#     print("\nNo, under-construction properties cost more than ready to move properties.")


# Question 5: Do RERA-approved properties command a price premium?
# rera_approved_avg_price = df[df['rera_approval'] == True]['price'].mean()
# non_rera_approved_avg_price = df[df['rera_approval'] == False]['price'].mean()
# if rera_approved_avg_price > non_rera_approved_avg_price:
#     print("\nYes, RERA-approved properties command a price premium.")
# else:
#     print("\nNo, RERA-approved properties do not command a price premium.")


# Question 6: How does area (sqft) impact property price?
# sns.scatterplot(data=df, x='area', y='price')
# plt.show()
# print('Area does not have significant impact on property price as there is no clear trend in the scatter plot.')


# Question 7: Which BHK configuration is the most expensive on average based on rate per sqft?
# most_expensive_bhk = df.groupby('bhk_count')['rate_per_sqft'].mean().idxmax()
# print(f"\nThe most expensive BHK configuration on average is: {most_expensive_bhk} BHK with an average rate of {df.groupby('bhk_count')['rate_per_sqft'].mean().max():.2f} per sqft.")


# Question 8: Which property type (Apartment, Floor, Plot) is the costliest?
# costliest_flat_type = df.groupby('flat_type')['rate_per_sqft'].mean().idxmax()
# print(f"\nThe costliest property type on average is: {costliest_flat_type} with an average rate of {df.groupby('flat_type')['rate_per_sqft'].mean().max():.2f} per sqft.")


# Question 9: Do certain builders or companies consistently price higher?
# print(f'Top 5 builders/companies with the highest average rate per sqft are: {df.groupby("company_name")["rate_per_sqft"].mean().sort_values(ascending=False).head(5).index.tolist()}.')


# Question 10: Are larger homes always more expensive per square foot?
df = pd.read_excel('Analysis/clean_data.xlsx')
sns.scatterplot(data=df, x='area', y='rate_per_sqft')
plt.show()
print('No, larger homes are not always more expensive per square foot as there is no clear trend in the scatter plot.')
larger_homes_expensive = df.groupby('area')['rate_per_sqft'].mean().sort_values(ascending=False).head(5).index.tolist()
print(f"\nLarger homes with the highest average rate per sqft are: {larger_homes_expensive} sqft.")