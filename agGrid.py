import dash
import dash_ag_grid as dag
import pandas as pd

from dash import html
from utils.styleCondition import discrete_background_color_bins, create_car_style, discrete_background_color, discrete_background_color_red_by_blue


data = pd.read_json("./stintFile.json")
df = pd.DataFrame(data)

# Générer les conditions de style pour la coloration des cellules
n_bins = 5  # Nombre de bins pour la coloration
styleConditionKpi = discrete_background_color_bins(df, n_bins=n_bins, columns=["kpi"])
styleConditionAverage = discrete_background_color(df, columns=["Average"])
styleConditionIdeal = discrete_background_color_red_by_blue(df, columns=["Ideal"]) 
styleConditionCarNumber = create_car_style(df, column="carNumber")

app = dash.Dash(__name__)

# Définir les colonnes avec le style conditionnel pour les dégradés de couleurs
columns = [
    {"headerName": "Ideal", "field": "Ideal", "cellStyle": {"styleConditions": styleConditionIdeal}},
    {"headerName": "Average", "field": "Average", "cellStyle": {"styleConditions": styleConditionAverage}},
    {"headerName": "Car Number", "field": "carNumber", "cellStyle": {"styleConditions": styleConditionCarNumber}},
    {
        "headerName": "KPI",
        "field": "kpi",
        "cellStyle": {"styleConditions": styleConditionKpi},  # Appliquer les styles conditionnels ici
    },
]

# Définir la mise en page de l'application
app.layout = html.Div([
    dag.AgGrid(
        id="grid",
        rowData=df.to_dict("records"),
        columnDefs=columns,
        defaultColDef={"sortable": True, "filter": True, "resizable": True, "flex": 1},
        dashGridOptions={"animateRows": False}  # Option pour désactiver l'animation des lignes
    ),
])

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)
