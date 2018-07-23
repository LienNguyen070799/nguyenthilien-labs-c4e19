def remove_dollar_sign(s) :
    l = list(s)
    for i in range(len(l)) :
        if '$' in l:
            p = l.index("$")
            del(l[p])
    s = "".join(l)
    print(s)
    return s
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
# print(string_with_no_dollars)
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")

