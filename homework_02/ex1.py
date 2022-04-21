list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

# Ascendent list

ascendent_list = list.copy()
ascendent_list.sort()
print(f'Ascendent list: {ascendent_list}')

# Descendent list

descendent_list = ascendent_list.copy()
descendent_list.reverse()
print(f'Descendent list: {descendent_list}')

# Even numbers

even_list = ascendent_list[1::2]
print(f'Even list: {even_list}')

# Odd numbers

odd_list = ascendent_list[::2]
print(f'Odd list: {odd_list}')

# Multiples of 3

three_multiples = ascendent_list[2::3]
print(f'Three multiples list: {three_multiples}')

print(f'Initial list: {list}')
