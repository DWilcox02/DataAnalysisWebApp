import justpy as jp
import justpy as jp
import pandas
import matplotlib.pyplot as plt
from datetime import datetime
from pytz import utc

data = pandas.read_csv("reviews.csv", parse_dates=['Timestamp'])
data["Month"] = data["Timestamp"].dt.strftime("%Y-%m")
df = data.groupby(["Course Name"])["Rating"].count()

chartDef = """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
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
    hc = jp.HighCharts(a = wp, options = chartDef)
    hcData = [{"name": v1, "y": v2} for v1, v2 in zip(df.index, df)]
    hc.options.series[0].data = hcData
    return wp

jp.justpy(app)


# Control C to stop the process