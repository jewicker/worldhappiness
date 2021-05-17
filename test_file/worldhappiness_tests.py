import pandas as pd
import dash
import dash_core_components as dcc 
import dash_html_components as html 
from dash.dependencies import Input, Output

import plotly
import plotly.express as px

# This program uses Dash and interactively plots world happiness scores from
# many countries and regions as a function of per capita GDP. 

def produce_df():

# The datasets were downloaded from Kaggle.com during the week of May 1, 2021
# This program was developed in using Python 3.8 during May 1-16, 2021

#--------------------------------------------------------------------------------
# This function reads the data and preprocesses the data in order to
# yield the final DataFrame in the form that is useful to the program.
# The datafiles should be stored in a directory below the root named datafiles.

    df1 = pd.read_csv('datafiles/2015.csv')
    df1 = df1[['Country','Economy (GDP per Capita)','Happiness Score']]
    df1.insert(3, 'year', '2015')

    df2 = pd.read_csv('datafiles/2016.csv')
    df2 = df2[['Country','Economy (GDP per Capita)','Happiness Score']]
    df2.insert(3, 'year', '2016')

    df3 = pd.read_csv('datafiles/2017.csv')
    df3 = df3[['Country','Economy..GDP.per.Capita.','Happiness.Score']]
    df3.rename(columns = {'Economy..GDP.per.Capita.':'Economy (GDP per Capita)'}, inplace = True)
    df3.rename(columns = {'Happiness.Score':'Happiness Score'}, inplace = True)
    df3.insert(3, 'year', '2017')

    df4 = pd.read_csv('datafiles/2018.csv')
    df4 = df4[['Country or region','GDP per capita','Score']]
    df4.rename(columns = {'Country or region':'Country'}, inplace = True)
    df4.rename(columns = {'GDP per capita':'Economy (GDP per Capita)'}, inplace = True)
    df4.rename(columns = {'Score':'Happiness Score'}, inplace = True)
    df4.insert(3, 'year', '2018')

    df5 = pd.read_csv('datafiles/2019.csv')
    df5 = df5[['Country or region','GDP per capita','Score']]
    df5.rename(columns = {'Score':'Happiness Score'}, inplace = True)
    df5.rename(columns = {'GDP per capita':'Economy (GDP per Capita)'}, inplace = True)
    df5.rename(columns = {'Country or region':'Country'}, inplace = True)
    df5.insert(3, 'year', '2019')

    df6 = pd.read_csv('datafiles/2020.csv')
    df6 = df6[['Country name','Logged GDP per capita','Ladder score']]
    df6.rename(columns = {'Ladder score':'Happiness Score'}, inplace = True)
    df6.rename(columns = {'Country name':'Country'}, inplace = True)
    df6.rename(columns = {'Logged GDP per capita':'Economy (GDP per Capita)'}, inplace = True)
    df6.insert(3, 'year', '2020')

    df7 = pd.read_csv('datafiles/2021.csv')
    df7 = df7[['Country name','Logged GDP per capita','Ladder score']]
    df7.rename(columns = {'Ladder score':'Happiness Score'}, inplace = True)
    df7.rename(columns = {'Country name':'Country'}, inplace = True)
    df7.rename(columns = {'Logged GDP per capita':'Economy (GDP per Capita)'}, inplace = True)
    df7.insert(3, 'year', '2021')

    df = pd.concat([df1, df2, df3, df4, df5, df6, df7], axis=0)
    df.rename(columns = {'Country':'Country or Region'}, inplace = True)
    df['year'] = df['year'].astype(int)

    return df


#--------------------------------------------------------------------------------

# This reads the data and produces the DataFrame df

df = produce_df()

print(df.head)
print(df.shape)

#--------------------------------------------------------------------------------
# The DataFrame that is finally passed into the program is called df.
# All other dataframes are deleted in order to save memory.
#--------------------------------------------------------------------------------
# These mark_values define the year values in the slider

mark_values = {2015:'2015',2016:'2016',2017:'2017',2018:'2018',2019:'2019',2020:'2020',2021:'2021'}

app = dash.Dash(__name__)

#--------------------------------------------------------------------------------
# This section defines the layout of the web app

app.layout = html.Div([
    html.Div([
        html.Pre(children= "World Happiness 2015-2021",
        style={"text-align": "center", "font-size": "200%", "color":"black"})
    ]),

    html.Div([
        dcc.Graph(id='the_graph')
    ]),

    html.Div([
        dcc.Slider(id='the_year',
            min=2015,
            max=2021,
            value=2015,
            marks=mark_values,
            step=1)]),
            
    html.Div([
        html.H1('This plot features data from the World Happiness Report'),
        html.Div([
        html.P('You can change the year by moving the slider.'),
        html.P('Hovering your mouse over a data point displays values for a country or region.')
        ])
    ])
])

#--------------------------------------------------------------------------------
# This section defines the control loop of the web app

@app.callback(
    Output('the_graph','figure'),
    [Input('the_year','value')]
)

def update_graph(year_chosen):

    dff=df[(df['year']==year_chosen)]

    scatterplot = px.scatter(
        data_frame=dff,
        x="Economy (GDP per Capita)",
        y="Happiness Score",
        hover_data=['Country or Region'],
        height=550
    )

    scatterplot.update_traces(textposition='top center')

    return (scatterplot)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=False, port=8050)
