import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('Larkin_Audio_SMB_Data_Set.csv')

# print(data.head())

data_cost = data[' Total Cost']
print(data_cost.sample(5))
