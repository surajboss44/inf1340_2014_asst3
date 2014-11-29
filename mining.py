#!/usr/bin/env python3

""" Docstring """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"

__copyright__ = "2014 Susan Sim"
__license__ = "MIT License"

__status__ = "Prototype"

# imports one per line
import json
import datetime
from operator import itemgetter

global stock_year_list
stock_year_list = []
final_list = []


def read_stock_data(stock_file_name):
    """

    :param stock_file_name:
    :return:
    """
    try:
        with open(stock_file_name, "r") as file_reader:
            global stock_file_content
            stock_file_content = file_reader.read()
        try:
            global stock_records
            stock_records = json.loads(stock_file_content)
            print(calculate_stock_price(stock_records))
            print(six_worst_months())
            print(six_best_months())
            # print(stock_records)
            #print(stock_records[0])
        except ValueError:
            return "No values in the JSON file"
    except FileNotFoundError:
        return "JSON file not found"
        # try:
        # stock_records = json.loads(stock_file_content)
        #  function1(stock_records, '2008', '08')
        #except ValueError:
        #    return "No values in the JSON file"
    except FileNotFoundError:
        return "JSON file not found"


def calculate_stock_price(input_stock_records):
    """

    :param input_stock_records:
    :return:
    """
    stock_year_list_with_duplicates = []
    # closing_stock_value = []
    #monthly_sales = 0
    #monthly_volume = 0
    #monthly_sales_data = ()
    #for item in range(len(input_stock_records)):
    for each_stock_record in input_stock_records:
        stock_year_month = each_stock_record["Date"][0:7]
        stock_year_list_with_duplicates.append(stock_year_month)
    for temp_item in stock_year_list_with_duplicates:
        if temp_item not in stock_year_list:  # Removing duplicate occurrence of "YYYY-MM"
            stock_year_list.append(temp_item)
    for date_item in stock_year_list:
        average = calculate_average_for_a_month(input_stock_records, date_item)
        monthly_stock_average = (date_item, average)  # Tuple for storing monthly average stock price
        final_list.append(monthly_stock_average)  # List for storing average stock price of all months
    #print("final_list "+str(final_list))
    return final_list


def calculate_average_for_a_month(input_stock_records, month_val):
    """

    :param input_stock_records:
    :param month_val:
    :return:
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
            average_monthly_price = monthly_sales / monthly_volume
    return average_monthly_price


def six_worst_months():
    six_worst_months_data = sorted(final_list, key=itemgetter(1))
    # six_worst_months_data_sorted = sorted(six_worst_months_data, key=itemgetter(1))
    return six_worst_months_data[0:6]


def six_best_months():
    """


    :return:
    """
    six_best_months_data = []
    six_best_months_data_sorted = []
    # six_best_months_data = sorted(final_list, key=itemgetter(1))
    six_best_months_data_sorted = sorted(final_list, reverse=True, key=itemgetter(1))
    return six_best_months_data_sorted[0:6]


"""
def read_json_from_file(file_name):
    with open(file_name) as file_handle:
        file_contents = file_handle.read()

    return json.loads(file_contents)
"""

read_stock_data("data\GOOG.json")