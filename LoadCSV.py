from csv import reader

# Code for loading csv
''''
input: csv file path
output: list of list instance.
'''
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
Handle non number value in cell
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

