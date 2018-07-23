def get_even_list (l) :
    even_number_list = []
    for i in l:
        if i % 2 == 0:
            even_number_list.append(i)
    print(even_number_list)
get_even_list([1,4,6,8,3,11,10,-2,-6,-9])