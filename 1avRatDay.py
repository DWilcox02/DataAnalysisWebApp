import justpy as jp
import pandas
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc
data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])

data['Weekday'] = data['Timestamp'].dt.strftime("%A")
data['Daynum'] = data['Timestamp'].dt.strftime("%w")

df = data.groupby(['Weekday', 'Daynum']).mean()
df = df.sort_values('Daynum')
x = df.index.get_level_values(0)
y = df['Rating']


#Functions as a dictionary and you can access and alter the keys with code
chartDef = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Atmosphere Temperature by Altitude'
    },
    subtitle: {
        text: 'According to the Standard Atmosphere Model'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Altitude'
        },
        labels: {
            format: '{value} km'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Temperature'
        },
        labels: {
            format: '{value}°'
        },
        accessibility: {
            rangeDescription: 'Range: 3 to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{point.x}, {point.y}'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Temperature',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""

def changeLabels(hc): # Function to change the titles and labels
    hc.options.xAxis.title.text = "Day of Week"
    hc.options.xAxis.labels.format = "{value}"
    hc.options.yAxis.title.text = "Avg Rating"
    hc.options.title.text = "Average Rating by Day"
    hc.options.series[0].name = "Rating"


## Create quasar page
def app(): #returns quasar page
    wp = jp.QuasarPage()
    #Add elements
    #Classes add style, spaces in between each
    #Respect the order that elements are added it goes top to bottom
    h1 = jp.QDiv(a = wp, text = "Analysis of course reviews", classes = "text-h3 text-center q-pa-md") 
    #Quasar division (from HTML)
    p1 = jp.QDiv(a = wp, text = "These grpahs represent course review analysis")
    #Adding highcharts graph, justpy combines them together
    hc = jp.HighCharts(a = wp, options = chartDef)

    #Changing data
    hc.options.xAxis.categories = list(df.index)
    hc.options.series[0].data = list(y)

    changeLabels(hc)

    # must convert Dataframe format into Highcharts series
    # Use zip function
    # Using hc.options... you can access the keys to the dictionary
    return wp

jp.justpy(app)
# Control C to stop the process