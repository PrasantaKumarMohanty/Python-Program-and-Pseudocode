def arr(lis):
    lis.sort()
    print(lis)
    min_num=min(lis)
    resultlist=[]
    resultlist.append(min_num)
    for i in lis:
        print(min_num)
        if i==min_num:
            min_num+=1
            pass
        else:
            max_num=i
            print(max_num)
            break

    resultlist.append(max_num)
    print(resultlist)

if __name__ == '__main__':
    lis=[1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6]
    arr(lis)