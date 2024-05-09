import pandas
import matplotlib.pyplot as plt

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('top_200_youtubers.csv')
data.rename(columns=lambda x: x.strip(), inplace=True)

# print(data.head())
# print(data.sample(5))

# Filter for 'Like Nastya' and select relevant columns
data_nastya = data[data['Channel Name'] == 'Like Nastya'][['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day']]

# print(data_nastya.count)

# Normalize values across 1 day
data_nastya['Avg. 1 Day'] = data_nastya['Avg. 1 Day'] / 1
data_nastya['Avg. 3 Day'] = data_nastya['Avg. 3 Day'] / 3
data_nastya['Avg. 7 Day'] = data_nastya['Avg. 7 Day'] / 7
data_nastya['Avg. 14 Day'] = data_nastya['Avg. 14 Day'] / 14
data_nastya['Avg. 30 day'] = data_nastya['Avg. 30 day'] / 30
data_nastya['Avg. 60 day'] = data_nastya['Avg. 60 day'] / 60

data_out = data_nastya.melt(value_vars=['Avg. 1 Day', 'Avg. 3 Day', 'Avg. 7 Day', 'Avg. 14 Day', 'Avg. 30 day', 'Avg. 60 day'], var_name='Days', value_name='Daily Average')

day_mapping = {'Avg. 1 Day': 1, 'Avg. 3 Day': 3, 'Avg. 7 Day': 7, 'Avg. 14 Day': 14, 'Avg. 30 day': 30, 'Avg. 60 day': 60}
data_out['Days'] = data_out['Days'].map(day_mapping)

data_out = data_out.reset_index(drop=True)

plt.figure(figsize=(10, 6))
plt.plot(data_out['Days'], data_out['Daily Average'], marker='o', linestyle='-')
plt.title('Daily Average Viewers Over Time for Like Nastya')
plt.xlabel('Days')
plt.ylabel('Daily Average Viewers')
plt.xticks(data_out['Days'])
plt.grid(axis='y', linestyle='--')
plt.show()
