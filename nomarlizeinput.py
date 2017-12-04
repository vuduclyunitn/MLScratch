

dataset = [[1, 2, 3, 4], [1,100, 3, 3], [10, 12, 0, 4]]

def getMinMax(dataset):
    minmax = []
    for col in range(len(dataset[0])):
        temp = []
        for row in range(len(dataset)):
            temp.append(dataset[row][col])
        minmax.append((min(temp), max(temp)))
    return minmax

mm = getMinMax(dataset)
print(mm)
