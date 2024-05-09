import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('website_traffic_by_language_2020-2021.csv')

# print(data.head())

data_2021 = data[data['Year'] == 2021]

# print(data_2021.info())

language_counts = data_2021['Language'].value_counts().reset_index(name='Count').set_axis(['Language', 'Count'], axis=1)

print(language_counts)
