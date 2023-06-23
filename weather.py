import csv
from datetime import datetime
import py_compile

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts an ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_time = datetime.fromisoformat(iso_string)
    new_date = date_time.strftime("%A %d %B %Y")
    # print(new_date)
    return new_date



def convert_f_to_c(temp_in_farenheit):
    """Converts a temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    if isinstance(temp_in_farenheit, str):
        temp_in_farenheit = float(temp_in_farenheit)
    deg_c = (temp_in_farenheit - 32) * 5 / 9
    round_degrees = round(deg_c, 1)
    # print(round_degrees)
    return round_degrees


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    weather_data = [float(data) for data in weather_data]
    return sum(weather_data) / len(weather_data)

if __name__ == "__main__":
    import sys
    sys.path.append('tests')

    import test_calculate_mean

    temperatures = test_calculate_mean.CalculateMeanTests()

    for data in temperatures:
        mean = calculate_mean(data)
        print("Mean value:", mean)



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    pass 

# it basically takes one function, csv_file, and whenever we refer to that, the csv_file will be whatever we're passing it in. the test function is to give different values and make sure it's working. we just need to implement the code and functions.

# press cmd and left click when hovering over a function and it will take you to the implementation of the function (use this in the test-files to find where the functions are, as there are a heap of functions)


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    if not weather_data:
        return ()

    try:
        float_data = [float(value) for value in weather_data]
        min_value = min(float_data)
        min_index = len(float_data) - 1 - float_data[::-1].index(min_value)
        # print(min_value)
        return min_value, min_index
    except ValueError:
        return ()


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if not weather_data:
        return ()

    max_value = float('-inf')
    max_index = None

    for i, value in enumerate(weather_data):
        try:
            numeric_value = float(value)
        except ValueError:
            continue
        
        if numeric_value >= max_value:
            max_value = numeric_value
            max_index = i
    print(max_value)
    return max_value, max_index



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    for day_data in weather_data:
        date_string = day_data[0]
        temperature_min = float(day_data[1])
        temperature_max = float(day_data[2])

        date = datetime.fromisoformat(date_string)
        date_string = date.strftime("%B %d, %Y")

        summary += f"Weather summary for {date_string}:\n"
        summary += f"Temperature: {temperature_min:.1f}{DEGREE_SYBMOL} - {temperature_max:.1f}{DEGREE_SYBMOL}\n\n"

    return summary.strip()

# THIS CODE IS ERRORING!!



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""
    
    for day_data in weather_data:
        date_obj = datetime.fromisoformat(day_data[0])
        date_str = date_obj.strftime("%A %d %B %Y")
        min_temp = day_data[1]
        max_temp = day_data[2]
        
        summary += f"Weather summary for {date_str}:\n"
        summary += f"Temperature range: {min_temp}{DEGREE_SYBMOL} - {max_temp}{DEGREE_SYBMOL}\n\n"

    return summary


# THIS CODE IS ERRORING!!