#!/usr/bin/env python3

""" Docstring """

__author__ = 'Sam Novak and Suraj Narayanan'

# imports one per line
import json
import datetime
from operator import itemgetter

stock_year_list = []
final_list = []
six_best_months_data_sorted = []
six_worst_months_data_sorted = []


def read_stock_data(stock, stock_file_name):

    """
    Reads JSON file and calls functions for processing

    :param stock_file_name: The name of a JSON formatted file that contains stock price data
    :param stock: The name of the stock
    :return: Program returns exceptions for value and file errors. Calls function calculate_stock_price
             to process stock data
    """

    global stock_year_list
    global final_list
    clear_globals()

    try:
        with open(stock_file_name, "r") as file_reader:
            global stock_file_content
            stock_file_content = file_reader.read()
        try:
            global stock_records
            stock_records = json.loads(stock_file_content)
            calculate_stock_price(stock_records)
        except ValueError:
            return ValueError("No values in the JSON file")

    except FileNotFoundError:
        return FileNotFoundError("JSON file not found")


def clear_globals():
    """
    A function to reset global variables to any json file being passed
    """
    global stock_year_list
    global final_list
    stock_year_list, final_list = [], []


def calculate_stock_price(input_stock_records):
    """
    Reads JSON file and calls functions for processing

    :param input_stock_records: Stock record data
    :return: list of tuples containing year, month, and average stock price
    """

    global final_list
    stock_year_list_with_duplicates = []

    for each_stock_record in input_stock_records:
        stock_year_month = each_stock_record["Date"][0:7]
        stock_year_list_with_duplicates.append(stock_year_month)
    for temp_item in stock_year_list_with_duplicates:
        if temp_item not in stock_year_list:  # Removing duplicate occurrence of YYYY-MM
            stock_year_list.append(temp_item)
    for date_item in stock_year_list:
        average = calculate_average_for_a_month(input_stock_records, date_item)
        monthly_stock_average = (date_item, round(average, 2))  # Tuple for storing monthly average stock price
        final_list.append(monthly_stock_average)  # List for storing average stock price of all months
    return final_list


def calculate_average_for_a_month(input_stock_records, month_val):
    """
    Reads JSON file and calls functions for processing

    :param input_stock_records: Stock record data
    :param month_val: month being evaluated
    :return: list of tuples containing year, month, and average stock price
    """
    monthly_sales = 0
    monthly_volume = 0
    for each_stock_record in input_stock_records:
        stock_year_month = each_stock_record["Date"][0:7]
        if month_val == stock_year_month:
            daily_total_sales = float(each_stock_record["Volume"]) * float(each_stock_record["Close"])
            daily_volume = int(each_stock_record["Volume"])
            monthly_sales += daily_total_sales
            monthly_volume += daily_volume
    if monthly_volume == 0:
        return 0
    else:
        return monthly_sales / monthly_volume


def six_worst_months():
    global final_list
    global six_worst_months_data
    six_worst_months_data = sorted(final_list, key=itemgetter(1))
    return six_worst_months_data[0:6]


def six_best_months():
    """
    :return:
    """
    global final_list
    global six_best_months_data_sorted
    six_best_months_data_sorted = sorted(final_list, reverse=True, key=itemgetter(1))
    return six_best_months_data_sorted[0:6]


"""
def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)
"""
#print(read_stock_data("GOOG", ""))
#
# print(six_worst_months())
