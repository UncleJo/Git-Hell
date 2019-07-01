if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())


    temp=set(arr)
    res=list(temp)
    res.sort()

    print(res[-2])
