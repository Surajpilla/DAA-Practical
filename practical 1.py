a = list(map(int, input("Enter numbers: ").split()))

n = len(a)

for i in range(n):
    min = i

    for j in range(i + 1, n):
        if a[j] < a[min]:
            min = j

    a[i], a[min] = a[min], a[i]

print("Sorted array:", a)

for i in range(1, len(a)):
    key = a[i]
    j = i - 1

    while j >= 0 and a[j] > key:
        a[j + 1] = a[j]
        j -= 1

    a[j + 1] = key

print("Sorted array:", a)

n = len(a)

for i in range(n):
    for j in range(0, n - i - 1):

        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]

print("Sorted array:", a)

