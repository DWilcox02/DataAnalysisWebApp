import justpy as jp

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

    return wp

jp.justpy(app)
# Control C to stop the process