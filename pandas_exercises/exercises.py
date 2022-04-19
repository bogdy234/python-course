import matplotlib.pyplot as mathplotvar
import pandas

# dataset = {
#     'cars': ["BMW", "Dacia", "Ford"],
#     'color': ["red", "black", "gray"],
# }

# variable = pandas.DataFrame(dataset)
# print(variable)

# colors = ['red', 'black', 'gray']
# anotherVariable = pandas.Series(colors, index=['x', 'y', 'z'])
# print(anotherVariable)
# print(anotherVariable['z'], anotherVariable[2])

# dataset = {"BMW": "red", "Dacia": "black", "Ford": "gray"}
# variable = pandas.Series(dataset, index=["Dacia", "Ford"])
# print(variable)

# dataset = {
#     'cars': ["BMW", "Dacia", "Ford"],
#     'color': ["red", "black", "gray"],
# }

# variable = pandas.DataFrame(
#     dataset, index=['producer1', 'producer2', 'producer3'])
# print(variable.loc[0]) nu mai merge aici pt ca am alocat un label
# print(variable.loc['producer1'])

# print(pandas.options.display.max_rows)


# data = {
#     "Duration": {
#         "0": 60,
#         "1": 60,
#         "2": 60,
#         "3": 45,
#         "4": 45,
#         "5": 60
#     },
#     "Pulse": {
#         "0": 110,
#         "1": 117,
#         "2": 103,
#         "3": 109,
#         "4": 117,
#         "5": 102
#     },
#     "Maxpulse": {
#         "0": 130,
#         "1": 145,
#         "2": 135,
#         "3": 175,
#         "4": 148,
#         "5": 127
#     },
#     "Calories": {
#         "0": 409,
#         "1": 479,
#         "2": 340,
#         "3": 282,
#         "4": 406,
#         "5": 300
#     }
# }

# df = pandas.DataFrame(data)
# print(df)
# print(df.tail(2))
# print(df.head(2))
# print(df.info())

df = pandas.read_csv('test.csv')
# print(df)
for i in df.index:
    # print(i)
    # print(df.loc[i, 'AL'])
    pass

# print(df.corr())
# print(df.describe())
# print(df.mean())

# df.plot(kind='scatter', x='AT', y='BE')
# df['AT'].plot(kind='hist')
# mathplotvar.show()

# df.fillna(0, inplace=True)  # inplace true -> modify in the same place
# print(df.fillna(0))

# replace NaN with 0

# df['AL'].fillna(0, inplace=True)  # inplace true -> modify in the same place
# print(df.fillna(0))

# df.loc[7, 'AL'] = 45
# print(df)

df.fillna(0, inplace=True)  # inplace true -> modify in the same place

df.replace(': ', 0, inplace=True)
df.replace(':', 0, inplace=True)

print(df)
print(df.transpose())

df.to_csv('test1.csv')
