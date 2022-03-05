import plotly.express as px
import csv
import numpy as np

def plotFigure(data_path):
    with open(data_path) as f:
        df = csv.DictReader(f)
        fig = px.scatter(df,x="Temperature", y="Ice-cream Sales")
        fig.show()

def getDataSource(data_path):
    ice_cream_sales = []
    temp = []
    with open(data_path) as f:
        csv_reader = csv.DictReader(f)
        for row in csv_reader:
            ice_cream_sales.append(float(row["Ice-cream Sales"]))
            temp.append(float(row["Temperature"]))

    return {"x" : temp, "y": ice_cream_sales}


