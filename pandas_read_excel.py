import pandas as pd


file_name = "bones.xlsx"

# df = pd.read_excel(file_name, sheet_name=None)
df = pd.read_excel(file_name, sheet_name="Sheet1") # sheet_name needs to be passed correctly
# sheet_name='somename')

print(df)
print(df.columns)

# name of the first column
print(df.columns[0])

# subset of names and ages
df1 = df[[df.columns[0],df.columns[1]]]
print(df1)

# print unique names
df_names = pd.unique(df1[df1.columns[0]])
print(df_names)
print(len(df_names))

# convert to DataFrame to save to excel
# df_name_dataframe = pd.DataFrame(df_names)



df_name_dataframe = pd.DataFrame(	data=df_names	)

# print(df_name_dataframe)
df_name_dataframe.to_excel("names.xlsx")