import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('Larkin_Audio_SMB_Data_Set.csv')

# print(data.columns())

data_cost = data[' Total Cost '].str.replace(r'[^\d\-+\.]', repl='', regex=True).astype(float)
print(data_cost.sample(5))
