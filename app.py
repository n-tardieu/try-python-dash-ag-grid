import dash
from dash import html
from dash_ag_grid import AgGrid
import pandas as pd
from utils.styleCondition import discrete_background_color_bins, create_car_style, discrete_background_color, discrete_background_color_red_by_blue, discrete_background_color_last_row


# Create the DataFrame
data = {
    "CarNumber": ["#36", "#38", "#50", "#51", "#63", "#83", "#93", "#94", "#99"],
    "FCY Pace (km/h)": [80.0] * 9,
    "FCY Time (s)": [77.7, 53.9, 64.6, 70.1, 107.3, 111.4, 106.7, 106.7, 77.6],
    "Distance (km)": [1.727, 1.198, 1.437, 1.558, 2.386, 2.476, 2.372, 2.371, 1.725],
    "Green Time (s)": [32.1, 27.3, 24.2, 34.3, 43.4, 50.4, 43.4, 43.4, 32.1],
    "Green Pace (km/h)": [193.5, 157.9, 213.9, 163.8, 197.7, 177.0, 196.5, 196.5, 193.2],
    "Time Lost (s/km)": [26.4, 22.2, 28.2, 23.0, 26.8, 24.7, 26.7, 26.7, 26.4],
    "FCY Duration (s)": [120.0] * 9,
    "FCY Distance (km)": [2.667] * 9,
    "FCY Time Loss (s)": [70.4, 59.2, 75.1, 61.4, 71.4, 65.8, 71.2, 71.1, 70.3],
    "FCY Delta (s) (extrapolated)": [11.2, 0.0, 15.9, 2.2, 12.2, 6.6, 12.0, 11.9, 11.1]
}

df = pd.DataFrame(data)
unique_car_numbers = df['CarNumber'].unique()

df = df.set_index("CarNumber").T.reset_index().rename(columns={"index": "Label"})
styleConditions = discrete_background_color_last_row(df)

# Define columns for AgGrid
column_defs = [{"headerName": "On the FCY", "children": [
        {"headerName": "Sector", "field": "Label"}
]}]

for car_number in unique_car_numbers:
    column_defs.append({
        "headerName": car_number,
        "children": [
            {"headerName": "IP2-FL", "field": car_number}
        ]
    })
# Initialize the Dash app
app = dash.Dash(__name__)

app.layout = html.Div([
    AgGrid(
        id='ag-grid',
        columnDefs=column_defs,
        rowData=df.to_dict('records'),
        defaultColDef={"sortable": False, "filter": False, "resizable": True, "flex": 1, "cellStyle": {"styleConditions": styleConditions}},
        style={'height': '900px', 'width': '100%'}
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
