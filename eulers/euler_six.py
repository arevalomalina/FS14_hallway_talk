#find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum of the first one hundred natural numbers.

def sum_square_difference():
    number_list = []
    square_list = []
    for i in range (1, 101):
        number_list.append(i)
        
    square_of_sum = sum(number_list) * sum(number_list)
    
    for i in number_list:
        square_list.append(i*i)
    
    sum_of_square = sum(square_list)
    
    print square_of_sum - sum_of_square

sum_square_difference()