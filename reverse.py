def reversed_list(x):
    new_list=[]
    x=x[::-1]
    for i in x:
        if type(i) is list:
            i=i[::-1]
            new_list.append(i)
    return new_list
x=[[1, 2], [3, 4], [5, 6, 7]]
reversed_list(x)
