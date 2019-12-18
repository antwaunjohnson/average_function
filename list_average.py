from functools import reduce

# Personal Solution (Getting the average from a python list)
def list_average(list):
    average = sum(list) / len(list)
    print(average)

list = [3,234,56,223,56,21,334,6,1,0]

list_average(list)


# Instructor Solution (Getting the average from a python list)

def get_average(num_list):
    total = reduce((lambda total, element: total + element),num_list)

    return total / len(num_list)


num_list = [1,2,3,4,5,6]

print(get_average(num_list))


