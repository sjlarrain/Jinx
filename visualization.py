import pandas as pd
import sqlite3
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load the data from the SQLite database
conn = sqlite3.connect('master_database.db')
df = pd.read_sql_query("SELECT * FROM master_table", conn)
conn.close()

# Initialize the Dash app
app = dash.Dash(__name__)

# Create the layout of the app
app.layout = html.Div([
    html.H1("Database Visualization"),
    html.Div([
        html.Label("Filter by column:"),
        dcc.Dropdown(
            id='column-dropdown',
            options=[{'label': col, 'value': col} for col in df.columns],
            value=df.columns[0]
        ),
        dcc.Input(id='filter-input', type='text', placeholder='Enter filter value'),
        html.Button('Apply Filter', id='filter-button', n_clicks=0)
    ]),
    html.Div(id='table-container')
])

# Callback to update the table based on the filter
@app.callback(
    Output('table-container', 'children'),
    [Input('filter-button', 'n_clicks')],
    [Input('column-dropdown', 'value'), Input('filter-input', 'value')]
)
def update_table(n_clicks, column, value):
    if value:
        filtered_df = df[df[column].astype(str).str.contains(value, case=False, na=False)]
    else:
        filtered_df = df
    return html.Div([
        html.H2(f"Filtered Data (Column: {column}, Value: {value})"),
        dcc.Graph(
            id='table',
            figure={
                'data': [{
                    'type': 'table',
                    'header': {'values': list(filtered_df.columns)},
                    'cells': {'values': [filtered_df[col] for col in filtered_df.columns]}
                }]
            }
        )
    ])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
