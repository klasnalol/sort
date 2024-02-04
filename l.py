try:
    n = int(input("size of the array: "))
    if n <= 0:
        print("should be >0")
    else:
        elements = list(map(int, input("Enter the elements ").split()))

        if len(elements) != n:
            print("TOO much arr")
        else:
            # Quick sort
            for i in range(len(elements)):
                for j in range(i + 1, len(elements)):
                    if elements[j] < elements[i]:
                        elements[i], elements[j] = elements[j], elements[i]

            print("Sorted array:", end=" ")
            for num in elements:
                print(num, end=" ")

except ValueError:
    print("NE 4eslo")
