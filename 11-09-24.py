def sort_tuple_by_second_element(t):
    sorted_list=sorted(t, key=lambda x: x[1])
    return tuple(sorted_list)
example_tuple = ((1,2),(3,1),(5,0))
sorted_tuple = sort_tuple_by_second_element(example_tuple)
print(sorted_tuple)
