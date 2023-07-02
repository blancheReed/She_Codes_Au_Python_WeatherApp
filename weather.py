import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    temperature = str(temp)
    return f"{temperature}{DEGREE_SYBMOL}"
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """ 


def convert_date(iso_string):
    date_obj = datetime.fromisoformat(iso_string)
    formatted_date = date_obj.strftime('%A %d %B %Y')
    return formatted_date

iso_date = "2021-07-05T07:00:00+08:00"
formatted_date = convert_date(iso_date)
print(formatted_date)


"""Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """



def convert_f_to_c(temp_in_f):
    temp_in_f = float(temp_in_f)
    temp_in_celsius = (temp_in_f - 32) * 5 / 9
    return round(temp_in_celsius, 1)

temperature_fahrenheit= "77.0"
temperature_celsius = convert_f_to_c(temperature_fahrenheit)

print(temperature_celsius)
"""Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """


def calculate_mean(weather_data):
    if len(weather_data) == 0:
        return 0.0  # Return 0 if the list is empty
    temperatures = [float(x) for x in weather_data]
    total = sum(temperatures)
    mean = total / len(temperatures)
    return mean

temperatures = [17, 23, 25, 22, 18]
mean = calculate_mean(temperatures)
print(mean)


"""Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """



def load_data_from_csv(csv_file, delimiter=','):
    with open(csv_file, 'r') as weather_file:
        csv_reader = csv.reader(weather_file, delimiter=delimiter)
        next(csv_reader)  # Skip the header row
        list_of_csv = []
        for row in csv_reader:
            if len(row) >= 3:  # Make sure each row has at least 3 elements
                date = row[0]
                min_temp = int(row[1])
                max_temp = int(row[2])
                list_of_csv.append([date, min_temp, max_temp])
    
    return list_of_csv

csv_file = 'tests/data/example_one.csv'
delimiter = ' '  # Change the delimiter to the appropriate value if needed
data = load_data_from_csv(csv_file, delimiter=delimiter)
print(data)


"""Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """


def find_min(weather_data):
    if len(weather_data) == 0:
        return ()  # Return empty tuple if the list is empty

    min_value = float('inf')
    min_position = None
    last_duplicate_position = None
    seen_values = {}

    for i in range(len(weather_data)):
        value = weather_data[i]

        if isinstance(value, str):
            value = float(value)

        if value <= min_value:
            min_value = value
            min_position = i

        seen_values[value] = i

    if min_position is not None:
        last_duplicate_position = seen_values.get(min_value)

    return (min_value, last_duplicate_position) if min_position is not None else ()

temperatures = [20, 23, 16, 25, 19, 23, 16, 25]
min_value, last_duplicate_position = find_min(temperatures)
print("Minimum value:", min_value)
print("Position of last duplicate value:", last_duplicate_position)




"""Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The miniumum value and it's position in the list.
    """


def find_max(weather_data):
    if len(weather_data) == 0:
        return ()  # Return empty tuple if the list is empty

    max_value = float('-inf')
    max_position = None
    last_duplicate_position = None
    seen_values = {}

    for i in range(len(weather_data)):
        value = weather_data[i]

        if isinstance(value, str):
            value = float(value)

        if value >= max_value:
            max_value = value
            max_position = i

        seen_values[value] = i

    if max_position is not None:
        last_duplicate_position = seen_values.get(max_value)

    return (max_value, last_duplicate_position) if max_position is not None else ()

temperatures = [20, 23, 16, 25, 19, 23, 16, 25]
max_value, last_duplicate_position = find_max(temperatures)
print("Maximum value:", max_value)
print("Position of last duplicate value:", last_duplicate_position)


"""Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """



# def generate_summary(weather_data):

# def convert_date(iso_string):
#     date_obj = datetime.fromisoformat(iso_string)
#     formatted_date1 = date_obj.strftime('%A %d %B %Y')
#     return formatted_date1

# def find_min1(weather_data):
#     if len(weather_data) == 0:
#         return None, None

#     min_value = float('inf')
#     min_date1 = None

#     for data in weather_data:
#         if data[1] <= min_value:
#             min_value = data[1]
#             min_date1 = data[0]

#     return min_value, min_date1

# def find_max1(weather_data):
#     if len(weather_data) == 0:
#         return None, None

#     max_value = float('-inf')
#     max_date1 = None

#     for data in weather_data:
#         if data[2] >= max_value:
#             max_value = data[2]
#             max_date1 = data[0]

#     return max_value, max_date1

# def generate_summary(weather_data):
#     num_days = len(weather_data)
#     min_temp, min_date1 = find_min1(weather_data)
#     max_temp, max_date1 = find_max1(weather_data)
#     formatted_date1 = convert_date(min_date1)

#     avg_low = sum(day[1] for day in weather_data) / num_days
#     avg_high = sum(day[2] for day in weather_data) / num_days

#     summary = f"{num_days} Day Overview\n"
#     summary += f"The lowest temperature will be {min_temp:.1f}°C, and will occur on {formatted_date1}.\n"
#     summary += f"The highest temperature will be {max_temp:.1f}°C, and will occur on {convert_date(max_date1)}.\n"
#     summary += f"The average low this week is {avg_low:.1f}°C.\n"
#     summary += f"The average high this week is {avg_high:.1f}°C.\n"

#     return summary


# def convert_f_to_c(temp_in_f):
#     temp_in_f = float(temp_in_f)
#     temp_in_celsius = (temp_in_f - 32) * 5 / 9
#     return round(temp_in_celsius, 1)

# temp_in_f = [
#     ["2021-07-02T07:00:00+08:00", 49, 67],
#     ["2021-07-03T07:00:00+08:00", 57, 68],
#     ["2021-07-04T07:00:00+08:00", 56, 62],
#     ["2021-07-05T07:00:00+08:00", 55, 61],
#     ["2021-07-06T07:00:00+08:00", 53, 62]
# ]

# temp_in_celsius = [[data[0], convert_f_to_c(data[1]), convert_f_to_c(data[2])] for data in temp_in_f]

# summary = generate_summary(temp_in_celsius)
# print(summary)


def convert_date(iso_string):
    date_obj = datetime.fromisoformat(iso_string[:10])
    formatted_date1 = date_obj.strftime('%A %d %B %Y')
    return formatted_date1

def find_min1(weather_data):
    if len(weather_data) == 0:
        return None, None

    min_value = float('inf')
    min_date1 = None

    for data in weather_data:
        if data[1] <= min_value:
            min_value = data[1]
            min_date1 = data[0]

    return min_value, min_date1

def find_max1(weather_data):
    if len(weather_data) == 0:
        return None, None

    max_value = float('-inf')
    max_date1 = None

    for data in weather_data:
        if data[2] >= max_value:
            max_value = data[2]
            max_date1 = data[0]

    return max_value, max_date1

def generate_summary(weather_data):
    num_days = len(weather_data)
    min_temp, min_date1 = find_min1(weather_data)
    max_temp, max_date1 = find_max1(weather_data)
    formatted_date1 = convert_date(min_date1)

    avg_low = sum(day[1] for day in weather_data) / num_days
    avg_high = sum(day[2] for day in weather_data) / num_days

    summary = f"{num_days} Day Overview\n"
    summary += f"The lowest temperature will be {min_temp:.1f}°C, and will occur on {formatted_date1}.\n"
    summary += f"The highest temperature will be {max_temp:.1f}°C, and will occur on {convert_date(max_date1)}.\n"
    summary += f"The average low this week is {avg_low:.1f}°C.\n"
    summary += f"The average high this week is {avg_high:.1f}°C.\n"

    return summary


def convert_f_to_c(temp_in_f):
    temp_in_f = float(temp_in_f)
    temp_in_celsius = (temp_in_f - 32) * 5 / 9
    return round(temp_in_celsius, 1)

temp_in_f = [
    ["2021-07-02T07:00:00+08:00", 49, 67],
    ["2021-07-03T07:00:00+08:00", 57, 68],
    ["2021-07-04T07:00:00+08:00", 56, 62],
    ["2021-07-05T07:00:00+08:00", 55, 61],
    ["2021-07-06T07:00:00+08:00", 53, 62]
]

temp_in_celsius = [[data[0], convert_f_to_c(data[1]), convert_f_to_c(data[2])] for data in temp_in_f]

summary = generate_summary(temp_in_celsius)
print(summary)


"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """


