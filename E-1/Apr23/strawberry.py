import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('STRAWBERRY SALES 2023 - Sheet1.tsv', sep='\t', skiprows=2)

# print(data.head())

data['#UNIT'] = data['#CLAMSHELLS'] + data['#BOXES']

print(data.head())
