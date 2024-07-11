import dash
import dash_ag_grid as dag
import pandas as pd

from dash import html
from utils.styleCondition import discrete_background_color_bins, create_car_style, discrete_background_color, discrete_background_color_red_by_blue, discrete_background_color_last_row


data = pd.read_json("./stintFile.json")
df = pd.DataFrame(data)

# Générer les conditions de style pour la coloration des cellules
n_bins = 5  # Nombre de bins pour la coloration
styleConditions = discrete_background_color_last_row(df)

app = dash.Dash(__name__)

# Définir les colonnes avec le style conditionnel pour les dégradés de couleurs
columns = [
    {"headerName": "Car Number", "field": "carNumber"},
    {"headerName": "Ideal", "field": "Ideal" },
    {"headerName": "Average", "field": "Average"},
    {
        "headerName": "KPI",
        "field": "kpi"
    },
]

# Définir la mise en page de l'application
app.layout = html.Div([
    dag.AgGrid(
        id="grid",
        rowData=df.to_dict("records"),
        columnDefs=columns,
        defaultColDef={"sortable": True, "filter": True, "resizable": True, "flex": 1, "cellStyle": {"styleConditions": styleConditions}},
        dashGridOptions={"animateRows": False}  # Option pour désactiver l'animation des lignes
    ),
])

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)
