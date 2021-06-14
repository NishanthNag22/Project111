import csv
import pandas as pd
import random
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv("Project110/data.csv")
data = df["reading_time"].to_list()

def randomSetOfMean(counter):
    dataset = []
    for i in range(0, counter):
        randomIndex= random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showFig(meanList):
    df = meanList
    mean = statistics.mean(df)
    fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="MEAN"))
    fig.show()

def setup():
    meanList = []
    for i in range(0,1000):
        setOfMeans= randomSetOfMean(100)
        meanList.append(setOfMeans)
    showFig(meanList)
    
    mean = statistics.mean(meanList)
    print("Mean of sampling distribution : ",mean )

setup()

populationMean = statistics.mean(data)
print("population mean : ", populationMean)

def standardDeviation():
    meanList = []
    for i in range(0,1000):
        setOfMeans= randomSetOfMean(100)
        meanList.append(setOfMeans)

    stdDeviation = statistics.stdev(meanList)
    print("Standard deviation of sampling distribution:- ", stdDeviation)

standardDeviation()