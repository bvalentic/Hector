import numpy
import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('uk_universities.csv')

# print(data.head())
# print(data.info())

for column_name in ["Student_satisfaction", "CWUR_score"]:
  if not pandas.api.types.is_numeric_dtype(data[column_name]):
    data[column_name] = pandas.to_numeric(data[column_name].str.replace("%", repl="", regex=True))

correlation = numpy.corrcoef(data['CWUR_score'], data['Student_satisfaction'])[0, 1]
print(f"Overall correlation between CWUR score and student satisfaction: {correlation:.3f}")

correlations_by_region = data.groupby('Region')[['CWUR_score', 'Student_satisfaction']].corr().unstack()[('CWUR_score', 'Student_satisfaction')]
correlations_by_region = correlations_by_region.sort_values(ascending=False)
print(correlations_by_region)
