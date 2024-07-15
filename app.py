import dash
from dash import html
from dash_ag_grid import AgGrid
import pandas as pd
from utils.styleCondition import discrete_background_color_bins, create_car_style, discrete_background_color, discrete_background_color_red_by_blue, discrete_background_color_last_row


# Create the DataFrame
dataGoal = {
    "carNumber": ["#36", "#38", "#50", "#51", "#63", "#83", "#93", "#94", "#99"],
    "section": ["IP2-IP1"] * 9,
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

data = [{'carNumber': '2', 'section': 'PL3-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 84.5, 'distance (km)': 1.878, 'greenTime (s)': 29.8, 'greenSpeed (kph)': 226.6, 'timeLost (s)': 29.1, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 97.2, 'fcyDelta (s)': 17.3}, {'carNumber': '5', 'section': 'PL3-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 82.5, 'distance (km)': 1.833, 'greenTime (s)': 29.8, 'greenSpeed (kph)': 221.2, 'timeLost (s)': 28.7, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 95.9, 'fcyDelta (s)': 16.0}, {'carNumber': '6', 'section': 'PL3-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 83.1, 'distance (km)': 1.846, 'greenTime (s)': 29.8, 'greenSpeed (kph)': 222.8, 'timeLost (s)': 28.8, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 96.3, 'fcyDelta (s)': 16.4}, {'carNumber': '7', 'section': 'PL3-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 82.6, 'distance (km)': 1.836, 'greenTime (s)': 29.8, 'greenSpeed (kph)': 221.6, 'timeLost (s)': 28.8, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 96.0, 'fcyDelta (s)': 16.1}, {'carNumber': '8', 'section': 'PL3-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 82.6, 'distance (km)': 1.836, 'greenTime (s)': 29.8, 'greenSpeed (kph)': 221.5, 'timeLost (s)': 28.7, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 96.0, 'fcyDelta (s)': 16.1}, {'carNumber': '11', 'section': 'PL2-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 147.3, 'distance (km)': 3.274, 'greenTime (s)': 65.7, 'greenSpeed (kph)': 179.4, 'timeLost (s)': 24.9, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 83.2, 'fcyDelta (s)': 3.3}, {'carNumber': '12', 'section': 'PL3-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 83.0, 'distance (km)': 1.844, 'greenTime (s)': 29.8, 'greenSpeed (kph)': 222.5, 'timeLost (s)': 28.8, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 96.2, 'fcyDelta (s)': 16.3}, {'carNumber': '15', 'section': 'PL2-SCL2', 'fcySpeed (kph)': 80, 'fcyTime (s)': 136.1, 'distance (km)': 3.024, 'greenTime (s)': 63.1, 'greenSpeed (kph)': 172.6, 'timeLost (s)': 24.1, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 80.6, 'fcyDelta (s)': 0.7}, {'carNumber': '20', 'section': 'IP2-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 106.3, 'distance (km)': 2.362, 'greenTime (s)': 41.5, 'greenSpeed (kph)': 205.0, 'timeLost (s)': 27.4, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 91.6, 'fcyDelta (s)': 11.7}, {'carNumber': '35', 'section': 'PL2-VMAX2', 'fcySpeed (kph)': 80, 'fcyTime (s)': 100.4, 'distance (km)': 2.231, 'greenTime (s)': 47.0, 'greenSpeed (kph)': 170.9, 'timeLost (s)': 23.9, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 79.9, 'fcyDelta (s)': 0.0}, {'carNumber': '36', 'section': 'IP2-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 106.2, 'distance (km)': 2.361, 'greenTime (s)': 41.5, 'greenSpeed (kph)': 204.9, 'timeLost (s)': 27.4, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 91.6, 'fcyDelta (s)': 11.7}, {'carNumber': '38', 'section': 'IP2-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 106.5, 'distance (km)': 2.367, 'greenTime (s)': 41.5, 'greenSpeed (kph)': 205.4, 'timeLost (s)': 27.5, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 91.7, 'fcyDelta (s)': 11.8}, {'carNumber': '50', 'section': 'IP2-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 107.7, 'distance (km)': 2.393, 'greenTime (s)': 41.5, 'greenSpeed (kph)': 207.7, 'timeLost (s)': 27.7, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 92.4, 'fcyDelta (s)': 12.5}, {'carNumber': '51', 'section': 'PL3-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 83.7, 'distance (km)': 1.86, 'greenTime (s)': 29.8, 'greenSpeed (kph)': 224.5, 'timeLost (s)': 29.0, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 96.7, 'fcyDelta (s)': 16.8}, {'carNumber': '63', 'section': 'PL2-SCL2', 'fcySpeed (kph)': 80, 'fcyTime (s)': 136.6, 'distance (km)': 3.036, 'greenTime (s)': 63.1, 'greenSpeed (kph)': 173.3, 'timeLost (s)': 24.2, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 80.9, 'fcyDelta (s)': 1.0}, {'carNumber': '83', 'section': 'IP2-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 106.2, 'distance (km)': 2.36, 'greenTime (s)': 41.5, 'greenSpeed (kph)': 204.8, 'timeLost (s)': 27.4, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 91.6, 'fcyDelta (s)': 11.7}, {'carNumber': '93', 'section': 'PL2-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 146.0, 'distance (km)': 3.245, 'greenTime (s)': 65.7, 'greenSpeed (kph)': 177.8, 'timeLost (s)': 24.8, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 82.6, 'fcyDelta (s)': 2.7}, {'carNumber': '94', 'section': 'PL2-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 145.4, 'distance (km)': 3.232, 'greenTime (s)': 65.7, 'greenSpeed (kph)': 177.1, 'timeLost (s)': 24.7, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 82.4, 'fcyDelta (s)': 2.5}, {'carNumber': '99', 'section': 'IP2-IP1', 'fcySpeed (kph)': 80, 'fcyTime (s)': 106.4, 'distance (km)': 2.365, 'greenTime (s)': 41.5, 'greenSpeed (kph)': 205.2, 'timeLost (s)': 27.5, 'fcyDuration (s)': 150.3, 'fcyDistance (km)': 3.339, 'fcyTimeLoss (s)': 91.7, 'fcyDelta (s)': 11.8}]
keys = data[0].keys()

dataFormatted = {}
for key in keys:
    if key == "section":
        continue
    dataFormatted[key] = [d[key] for d in data]

df = pd.DataFrame(dataFormatted)
# df = pd.DataFrame(dataGoal)
unique_car_numbers = df['carNumber'].unique()

df = df.set_index("carNumber").T.reset_index().rename(columns={"index": "Label"})
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
