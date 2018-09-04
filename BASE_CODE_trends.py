import setup
import csv
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


f = open('fakenews.csv', newline='')
read = csv.reader(f, delimiter=' ', quotechar='|')

rows = []
for i in read:
    for k in i:
        rows.append(k)
xunf = []
y = []
for i in rows[7:]:
    date,data = i.split(',')
    xunf.append(date)
    y.append(int(data))

x = []
for date in xunf:
    x.append(datetime.strptime(date, "%Y-%m"))
plt.title("FIGURE A: Use of 'Fake News' in America")
plt.plot(x,y)
plt.gcf().autofmt_xdate()
#plt.savefig("A.png")
plt.show()


def derive(y):
    der = []
    for i in range(0,len(y)-1):
        if i != 0 or i != len(y)-1:
            der.append((y[i+1] - y[i-1])/1)
        elif i == 0:
            der.append((y[i+1]-y[i])/1)
        elif i == len(y)-1:
            der.append((y[i]-y[i-1])/1)
    der.append(der[-1])
    return der
plt.title("FIGURE B: Derivative of FIGURE A")
plt.plot(x, derive(y))
plt.gcf().autofmt_xdate()
#plt.savefig("B.png")
plt.show()

def stack(x,y):
    dataset = []
    for i in range(0,len(x)-1):
        dataset.append([x[i], y[i]])
    return dataset
largest = [0,0]
index = 0
counter = 0
dataset = stack(x, derive(y))
for i in dataset:
    if i[1] > largest[1]:
        largest=i
        index = counter
        
    counter += 1
print(largest, index)
print(dataset[index-1], dataset[index+1])
    

