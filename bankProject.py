import pdfplumber
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Path to your PDF file
pdf_path = 'bank_df.pdf'

# Open the PDF file
with pdfplumber.open(pdf_path) as pdf:
    # Iterate over each page
    for page in pdf.pages:
        # Extract table data
        table = page.extract_table()
        if table:
            # Convert to DataFrame
            df = pd.DataFrame(table[1:], columns=table[0])
            print(df['Total Income'])

TotalIncomeArray = df['Total Income'].to_numpy()
def clean_and_convert(value):
    # Remove parentheses and commas
    cleaned_value = value.replace('(', '').replace(')', '').replace(',', '')
    # Convert to float
    return float(cleaned_value)
cleaned_array = np.array([clean_and_convert(val) for val in TotalIncomeArray])

# Convert the cleaned array to integers (if needed)
TotalIncomeArrayInt = cleaned_array.astype(int)

print(np.median(TotalIncomeArrayInt))
plt.hist(TotalIncomeArrayInt)
plt.show()

