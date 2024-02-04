try:
    n = int(input("size of the array: "))
    if n <= 0:
        print("should be >0")
    else:
        elements = list(map(int, input("Enter the elements ").split()))

        if len(elements) != n:
            print("TOO much arr")
        else:
            # Heapify function
            def heapify(arr, n, i):
                largest = i
                left = 2 * i + 1
                right = 2 * i + 2

                if left < n and arr[left] > arr[largest]:
                    largest = left

                if right < n and arr[right] > arr[largest]:
                    largest = right

                if largest != i:
                    arr[i], arr[largest] = arr[largest], arr[i]
                    heapify(arr, n, largest)


            # Heap sort
            for i in range(n // 2 - 1, -1, -1):
                heapify(elements, n, i)

            for i in range(n - 1, 0, -1):
                elements[i], elements[0] = elements[0], elements[i]
                heapify(elements, i, 0)
            print("Sorted array:", end=" ")
            for num in elements:
                print(num, end=" ")

except ValueError:
    print("NE 4eslo")