# def generate_daily_summary(weather_data):


# def convert_date(iso_string):
#     date_obj = datetime.fromisoformat(iso_string)
#     formatted_date2 = date_obj.strftime('%A %d %B %Y')
#     return formatted_date2

# def generate_daily_summary(weather_data):
#     summary = ""
#     for data in weather_data:
#         date = convert_date(data[0])
#         min_temp = data[1]
#         max_temp = data[2]
#         summary += f"---- {date} ----\n"
#         summary += f"  Minimum Temperature: {min_temp:.1f}°C\n"
#         summary += f"  Maximum Temperature: {max_temp:.1f}°C\n\n"
#     return summary

# data = [
#     ['2021-07-02', 9.4, 19.4],
#     ['2021-07-03', 13.9, 20.0],
#     ['2021-07-04', 13.3, 16.7],
#     ['2021-07-05', 12.8, 16.1],
#     ['2021-07-06', 11.7, 16.7]
# ]

# summary = generate_daily_summary(data)
# print(summary)

from datetime import datetime

def convert_f_to_c(temp_in_f):
    temp_in_celsius = (temp_in_f - 32) * 5 / 9
    return round(temp_in_celsius, 1)

def convert_date(iso_string):
    date_obj = datetime.fromisoformat(iso_string)
    formatted_date2 = date_obj.strftime('%A %d %B %Y')
    return formatted_date2

def generate_daily_summary(weather_data):
    summary = ""
    for data in weather_data:
        date = data[0][:10]  # Extract the date part from the ISO8601 string
        min_temp = convert_f_to_c(data[1])
        max_temp = convert_f_to_c(data[2])
        summary += f"---- {convert_date(date)} ----\n"
        summary += f"  Minimum Temperature: {min_temp:.1f}°C\n"
        summary += f"  Maximum Temperature: {max_temp:.1f}°C\n\n"
    return summary

data = [
    ['2021-07-02T07:00:00+08:00', 49, 67],
    ['2021-07-03T07:00:00+08:00', 57, 68],
    ['2021-07-04T07:00:00+08:00', 56, 62],
    ['2021-07-05T07:00:00+08:00', 55, 61],
    ['2021-07-06T07:00:00+08:00', 53, 62]
]

summary = generate_daily_summary(data)
print(summary)


"""Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

