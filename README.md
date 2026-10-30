Real Estate Price Analysis

A Python-based exploratory data analysis project to understand the
factors associated with residential property prices in Gurugram,
India. The project analyses property listings to compare localities,
property types, builders, BHK configurations, property status and RERA
approval.


Project Overview

The goal is to explore questions such as:
- Which locality has the highest average property price?
- Which locality has the highest price per square foot?
- Are ready-to-move properties priced higher than under-construction
  properties?
- Do RERA-approved properties command a price premium?
- How are property area, BHK configuration and property type related
  to price?
- Which builders or companies have the highest average price per
  square foot?

  
The analysis uses 14,223 property listings and a dataset containing
12 columns.

Tools & Technologies
- Python -- analysis
- Pandas -- data cleaning and manipulation
- NumPy -- numerical operations
- Matplotlib -- data visualisation
- Seaborn -- statistical visualisation
- Excel -- cleaned dataset format


Dataset

The project report identifies clean_data.xlsx as the cleaned dataset.
It contains 14,223 rows and 12 columns, with no missing values after
cleaning.

Column            Description
price           Property price in rupees
status          Ready to move / under construction
area            Property area in square feet
rate_per_sqft   Price per square foot
property_type   Property type
locality        Neighbourhood or locality
builder_name    Builder name
rera_approval   RERA approval status
bhk_count       Number of BHKs
society         Society or project name
company_name    Company name
flat_type       Apartment, floor, plot, villa, penthouse or house


Key Analysis & Findings

The project investigates ten questions and reports the following key
findings:
1. Costliest listing: A 6 BHK apartment in DLF Camellias, Sector
   42, priced at approximately ₹122.63 crore.
2. Locality with highest average price: Baliawas in the analysed
   listings.
3. Locality with highest rate per square foot: Sector 42, at
   approximately ₹55,989/sqft.
4. Property status: Ready-to-move properties had a slightly higher
   average price than under-construction properties (₹4.15 crore vs
   ₹3.96 crore).
5. RERA approval: The analysis did not find a price premium for
   RERA-approved properties (₹3.86 crore vs ₹4.08 crore for non-RERA
   properties).
6. Area vs total price: A positive relationship was observed after
   removing five area outliers (correlation of approximately 0.63).
7. BHK vs rate per square foot: The report identifies 7 BHK as the
   highest average rate configuration after treating 114 BHK entries as
   plot-data errors.
8. Property type: Villas had the highest average rate per square
   foot (approximately ₹17,740); penthouses had the highest average
   total price (approximately ₹13.8 crore).
9. Builders/companies: Camelliaass, Cameliaas and Tulip were among
   the highest average-rate names in the report.
10. Area vs rate per square foot: No meaningful relationship was
    observed (correlation of approximately 0.08).
These are findings from this dataset and analysis; they should not be
interpreted as a guarantee of current market prices.


Project Workflow

1. Load the cleaned Excel dataset.
2. Inspect the columns and data types.
3. Check data quality and identify unusual values/outliers.
4. Use Pandas and NumPy to group, aggregate and compare listings.
5. Create charts with Matplotlib and Seaborn.
6. Interpret the results to answer the ten analysis questions.


Conclusion

The analysis suggests that location and property size are important
factors associated with total property price in the dataset. Sector 42
and Sector 113 show high rates per square foot, villas lead on average
rate per square foot, and ready-to-move properties are slightly more
expensive on average. RERA approval alone did not correspond to a higher
average price in this analysis.


Future Improvements

- Standardise builder and company names to merge spelling variations.
- Build a machine-learning model to predict property prices.
- Extend the analysis to additional cities for comparison.


Author

Shivam

Delhi Technological University
