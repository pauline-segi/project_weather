import csv
from datetime import datetime
import py_compile

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns: 
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


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
    data_list = []
    with open(csv_file, mode="r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for row in csv_reader:
            if row and all(row):
                data_list.append([row[0],int(row[1]),int(row[2])])
    return data_list


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
    # print(max_value)
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
        if not day_data:  
                continue

        date_string = day_data[0]
        temperature_min = float(day_data[1])
        temperature_max = float(day_data[2])

        rounded_min = round(temperature_min, 1)
        rounded_max = round(temperature_max, 1)

        temperature_min = (temperature_min - 32) * 5 / 9
        temperature_max = (temperature_max - 32) * 5 / 9

        date = datetime.fromisoformat(date_string)
        date_string = date.strftime("%B %d, %Y")

        summary += f"The lowest temperature will be {rounded_min}{DEGREE_SYMBOL}, and will occur on {date_string}:\n"
        summary += f"The highest temperature will be {rounded_max}{DEGREE_SYMBOL}, and will occur on {date_string}:\n"
        summary += f"The average low this week is {rounded_min}{DEGREE_SYMBOL} - {rounded_max}{DEGREE_SYMBOL}\n"
        summary += f"The average high this week is {rounded_max}{DEGREE_SYMBOL} - {rounded_min}{DEGREE_SYMBOL}\n"
    return summary.strip()

# THIS CODE IS ERRORING!!



def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = "5 Day Overview\n"

    for day_data in weather_data:
        date_obj = datetime.fromisoformat(day_data[0])
        date_str = date_obj.strftime("%A %d %B %Y")
        min_temp_fahrenheit = float(day_data[1])
        max_temp_fahrenheit = float(day_data[2])

        # Convert temperatures to Celsius
        min_temp_celsius = (min_temp_fahrenheit - 32) * 5 / 9
        max_temp_celsius = (max_temp_fahrenheit - 32) * 5 / 9

        summary += f"---- {date_str} ----\n"
        summary += "  Minimum Temperature: {:.1f}{}\n".format(min_temp_celsius, DEGREE_SYMBOL)
        summary += "  Maximum Temperature: {:.1f}{}\n\n".format(max_temp_celsius, DEGREE_SYMBOL)

    return summary.rstrip()


# THIS CODE IS ERRORING!!