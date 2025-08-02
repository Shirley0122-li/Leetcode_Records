def d_apart(numbers: list[int], difference: int) -> list[tuple[int, int]]: 
    # no repeating in numbers
    # numbers.sort()
    # l = 0
    # res = []
    # for r in range(1, len(numbers)):
    #     temp_dif = numbers[r] - numbers[l]
    #     if temp_dif == difference:
    #         res.append((numbers[l], numbers[r]))
    #         l += 1
    #     elif temp_dif > difference:
    #         l += 1
    
    # return res

    dic = {}
    res = []
    for n in numbers:
        if n in dic:
            res.append((n, dic[n]))
        else:
            dic[n+difference] = n
            dic[n-difference] = n
    
    return res



# d_apart([3, 5, 7], 2) -> [(3, 5), (5, 7)]