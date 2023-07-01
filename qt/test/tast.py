import copy





while True:
    a = input()


    a
    arr2[0][0] = a
    if a == arr1[1][0]:
        value += 1
        path.append(value)
        arr2[0][1] = arr1[1][1]
        arr2[1][0] = arr1[0][1]
        arr2[1][1] = arr1[0][0]
        arr2[2] = arr1[2]

    elif a == arr1[1][1]:
        value -= 1
        path.append(value)
        arr2[0][1] = arr1[1][0]
        arr2[1][0] = arr1[0][0]
        arr2[1][1] = arr1[0][1]
        arr2[2] = arr1[2]

    elif a == arr1[2][0]:
        value += 4
        path.append(value)
        arr2[0][1] = arr1[2][1]
        arr2[1] = arr1[1]
        arr2[2][0] = arr1[0][1]
        arr2[2][1] = arr1[0][0]

    elif a == arr1[2][1]:
        value -= 4
        path.append(value)
        arr2[0][1] = arr1[2][0]
        arr2[1] = arr1[1]
        arr2[2][0] = arr1[0][0]
        arr2[2][1] = arr1[0][1]

    arr1 = copy.deepcopy(arr2)

    print(arr1)
    print(path)
