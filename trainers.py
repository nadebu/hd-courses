"""
This is responsible for managing of the trainer's who have signed up to deliver a course
Future iterations of this will create a join between the list of trainers and that of trainees
"""

import pandas as pd

df_trainers = pd.read_excel(
    "assets\\trainers\\Training Schedule.xlsx",
    sheet_name=0,  # Rather than hard coding the name of the sheet, uses first sheet
    skiprows=13,
    usecols="B:R",
    engine="openpyxl",
)

print(df_trainers.head())
df_trainers["single_trainer"] = (
    df_trainers["Trainer"].str.split().str[0].str.rstrip(",").str.rstrip(";")
)


print(df_trainers["single_trainer"].unique())
