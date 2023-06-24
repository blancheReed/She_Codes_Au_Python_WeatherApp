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


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    pass
