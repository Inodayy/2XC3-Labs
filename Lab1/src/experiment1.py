from bad_sorts import *

list_length = 10
max_value = 100

# Compare runtimes with random items
r_list = create_random_list(list_length, max_value)

# Compare runtimes with near sorted case/ sorted case
ns_list = create_near_sorted_list(list_length, max_value, 2)
s_list = create_near_sorted_list(list_length, max_value, 0)

# Any other cases?

# Tests
