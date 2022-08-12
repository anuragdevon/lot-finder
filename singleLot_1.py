#"""
#APPROACH 1
#"""
## Imports
#from collections import defaultdict
#import random
#
## Main vars
#extra_week = 5
#ITERATIONS = 100  # Denotes number of weeks to be analyzed
#INITAL_STOCK_VALUE = 500
#WORKING_DAYS = 6 
#
#
## User functions
#def demand_generator(working_days):
#    """
#    Generates an array of random numbers
#    """
#    array = []
#    n = int(working_days/2)
#    for i in range(0, n):
#        array.append(random.randint(0, 200))
#    return array
#
#
#def data_generator(iterations:int, working_days:int) -> list:
#    """
#    Generates data for previous weeks
#    """
#    # initialize dict with zeros
#    lots = {}
#    lots = defaultdict(int)
#
#    while(iterations-1):
#        # Generates random demand
#        demands = demand_generator(working_days)
#
#        # Half sum
#        n1 = int(working_days/2)
#        # n2 = working_days - n1
#        half_sum_1 = 0
#        for i in range(n1):
#            half_sum_1 += demands[i]
#
#        half_sum_2 = 0
#        for i in range(n1, len(demands)):
#            half_sum_2 += demands[i]
#
#        lot_value_1 = half_sum_1-(500 - half_sum_1)
#        lot_value_2 = half_sum_2-(500 - half_sum_2)
#
#        # Increase the frequency of corresposing lots choosen
#        lots[lot_value_1] += 1
#        lots[lot_value_2] += 1
#
#        iterations -= 1
#
#    return lots
#
#
#def predict(iterations:int):
#    """
#    Predicts the next week's demand
#    """
#    global extra_week
#
#    lots_data = dict(data_generator(iterations, WORKING_DAYS))
#    
#    for week in range(extra_week):
#        INITAL_STOCK_VALUE = 500
#        # Get lot of maximum frequency
#        max_lot_frequency = max(zip(lots_data, lots_data.keys()))[1]
#
#        first_array = demand_generator(WORKING_DAYS)
#        second_array = demand_generator(WORKING_DAYS)
#
#        remained_stock = max_lot_frequency + INITAL_STOCK_VALUE - (sum(first_array) + sum(second_array))
#        # print(remained_stock)
#        # Check if reuqired conditions are met assuming
#        if remained_stock > 0 and remained_stock < 50:
#            lots_data[max_lot_frequency] += 1
#        else:
#            for lot in lots_data:
#                if((lot + INITAL_STOCK_VALUE - (sum(first_array) + sum(second_array)))<50):
#                    lots_data[lot] += 1
#
#        print("Required stock for day", week+ITERATIONS-1, ": ", remained_stock)
#        print("Required lot size for day ", week+ITERATIONS-1, ": ", max_lot_frequency)
#        print("==================================================")    
#
#    
#def main(iterations:int):
#    """
#    Driver Code
#    """
#    predict(iterations)
#        
#main(ITERATIONS)

# Update Code---------------------------------------------------------------------------------------------------
"""
APPROACH 1
"""
# Imports
from collections import defaultdict
import random

# Main vars
extra_week = 10
iterations= 5
ITERATIONS = 100  # Denotes number of weeks to be analyzed
INITAL_STOCK_VALUE = 500
WORKING_DAYS = 6 


# User functions
def demand_generator(working_days):
    """
    Generates an array of random numbers
    """
    array = []
    n = int(working_days)
    for i in range(0, n):
        array.append(random.randint(50, 150))
        print(f"at day {i}:",array)
    return array


def data_generator(working_days:int):
    """
    Generates data for previous weeks
    """
    # initialize dict with zeros
    lots = {}
    lots = defaultdict(int)

    for z in range(5):
        print(f"week {z+1} data collection")
        demands = demand_generator(working_days)
        n1 = int(working_days/2)
            # n2 = working_days - n1
        half_sum_1 = 0
        for i in range(n1):
            half_sum_1 += demands[i]
        print("half sum1:",half_sum_1)

        half_sum_2 = 0
        for i in range(n1,working_days):
            half_sum_2 += demands[i]
        print("half sum2:",half_sum_2)

        lot_value_1 = half_sum_1-(500 - half_sum_1)
        lot_value_2 = half_sum_2-(500 - half_sum_2)

            # Increase the frequency of corresposing lots choosen
        lots[lot_value_1] += 1
        lots[lot_value_2] += 1

        for z in lots:
            print(z,":",lots[z])
        
    return lots


def predict():
    """
    Predicts the next week's demand
    """
    global extra_week

    lots_data = dict(data_generator(WORKING_DAYS))
    print("======================\n=================================================\n============================================")
    
    for week in range(extra_week):
        INITAL_STOCK_VALUE = 500
        # Get lot of maximum frequency
 
        

        print(f"for week {week+6} single level lot")
        print("first half of week")
        first_array = demand_generator(WORKING_DAYS/2)
        max_lot_frequency = max(zip(lots_data, lots_data.keys()))[1]
        print(f"lot value chosen={max_lot_frequency}")
        print("second half of the week")
        second_array = demand_generator(WORKING_DAYS/2)

        remained_stock = max_lot_frequency + INITAL_STOCK_VALUE - (sum(first_array) + sum(second_array))
        # print(remained_stock)
        # Check if reuqired conditions are met assuming
        for lot in lots_data:
            r = lot + INITAL_STOCK_VALUE - (sum(first_array) + sum(second_array))
            if(r<170 and r>0):
                    lots_data[lot] += 1

        print("amount added:", max_lot_frequency)
        print("balance: ", remained_stock)

        for s in lots_data:
            print(s,":",lots_data[s])
        

        print("==================================================")    

    
predict()







