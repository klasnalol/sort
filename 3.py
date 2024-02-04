try:
    n = int(input("size of the array: "))
    if n <= 0:
        print("should be >0")
    else:
        elements = list(map(int, input("Enter the elements ").split()))

        if len(elements) != n:
            print("TOO much arr")
        else:
            # Merge sort
            def merge_sort(arr):
                if len(arr) > 1:
                    mid = len(arr) // 2
                    left_half = arr[:mid]
                    right_half = arr[mid:]

                    merge_sort(left_half)
                    merge_sort(right_half)

                    i = j = k = 0

                    while i < len(left_half) and j < len(right_half):
                        if left_half[i] < right_half[j]:
                            arr[k] = left_half[i]
                            i += 1
                        else:
                            arr[k] = right_half[j]
                            j += 1
                        k += 1

                    while i < len(left_half):
                        arr[k] = left_half[i]
                        i += 1
                        k += 1

                    while j < len(right_half):
                        arr[k] = right_half[j]
                        j += 1
                        k += 1


            merge_sort(elements)

            print("Sorted array:", end=" ")
            for num in elements:
                print(num, end=" ")

except ValueError:
    print("NE 4eslo")