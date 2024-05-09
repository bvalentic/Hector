import pandas
import numpy

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('top_200_youtubers.csv')

# print(data.head())
# print(data.sample(5))

data_followers = data['followers ']
# print(data_followers.sample(5))

data['K_followers'] = data_followers / 1000
data['Unit'] = 'K'

print(data[['followers ', 'K_followers', 'Unit']].sample(5))
