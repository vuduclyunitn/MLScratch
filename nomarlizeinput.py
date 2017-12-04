

#dataset = [[1, 2, 3, 4], [1,100, 3, 3], [10, 12, 0, 4]]
dataset = [[50, 30], [20, 90]]
def getMinMax(dataset):
    minmax = []
    for col in range(len(dataset[0])):
        temp = []
        for row in range(len(dataset)):
            temp.append(dataset[row][col])
        minmax.append((min(temp), max(temp)))
    return minmax

def rescale(dataset):
    for col in range(len(dataset[0])):
        (mi, ma ) = getMinMax(dataset)[col]
        print(mi, ma)
        for row in range(len(dataset)):
            scaledValue = (dataset[row][col] - mi) / (ma - mi)
            print("Scaled value: {}".format(scaledValue))

mm = rescale(dataset)
#print(mm)
