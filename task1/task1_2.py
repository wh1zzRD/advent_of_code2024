def main():
    list1 = []
    list2 = []

    with open("task1_input.txt", "r") as file:
        for line in file:
            num1, num2 = map(int, line.split())
            list1.append(num1)
            list2.append(num2)

    print(list1)
    print(list2)

    max1 = max2 = 0
    for i in range(len(list1)):
        if list1[i] > max1:
            max1 = list1[i]
        if list2[i] > max2:
            max2 = list2[i]

    cnt1 = [0] * (max1 + 1)
    cnt2 = [0] * (max2 + 1)

    for i in range(len(list1)):
        cnt1[list1[i]] += 1
        cnt2[list2[i]] += 1

    print(cnt1)
    print(cnt2)

    result = 0
    for i in range(len(list1)):
        result += list1[i] * cnt2[list1[i]]

    print(result)


if __name__ == '__main__':
    main()
