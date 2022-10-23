def proc(x):
    for i in x:
        if isinstance(i,list):
            proc(i)
        else:
            empty_list.append(i)


x= [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
empty_list = []
proc(x)
print(empty_list)