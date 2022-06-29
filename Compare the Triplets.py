def compareTriplets(a, b):
    # Write your code here
    array = []
    a_points = 0
    b_points = 0
    
    for i in range(3):
        if a[i] > b[i]:
            a_points += 1
            
        elif a[i] < b[i]:
            b_points += 1
            
    array.insert(a_points, 0)
    array.insert(b_points, 1)
    
    return array
    print(array)

a = [23, 44, 56]
b = [21, 44, 60]

compareTriplets(a, b)