import dash
from dash import html, dcc
from dash.dependencies import Input, Output, State

import gspread
from google.oauth2.service_account import Credentials


import os
import json

credentials_content = os.getenv("CREDENTIALS_JSON")
credentials_file='credentials2.json'
with open(credentials_file, "w") as f:
    f.write(credentials_content)

# creds_path = os.getenv("api_credentials_path")

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file("credentials2.json", scopes=scopes)
client = gspread.authorize(creds)
sheet_id = "1Xp3jzJsTYeyJ5dE-uqeB0soCpsEFic2FgQvSO4JJ3zk"


# app=dash.Dash(__name__)
# server=app.server

# app.layout = html.Div(
#     [
#         dcc.Input(placeholder='Write name here', id='input-val'),
#         html.Button('submit', id='button-id', n_clicks=0),
#         html.Div(id='output-val')
#     ]
# )


# @app.callback(
#     Output('output-val', 'children'),
#     Input('button-id', 'n_clicks'),
#     State('input-val', 'value')
# )
# def callbk(n_clicks, input_val):
    
#     if n_clicks > 0 and input_val:
                
#         sheet = client.open_by_key(sheet_id).sheet1
#         sheet.append_row([input_val,2])
#         #sheet.update_cell(1, 1, input_val)
        

#         return f'{input_val} has been entered'
#     return ''


# if __name__ == '__main__':
#     app.run_server(debug=True)