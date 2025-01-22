
l1 = {
    'danial': 20,
    'mahsa': 14,
    'romina': 18,
    'alireza': 15,
}

below_16 = [k.upper() for k, v in l1.items() if v < 16]

print(below_16)

# remove floats:

original_list = [2, 2.25, 3, 3.8]

int_list = [x for x in original_list if type(x) == int]
# or x % 1 = 0
print(int_list)
