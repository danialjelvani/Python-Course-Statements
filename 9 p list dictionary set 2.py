
# 2 ta for kenare ham nested
l1 = [i for i in range(1, 100) for x in range(2, 10) if i % x == 0]
print(set(l1))


# list filtering:
z = [2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9]

# enumerate indexo value ro joda mikone va az
# z.index(3) behtare chon agar chanta 3 dashte
# bashim indexe avalin 3 ro barmigardune

filtered_list = [x for i, x in enumerate(z) if i not in [0, 2]]
filtered_list2 = [x for x in z if z.index(x) not in [0, 2]]
# baraye balayi indexe 3 mosavi 1 e b hamin khate hichkudum hazf nashodn
print(filtered_list)
print(filtered_list2)
