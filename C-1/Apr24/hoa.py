import pandas
import matplotlib.pyplot as plt

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('hoa_transactions.csv')
data.rename(columns=lambda x: x.strip(), inplace=True)

# print(data.head())

# Convert Date into datetime, only keep the valid dates.
data['date'] = pandas.to_datetime(data['Date'], format="%d-%b", errors='coerce').dropna()

corr_expense = data['date'].astype('int64').corr(data['Expenses'])
print(f'Correlation coefficient between Date (as timestamp) and Expenses: {corr_expense}')

corr_income = data['date'].astype('int64').corr(data['Income'])
print(f'Correlation coefficient between Date (as timestamp) and Income: {corr_income}')

# expenses vs date
plt.figure(figsize=(10, 6))
plt.scatter(data['date'], data['Expenses'])
plt.title('Date vs Expenses')
plt.xlabel('Date')
plt.ylabel('Expenses')
plt.xticks(rotation=45, ha='right')
plt.locator_params(axis='y', nbins=10)
plt.tight_layout()
plt.show()

# income vs date
plt.scatter(data['date'], data['Income'])
plt.title('Date vs Income')
plt.xlabel('Date')
plt.ylabel('Income')
plt.xticks(rotation=45, ha='right')
plt.locator_params(axis='y', nbins=10)
plt.tight_layout()
plt.show()


