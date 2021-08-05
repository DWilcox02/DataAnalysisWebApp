import justpy as jp
import pandas
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")

df = data.groupby(["Month", "Course Name"])["Rating"].count().unstack()

chartDef = """
{
    chart: {
        type: 'areaspline'
    },
    title: {
        text: 'Average fruit consumption during one week'
    },
    legend: {
        layout: 'vertical',
        align: 'bottom',
        verticalAlign: 'bottom',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 4.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Fruit units'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' units'
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
}
"""
## Create quasar page
def app(): #returns quasar page
    wp = jp.QuasarPage()
    #Add elements
    #Classes add style, spaces in between each
    #Respect the order that elements are added it goes top to bottom
    h1 = jp.QDiv(a = wp, text = "Analysis of course reviews", classes = "text-h3 text-center q-pa-md") 
    #Quasar division (from HTML)
    p1 = jp.QDiv(a = wp, text = "These grpahs represent course review analysis")
    hc = jp.HighCharts(a = wp, options= chartDef)
    hc.options.xAxis.categories = list(df.index)
    #Series is a list of dictionaries (represents line)
    #Dicts contain name and data
    #Data is another list

    #Use loops (this time nested in the lists)
    hcData = [{"name":v1, "data":[v2 for v2 in df[v1]]} for v1 in df.columns] 
    hc.options.series = hcData

    return wp

jp.justpy(app)
# Control C to stop the process