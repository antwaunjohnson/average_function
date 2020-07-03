from functools import reduce

# Personal Solution (Getting the average from a python list)
def list_average(list):
    average = sum(list) / len(list)
    print(average)

list = [.9638,.9595,.9432,.9163,.9019,.8917,.8904,.8858,.8715,.8680,.8633,.8586,.8633,.8564,.8505,.8309,.8141]

list_average(list)


# Instructor Solution (Getting the average from a python list)

# def get_average(num_list):
#     total = reduce((lambda total, element: total + element),num_list)

#     return total / len(num_list)


# num_list = [1,2,3,4,5,6]

# print(get_average(num_list))


