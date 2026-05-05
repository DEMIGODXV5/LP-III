def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        # find minimum element
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# 🔹 Taking input from user
n = int(input("Enter number of elements: "))

arr = []
print("Enter elements:")

for i in range(n):
    val = int(input())
    arr.append(val)

# 🔹 Sorting
sorted_arr = selection_sort(arr)

# 🔹 Output
print("Sorted Array:", sorted_arr)