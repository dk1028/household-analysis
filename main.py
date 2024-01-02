
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
pip install matplotlib
pip install pandas
pip install numpy
pip install openpyxl

* References
    - https://matplotlib.org/stable/api/
    - https://numpy.org/doc/stable/reference/
    - https://pandas.pydata.org/docs/reference/

"""

# Declare and initialize global variables
x_axis = None
y_axis_2020 = None
y_axis_2021 = None
y_axis_2022 = None
consumption_category = None
consumption_thismonth = None
sum_of_consumption_category = None
average_2020 = None
average_2021 = None
average_2022 = None


def main():
    set_data_from_excel()
    draw_linechart()
    draw_barchart()
    draw_piechart()

    plt.tight_layout()
    plt.show()
    return


# Import Excel data
def set_data_from_excel():
    global x_axis
    global y_axis_2020
    global y_axis_2021
    global y_axis_2022
    global consumption_category
    global consumption_thismonth
    global sum_of_consumption_category
    global average_2020

    global average_2021
    global average_2022
    dataframe = pd.read_excel("./LP-1-data.xlsx", sheet_name="Sheet1", header=None, index_col=None)
    x_axis = dataframe.iloc[0, 1:13].to_numpy()  # 선택한 행렬 데이터를 array 로 변환
    y_axis_2020 = dataframe.iloc[1, 1:13].to_numpy()
    y_axis_2021 = dataframe.iloc[2, 1:13].to_numpy()
    y_axis_2022 = dataframe.iloc[3, 1:13].to_numpy()
    consumption_category = dataframe.iloc[5, 1:5].to_numpy()
    consumption_thismonth = dataframe.iloc[6, 1:5].to_numpy()
    sum_of_consumption_category = np.nansum(consumption_thismonth, dtype="float16")
    average_2020 = np.nanmean(y_axis_2020, dtype="float16")
    average_2021 = np.nanmean(y_axis_2021, dtype="float16")
    average_2022 = np.nanmean(y_axis_2022, dtype="float16")
    return


# Monthly card usage history for the past 3 years
def draw_linechart():
    plt.subplot(3, 1, 1)
    plt.title("Monthly card usage history for the past year (unit: 10,000)")
    plt.plot(x_axis, y_axis_2020, marker="o", label="2020")
    plt.plot(x_axis, y_axis_2021, marker="o", label="2021")
    plt.plot(x_axis, y_axis_2022, marker="o", label="2022")
    plt.legend()
    plt.xlabel("Month")
    plt.ylabel("Card usage amount")
    plt.grid(True, axis="y")


# Comparison graph of this month’s consumption amount and the average consumption amount of the past 12 months
def draw_barchart():
    x = ["Amount spent this month", "average 2020", "average 2021", "average 2022"]
    plt.subplot(3, 1, 2)
    plt.title("Comparison graph of this month's consumption amount and the average consumption amount of the past three years (unit: 10,000)")
    plt.bar(x[0], sum_of_consumption_category, label="this month")
    plt.bar(x[1], average_2020, label="2020")
    plt.bar(x[2], average_2021, label="2021")
    plt.bar(x[3], average_2022, label="2022")
    plt.legend()
    plt.xlabel("Consumption amount this month & average consumption amount by year")
    plt.ylabel("Card usage amount")
    plt.grid(True, axis="y", linestyle=":")
    return


# Ratio of this month’s consumption amount by category
def draw_piechart():
    plt.subplot(3, 1, 3)
    plt.title("Ratio of this month’s spending amount by category")
    plt.pie(consumption_thismonth, labels=consumption_category, autopct="%.1f%%")
    plt.legend()
    return


if __name__ == "__main__":
    main()