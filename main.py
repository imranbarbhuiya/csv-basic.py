import pandas

# data = pandas.read_csv("weather_data.csv")
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)

# Mean temperature
# average_temp = sum(temp_list) / len(temp_list)
# print(average_temp)

# Mean using pandas
# mean = data["temp"].mean()
# print(mean)

# highest number
# highest = data["temp"].max()
# print(highest)

# get a row
# row = data[data.day == "Monday"]
# print(row)

# Create a dataframe
data_dict = {
    "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
    "temp": [1, 2, 3, 4, 5],
    "humidity": [1, 2, 3, 4, 5]
}

data = pandas.DataFrame(data_dict)
# print(data)

data.to_csv("new_data.csv")