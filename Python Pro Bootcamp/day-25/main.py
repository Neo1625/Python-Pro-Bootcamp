#with open("weather_data.csv") as data_file:
#    data = data_file.readlines()
#    print(data)

#import csv

#with open("weather_data.csv") as data_file:
#    data = csv.reader(data_file)
#    temperatures = []
#    for row in data:
#        if row[1] == "temp":
#            pass
#        else:
#            temperatures.append(int(row[1]))

#print(temperatures)

import pandas

#data = pandas.read_csv("weather_data.csv")
#print(type(data))
#print(data["temp"])

#data_to_dict = data.to_dict()
#print(data_to_dict)

#temp_list = data["temp"].to_list()
#print(len(temp_list))

#average = data["temp"].mean()
#print(average)

#print(max_temp)

#Get data in columns
#print(data["condition"])
#print(data.condition)

#Get data in a row
#print(data[data.day == "Monday"])

#print(data[data.temp == data["temp"].max()])

#monday = data[data.day == "Monday"]
#print((monday.temp * (9/5)) + 32)

#data_dict = {
#    "students": ["Amy", "James", "Angela"],
#    "scores": [76, 56, 65]
#}

#data = pandas.DataFrame(data_dict)
#print(data)
#data.to_csv("new_data.csv")

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#Gray = data["Primary Fur Color"].value_counts()["Gray"]
#Cinnamon = data["Primary Fur Color"].value_counts()["Cinnamon"]
#Black = data["Primary Fur Color"].value_counts()["Black"]

Gray = len(data[data["Primary Fur Color"] == "Gray"])
Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
Black = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur color": ["Gray", "Cinnamon", "Black"],
    "Count": [Gray, Cinnamon, Black]
}

print(data["Primary Fur Color"])

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")