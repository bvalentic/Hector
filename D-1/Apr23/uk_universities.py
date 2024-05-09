import pandas
from scipy.stats import pearsonr

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

# Read the csv file
data = pandas.read_csv('uk_universities.csv')

print(data.head())
# print(data.info())

factors = ['World_rank', 'Minimum_IELTS_score', 'UG_average_fees_(in_pounds)', 'PG_average_fees_(in_pounds)', 'Estimated_cost_of_living_per_year_(in_pounds)']
correlations = {}
for factor in factors:
  correlation, _ = pearsonr(data['Student_satisfaction'], data[factor])
  correlations[factor] = correlation
for factor, correlation in correlations.items():
  print(f"Correlation between Student_satisfaction and {factor}: {correlation:.3f}")
