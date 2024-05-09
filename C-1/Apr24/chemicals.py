import pandas
import numpy
from scipy.stats import norm

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('EQUIP-CHEMICALS.csv')

# print(data.head())

data_price = data['Total Price ']
# print(data_price.sample(5))

data_cleaned = data.dropna(subset=['Total Price ']) # remove missing values
data_cleaned['Total Price'] = pandas.to_numeric(data_cleaned['Total Price '], errors='coerce').fillna(0) # change str to int
data_cleaned['Total Price Adjusted'] = data_cleaned['Total Price'].apply(lambda x: x if x > 0 else 1) # make values positive
data_cleaned['Total Price Log'] = numpy.log(data_cleaned['Total Price Adjusted']) # put on log scale

mean_log = data_cleaned['Total Price Log'].mean()
std_dev_log = data_cleaned['Total Price Log'].std()
weights_log = norm.pdf(data_cleaned['Total Price Log'], loc=mean_log, scale=std_dev_log)

print(weights_log)
