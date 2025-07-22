def insertion_sort(list1):
    for i in range(1,len(list1)):
        ce = list1[i]
        p = i
       
        while ce <(list1[p-1]) and p>0:
            list1[p],list1[p-1]=list1[p-1],list1[p]
            p = p-1
            print(list1)
    print(list1)
insertion_sort([3,10,1,5,7])