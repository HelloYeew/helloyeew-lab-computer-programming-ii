def num_ways_with_1_2_to_get(n):
    if n < 2:
        return 1
    return num_ways_with_1_2_to_get(n - 1) + num_ways_with_1_2_to_get(n - 2)

def num_ways_with_1_2_3_to_get(n):
    if n < 2:
        return 1
    return num_ways_with_1_2_to_get(n - 1) + num_ways_with_1_2_to_get(n - 2)

def num_ways_with_1_2_3_to_get_helper(m, before):
    if m < 0:
        return 0
    elif before == "":
        before += ""
    else:
        before += "+"
    return num_ways_with_1_2_3_to_get_helper(m-1, f"{before}1") + num_ways_with_1_2_3_to_get_helper(m-2, f"{before}2")




print(num_ways_with_1_2_3_to_get(3))
