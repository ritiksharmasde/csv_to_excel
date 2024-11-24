# -----------------------------------------------------------this below program converts CSV file to Excel file which we scrapped from worldometer------Ritk sharma---------
# =======CSV TO EXCEL CONVERTOR ======PROGRAM NUMBER 25=================
import pandas as pd
df = pd.read_csv("output1.csv")

df.to_excel("input2.xlsx", index=False)


print("CSV file output converted to Excel file input successfully!")