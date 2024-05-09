import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('WELLNESS_COST_2022_CW_V2  - Sheet1.tsv', sep='\t')

# print(data.head())

data_primavera = data[data['COST_CENTER'] == 'PRIMAVERA']

print(data_primavera['JOB DESC'].value_counts().to_markdown())
