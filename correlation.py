import csv
import plotly.express as px
import pandas as pd

with open("./corr.csv") as csv_file:
    df = csv.DictReader(csv_file)
    fig = px.scatter(df, x = "Temperature", y = "Ice-cream Sales")
    fig.show()