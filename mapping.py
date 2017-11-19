##This module uses plotly to generate a chloropleth map representing user generated
## indices to the user

import plotly.offline as py
import pandas as pd
import webbrowser

# Read in CSV
df = pd.read_csv('./index.csv')

# Function to actually generate the chloropleth map
def plot(df, str):
    data = [ dict(
            type = 'choropleth', 
            locations = df['Country_Code'],
            z = df[str],
            text = df['Country_Code'],
            colorscale = [[0.0, "rgb(240,240,240)"],[0.01,"rgb(165, 0, 38)"],[0.1,"rgb(215, 48, 39"],[0.2,"rgb(244, 109, 67)"],\
                [0.3,"rgb(253, 174, 97)"],[0.4,"rgb(254, 224, 144)"],[0.5,"rgb(255, 255, 191)"],\
                [0.6,"rgb[224, 243, 248]"],[0.7,"rgb(171, 217, 233"],[0.8,"rgb(116, 173, 209)"],\
                [0.9,"rgb[69, 117, 180]"],[1.0,"rgb[49, 54, 149]"]],
            autocolorscale = False,
            reversescale = True,
            marker = dict(
                line = dict (
                    color = 'rgb(180,180,180)',
                    width = 0.5
                ) ),
            colorbar = dict(
                autotick = False,
                tickprefix = '',
                title = str),
          ) ]

    layout = dict(
        title = str,
        geo = dict(
            showframe = False,
            showcoastlines = False,
            projection = dict(
                type = 'Mercator'
            )
        )
    )
    fig = dict( data=data, layout=layout)
    #auto_open=False required so that browser doesn't open on application launch
    py.plot( fig, validate=False, filename='d3-world-map.html', auto_open=False)
