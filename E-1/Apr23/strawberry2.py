import pandas

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('STRAWBERRY SALES 2023 - Sheet1.tsv', sep='\t', skiprows=2)

# print(data.head())

data['$/BOX'] = data['$/BOX'].str.replace('[$, ]', '', regex=True).astype(float)
data['TOTAL'] = data['TOTAL'].str.replace('[$, ]', '', regex=True).astype(float)

data_out = data.groupby(['PRODUCT', 'TYPE OF PRODUCT'])[['$/BOX', '#KILOS', 'TOTAL']].agg(
    Average_Price_Per_Box=('$/BOX', 'mean'),
    Total_Kilos_Sold=('#KILOS', 'sum'),
    Total_Revenue=('TOTAL', 'sum')
).round(2).reset_index()

# print(data_out.head())

data['DATE'] = pandas.to_datetime(data['DATE'], format="mixed").dt.to_period('M')
merged_data = data.merge(data_out)
organic_strawberries = merged_data[merged_data['TYPE OF PRODUCT'] == 'ORGANIC']

monthly_revenue = organic_strawberries.groupby(organic_strawberries['DATE'].dt.month)['TOTAL'].sum()
average_monthly_revenue = organic_strawberries.groupby(organic_strawberries['DATE'].dt.month)['TOTAL'].mean()
higher_than_average = monthly_revenue[monthly_revenue > average_monthly_revenue]

print(higher_than_average)
