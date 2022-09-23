def flatten(x):
    
    for i in x:
        if type(i) is list:
            flatten(i)
        else:
            flat_list.append(i)
       
x =[[1,'a',['cat'],2],[[[3]],'dog'],4,5]
flat_list=[]
flatten(x)
print(flat_list)
