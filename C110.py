import pandas as pd
import plotly.express as px
import plotly.graph_objects as gp 
import csv
import plotly.figure_factory as pf
import random
import statistics

df = pd.read_csv("mediumdata.csv")

data = df["responses"].tolist()

newData=[]

def dataPicker(counter):
    for i in range(0,counter):
        ind = random.randint(0,len(data)-1)
        value = data[ind]
        newData.append(value)
    
    mean = statistics.mean(newData)
    return mean

def meanGraph(meanList):
    data1 = meanList
    mean = statistics.mean(data1)
    graph = pf.create_distplot([data1], ["Average"], show_hist = False)
    graph.add_trace(gp.Scatter(x = [mean, mean], y= [0, 1]))
    graph.show()
    
    
    
def main():
    meanList = []
    counter = int(input("Please Specify the amount of times you want to run this : "))
    for i in range(0, 1000):
        meanSet = dataPicker(counter)
        meanList.append(meanSet)
        print(meanSet)
    meanGraph(meanList)

main()
