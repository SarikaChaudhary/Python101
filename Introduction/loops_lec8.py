


def loops():
    a = [1,2,3,4]
    for i in a:
        print(i, end= " ")

    print()
    n = 4
    for i in range(0, n):
        print(i, end= " ")
    # 0 1 2 3

    # Print a dictionary
    d = dict({'x': 123, 'y': 354})
    for x in d:
        print("%s  %d" % (x, d[x]))

    # Index iteration
    arr = [1,2,3,4,5,6]
    for idx in range(len(arr)):     # range expects an integer
        print(arr[idx], end=" ")

    ## While loop
    end = 3
    start = 0
    while start < end:
        print(arr[start], end=" ")
        start += 1

    # Infinite loop
    # while(True):
    #     print("hellloo.. ")

    for i in range(1, 5):
        for j in range(i):
            print(j, end=" ")

    # Continue statement
    for letter in 'SayHiToPython':
        if letter == 'e' or letter == 's':
            continue
        print('Current Letter :', letter)

    # Break statement
    for letter in 'SayHiToPython':
        if letter == 'e' or letter == 's':
            break
        print('Current Letter :', letter)

    # Pass statement
    for letter in 'kuchbhi random':
        pass
    print('Last Letter :', letter)

if __name__ == '__main__':
    loops()