import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_excel('Gas_Prices.xlsx')

# print(data.head())

data['World Share + GDP Per Capita'] = data['World Share'] * data['GDP Per Capita ( USD )']

print(data.head())
