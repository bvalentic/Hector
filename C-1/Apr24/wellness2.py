import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('WELLNESS_COST_2022_CW_V2  - Sheet1.tsv', sep='\t')
data.rename(columns=lambda x: x.strip(), inplace=True)

# print(data.head())

job_desc_totals = data.groupby('JOB DESC')['TOTAL'].sum()
highest_total_job_desc = job_desc_totals.idxmax()
highest_total = job_desc_totals.max()

print(highest_total_job_desc, highest_total)
