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
        return None  # Return None if the list is empty

    min_value = min(weather_data)
    min_index = weather_data.index(min_value)
    min_index = int(min_index)
    return min_value, min_index

temperatures = [20, 23, 16, 25, 19]
min_value, min_index = find_min(temperatures)
print("Minimum value:", min_value)
print("Position:", min_index)


"""Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """


def find_max(weather_data):
    if len(weather_data) == 0:
        return None, None  # Return None if the list is empty

    max_value = max(weather_data)
    max_index = weather_data.index(max_value)
    max_index = int(max_index)
    return max_value, max_index

temperatures = [20, 24, 18, 21, 23]
max_value, max_index = find_max(temperatures)
print("Maximum value:", max_value)
print("Position:", max_index)

"""Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """



def generate_summary(weather_data):
    num_days = len(weather_data)
    min_temp = min(temperatures[1] for temperatures in weather_data)
    max_temp = max(temperatures[2] for temperatures in weather_data)
    avg_low = sum(temperatures[1] for temperatures in weather_data) / num_days
    avg_high = sum(temperatures[2] for temperatures in weather_data) / num_days

    summary = f"Weather Summary\n"
    summary += f"Number of days: {num_days}\n"
    summary += f"The lowest temperature will be {min_temp:.1f}{DEGREE_SYBMOL}\n"
    summary += f"The highest temperature will be {max_temp:.1f}{DEGREE_SYBMOL}\n"
    summary += f"The average low this week is {avg_low:.1f}{DEGREE_SYBMOL}\n"
    summary += f"The average high this week is {avg_high:.1f}{DEGREE_SYBMOL}\n"

    return summary

temperatures = [
    ['2021-07-02', 49, 67],
    ['2021-07-03', 57, 68],
    ['2021-07-04', 56, 62],
    ['2021-07-05', 55, 61],
    ['2021-07-06', 53, 62]
]

summary = generate_summary(temperatures)
print(summary)

"""Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
