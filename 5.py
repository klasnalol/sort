try:
    n = int(input("size of the array: "))
    if n <= 0:
        print("should be >0")
    else:
        elements = list(map(int, input("Enter the elements ").split()))

        if len(elements) != n:
            print("TOO much arr")
        else:
            # Maximum selection sort
            for i in range(n - 1, 0, -1):
                max_index = i
                for j in range(i):
                    if elements[j] > elements[max_index]:
                        max_index = j

                elements[i], elements[max_index] = elements[max_index], elements[i]

            print("Sorted array:", end=" ")
            for num in elements:
                print(num, end=" ")

except ValueError:
    print("NE 4eslo")