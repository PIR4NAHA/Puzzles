# 3n+1 problem
import csv
filepath = "3n+1_data.csv"


def saveData(values):
    """Saves results of algorithm to a csv file"""
    with open(filepath, mode='w', newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=",")
        writer.writerows(values)


def Algorithm(n: int): 
    n_value = n
    if (n==1):
        n_list = [1, 4, 2, 1]
    elif (n==2):
        n_list = [2, 1, 4, 2, 1]
    elif (n==4):
        n_list = [4, 2, 1]
    else:
        n_list = []
        n_list.append(n_value)
        while (n_value != 1):
            if n_value != 1:
                if n_value % 2 == 1:
                    n_value = (3 * n_value) + 1
                elif n_value % 2 == 0:
                    n_value = n_value / 2
            n_list.append(n_value)
    return n_list


values_for_each_n = []
user_input = int(input("Enter a natural number: "))
for i in range(1, user_input+1):
    values_for_each_n.append(Algorithm(i))
saveData(values_for_each_n)


