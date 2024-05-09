import pandas
import numpy
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_columns', None)

data = pandas.read_csv('WELLNESS_COST_2022_CW_V2  - Sheet1.tsv', sep='\t')
data.rename(columns=lambda x: x.strip(), inplace=True)

# print(data.head())

data["YEARLY"] = data[['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 'DECEMBER']].sum(axis=1)

# print(data["YEARLY"])

data_cluster = data[['EMPLOYEE', 'YEARLY']]

data_cluster['YEARLY_scaled'] = StandardScaler().fit_transform(data_cluster[['YEARLY']])

inertia = []
k_values = range(1, 11)

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init='auto')
    kmeans.fit(data_cluster[['YEARLY_scaled']])
    inertia.append(kmeans.inertia_)

plt.figure(figsize=(8, 6))
plt.plot(k_values, inertia, marker='o')
plt.title('Elbow Method for Optimal k')
plt.xlabel('Number of Clusters (k)')
plt.ylabel('Inertia')
plt.xticks(k_values)
plt.show()
