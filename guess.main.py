import csv


temp = []
with open("weather_data.csv", mode='r') as info:
    row = csv.reader(info)
    for data in row:
        print(data)
        if data[1] != "temp":
            temp.append(int(data[1]))

print(temp)
