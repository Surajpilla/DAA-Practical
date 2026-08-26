#linear search
a = list(map(int, input("Enter numbers: ").split()))
tar = int(input("Enter target number: "))

for i in range(len(a)):
    if a[i] == tar:
        print("Found at index:", i)
        break
else:
    print("Target not found")

low = 0
high = len(a) - 1

while low <= high:
    mid = (low + high) // 2

    if a[mid] == tar:
        print("Found at index:", mid)
        break

    elif a[mid] < tar:
        low = mid + 1

    else:
        high = mid - 1

else:
    print("Target not found")

