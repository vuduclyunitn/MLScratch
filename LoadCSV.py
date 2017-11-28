from csv import reader
def load_csv(filename):
    dataset = list()
    csvfile = open(filename, "r")
    lines = reader(csvfile)
    for line in lines:
        if not line:
            continue
        else:
            dataset.append(line)
    return dataset

'''
Convert items of dataset to float
'''
def string_column_to_float(dataset, column):
    row = []
    for i in dataset[column]:
        try:
            float(i)
        except ValueError:
            i = 'nan'
        row.append(float(i.strip()))
    return row

#filename = "pima-indians-diabetes.csv"
#dataset = load_csv(filename)
#print((dataset)[0])
#print(string_column_to_float(dataset, 0))
#
#print("Load dataset {0} with {1} rows and {2} columns".format(filename, len(dataset), len(dataset[0])))
#convertedData = []
#for i, r in enumerate(dataset):
#    convertedData.append(string_column_to_float(dataset, i))
#
#print("Converted: {}".format(convertedData[0]))
#print(len(dataset) == len(dataset[0]))
#
#print("Load dataset {0} with {1} rows and {2} columns".format(filename, len(convertedData), len(convertedData[0])))
#

# Iris : converting predicted values in strings to numeric
irisfile = "iris.csv"
def load_iris(filename):
    with open(filename, "r") as f:
        lines = reader(f)
        for line in lines:
            if len(line)
load_iris(irisfile)
#irisdataset = load_csv(irisfile)
#print(irisdataset[0])
#
## get distinct class values
#y = set()
#for d in irisdataset:
#    y.add(d[-1])
#
#print("Number of distinct classes: {}".format(y))
#
## assign class values 
#'''
#Iris-setosa : 0
#Iris-versicolor : 1
#Iris-virginica: 2
#'''
#for d in irisdataset:
#    if d[-1] == "Iris-setosa":
#        d[-1] = 0
#    elif d[-1] == "Iris-versicolor":
#        d[-1] = 1
#    else:
#        d[-1] = 2
#
#for d in irisdataset:
#    print(d[-1])
#

