def num_ways_with_1_2_to_get(n):
    prev = ''
    if n < 2:
        return 1
    print_helper(m - 2, f"{ค่า prev ที่ format เรียบร้อยแล้ว}2")
    return num_ways_with_1_2_to_get(n - 1) + num_ways_with_1_2_to_get(n - 2)

def print_with_prev(n, prev):
    if n == 0:
       print(prev)
    elif n == 0:
       print(prev + 1)
    else:
       print_with_prev(n - 1, 0)

print(num_ways_with_1_2_to_get(5))
