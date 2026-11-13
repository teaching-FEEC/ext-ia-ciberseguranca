# Import packages
from dash import Dash, html, dcc, callback, clientside_callback, Output, Input
import dash_ag_grid as dag
import pandas as pd
import numpy as np
import plotly.express as px
import dash_bootstrap_components as dbc

def parse_to_array(x):
    return np.array(x.split('|'), dtype='str')

dhead = pd.read_csv('editions/2026.2/projects/a-nova-rua/aplicacao-1/respostas.csv', nrows=1)
keys=dhead.to_dict('records')[0].keys()
converters = {key: parse_to_array for key in keys}

# Incorporate data
df = pd.read_csv('editions/2026.2/projects/a-nova-rua/aplicacao-1/respostas.csv', converters=converters)

correct_answers = {
    'Q1': 'D',
    'Q2': '1',
    'Q3': 'B',
    'Q4': 'C',
}

# 3. Calculate the count of correct answers per column
counts_data = []
for column, correct_value in correct_answers.items():
    if column in df.columns:
        # Count how many rows in this column match the correct value
        selected_df = df.explode(column)
        match_count = (selected_df[column] == correct_value).sum()
        counts_data.append({'Column': column, 'Correct Count': match_count})

# Convert the results into a new DataFrame for plotting
counts_df = pd.DataFrame(counts_data)

# 4. Create the bar chart (acts as a histogram of counts)
fig_cor = px.bar(
    counts_df, 
    x="Column", 
    y="Correct Count",
    title="Respostas Corretas por Questão",
    labels={"Column": "Questão", "Correct Count": "Nº de Respostas Corretas"},
    text="Correct Count" # Displays the exact count on top of the bars
)

# Update layout for better visuals
fig_cor.update_traces(textposition='outside')
fig_cor.update_layout(yaxis=dict(title='Nº de Respostas Corretas', dtick=1)) # dtick=1 forces integer steps

melted_df = df.melt(id_vars=['participante_id'], var_name='Column', value_name='Value')
# Source - https://stackoverflow.com/a/57472354
# Posted by Pygirl, modified by community. See post 'Timeline' for change history
# Retrieved 2026-10-27, License - CC BY-SA 4.0

melted_df = melted_df.explode('Value')

# Initialize the app - incorporate a Dash Bootstrap theme
external_stylesheets = [dbc.themes.CERULEAN]
app = Dash(__name__, external_stylesheets=external_stylesheets, external_scripts=[
        {'src': 'https://cdn.jsdelivr.net/npm/dom-to-image@2.6.0/dist/dom-to-image.min.js'}
    ])

# App layout
app.layout = dbc.Container([
    dbc.Row([
        dbc.Button(
            'Download as image',
            id='download-image'
        ),
    ]),

    dbc.Card([
        dbc.Row([
            html.Div('Dados e Gráficos da 1º realização.', className="text-primary text-center fs-3")
        ]),

        dbc.Row([
            dag.AgGrid(
                id='grid',
                rowData=df.to_dict('records'),
                columnDefs=[{"field": i} for i in df.columns],
                defaultColDef={"filter": True, "maxWidth": 200},
                columnSize="sizeToFit",
                style={"height": "100%", "width": "100%"}
            )
        ], style={"height": 220, "margin": "5px 5px 5px 5px"}),

        dbc.Row([
            dbc.RadioItems(options=[{"label": x, "value": x} for x in keys if x != 'participante_id'],
                        value='lifeExp',
                        inline=True,
                        id='radio-buttons-final')
        ]),

        dbc.Row([
            dbc.Col([
                dcc.Graph(figure={}, id='my-first-graph-final')
            ], width=6),

            dbc.Col([
                dcc.Graph(
                    id='correct-values-chart',
                    figure=fig_cor
                )
            ], width=6),
        ]),
        ],
        body=True,
        id='component-to-save'
    )

], fluid=True)

# Add controls to build the interaction
@callback(
    Output(component_id='my-first-graph-final', component_property='figure'),
    Input(component_id='radio-buttons-final', component_property='value')
)
def update_graph(col_chosen):
    selected_df = melted_df[melted_df["Column"] == col_chosen]
    fig = px.histogram(
        selected_df, 
        x="Column", 
        color="Value", 
        barmode="group",
        title="Respostas da questão:",
        labels={"Column": "Questão", "Value": "Categorias"},
        category_orders={"Value": ["A", "B", "C", "D"]} # Ensures consistent legend/color ordering
    )

    fig.update_layout(yaxis_title="Nº de Respostas")
    return fig

clientside_callback(
    """
    function(n_clicks){
        if(n_clicks > 0){
            domtoimage.toBlob(document.getElementById('component-to-save'))
                .then(function (blob) {
                    window.saveAs(blob, 'download.png');
                }
            );
        }
    }
    """,
    Output('download-image', 'n_clicks'),
    Input('download-image', 'n_clicks')
)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)