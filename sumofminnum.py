def sum_three_min_elements(lst):
    
    sorted_list = sorted(lst)
    
    sum_three_min = sum(sorted_list[:3])
    
    return sum_three_min

my_list = [5, 2, 8, 1, 6, 3, 7, 4]
result = sum_three_min_elements(my_list)
print("Sum of three smallest elements:", result)
