"""
APPROACH 2
"""
# Imports
from numpy import random
import numpy as np
from numpy.core.fromnumeric import mean
from matplotlib import pyplot as plt
from graphPlotter import plot

# User Defined values
remaining_inventory = 500
working_days = 7
demand_max = 175
demand_min = 50

# Custom Values
OPTIMZER = 500

def demand_generator(demand_min:int, demand_max:int) -> int:
    """
    Generates a random demand
    """
    return (random.randint(demand_min, demand_max))

def optimzer(iterations:int) -> int:

    # Global Variables
    global remaining_inventory
    global working_days
    global demand_max
    global demand_min
    """
    Optimizes the demand vs stock
    Initial Inventory is 500
    """

    # Dict for map LOT to day added
    lot_vs_days = {}
    stocks_left = {}
    while(iterations):
        demands = []
        lot = 0
        lot_day = 0
        flag = 0
        # Enter the day and perform calculations
        for _day in range(working_days):
            # Generate a random demand
            demand = demand_generator(demand_min, demand_max)
            demands.append(demand)

            # If remaining inventory is less than demand
            if remaining_inventory < demand:
                if flag == 0:
                    lot_day = _day+1
                    flag = 1

                remained_days = 5 - _day
                avg_now = mean(demands)

                # Creating a lot using standard deviation
                lot += np.sqrt(pow(remained_days, 2) * pow(avg_now, 2))
                remaining_inventory = remaining_inventory + lot
            else:
                remaining_inventory -= demand

        # Print Iteration
        print("============================")
        print("Iterations:", iterations)
        print("Demands for 6 days:", demands)
        print("Remaining Inventory:", remaining_inventory)
        print("Lot:", lot)
        print("Lot Day:", lot_day)
        print("============================")

        # Dict values will be randomly based selects
        lot_vs_days[lot] = lot_day
        stocks_left[lot] = remaining_inventory

        iterations -= 1

    # Pairing the minimum set
    min_lot = min(stocks_left, key=stocks_left.get)
    min_stock = stocks_left[min_lot]
    min_day = lot_vs_days[min_lot]

    return min_lot, min_stock, min_day, stocks_left


# Plot Graph
def GraphPlot(stocks):
    x = stocks.keys() # lots
    y = stocks.values() # amount of remaining stocks
    plot(x, y)

# Driver code
def main(degree:int):
    lot, stock_left, day, stocks_graph = optimzer(degree)
    print("\n----------------------\nPrediction of based upon random selection is:\n")
    print(lot, " lot to be added on ", day, " to get minimum stock left of ", stock_left)
    print("----------------------\n")
    print("ctrl+c to exit...")
    GraphPlot(stocks_graph)


main(OPTIMZER)


"""
Here What User will enter:
-> Initial Inventory
-> Working Days
-> demand_max, min

Our Values:
-> Optimizer
"""
