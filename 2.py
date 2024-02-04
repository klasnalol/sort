try:
    n = int(input("size of the array: "))
    if n <= 0:
        print("should be >0")
    else:
        elements = list(map(int, input("Enter the elements ").split()))

        if len(elements) != n:
            print("TOO much arr")
        else:
            # Insertion sort
            for i in range(1, len(elements)):
                key = elements[i]
                j = i - 1
                while j >= 0 and key < elements[j]:
                    elements[j + 1] = elements[j]
                    j -= 1
                elements[j + 1] = key

            print("Sorted array:", end=" ")
            for num in elements:
                print(num, end=" ")

except ValueError:
    print("NE 4eslo")