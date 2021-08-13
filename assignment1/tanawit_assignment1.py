# Name:
# ID:
# Assignment 1 : Read, write and, plot
# ====================================
import csv
from matplotlib import pyplot as plt
import math

csvfile = open('data.csv','r')
outputfile = open('output.csv', 'w')
header = ["point (i)","x","y","distance"]
data = csv.reader(csvfile)
output = csv.writer(outputfile)
init = [0,0]
data_list = list()
plot_x = list()
plot_y = list()
next(data,None)
#print(type(data))
total = 0
output.writerow(header)
header[0] = "point"
print(*header)
for row in data:
    dist = math.sqrt(math.pow(float(row[1]) - init[0],2) + math.pow(float(row[2]) - init[1],2))
    init = [int(row[1]) ,int(row[2])]
    total += dist
    output_row = [int(row[0]), int(row[1]), int(row[2]), round(dist,2)]
    plot_x.append(output_row[1])
    plot_y.append(output_row[2])
    output.writerow(output_row)
    print(*output_row)
    #print(row)
print('Total = '+str(total))
csvfile.close()
outputfile.close()
plt.plot(plot_x, plot_y)
plt.show()
