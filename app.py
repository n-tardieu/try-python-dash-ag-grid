import dash
from dash import html
import dash_ag_grid as dag
import pandas as pd
import colorlover

# Lire les données à partir du fichier JSON
data = pd.read_json("./stintFile.json")

# Convertir les données en DataFrame
df = pd.DataFrame(data)

def discrete_background_color_bins(df, n_bins=5, columns="all"):
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    if columns == "all":
        df_numeric_columns = df.select_dtypes("number")
    else:
        df_numeric_columns = df[columns]
    df_max = df_numeric_columns.max().max()
    df_min = df_numeric_columns.min().min()
    ranges = [((df_max - df_min) * i) + df_min for i in bounds]
    styleConditions = []
    legend = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        if i == len(bounds) - 1:
            max_bound += 1

        backgroundColor = colorlover.scales[str(n_bins)]["seq"]["Blues"][i - 1]
        color = "white" if i > len(bounds) / 2.0 else "inherit"

        styleConditions.append(
            {
                "condition": f"params.value >= {min_bound} && params.value < {max_bound}",
                "style": {"backgroundColor": backgroundColor, "color": color},
            }
        )

        legend.append(
            html.Div(
                [
                    html.Div(
                        style={
                            "backgroundColor": backgroundColor,
                            "borderLeft": "1px rgb(50, 50, 50) solid",
                            "height": "10px",
                        }
                    ),
                    html.Small(round(min_bound, 2), style={"paddingLeft": "2px"}),
                ],
                style={"display": "inline-block", "width": "60px"},
            )
        )

    return styleConditions, html.Div(legend, style={"padding": "5px 0 5px 0"})

# Générer les conditions de style pour la coloration des cellules
n_bins = 5  # Nombre de bins pour la coloration
styleConditions, legend = discrete_background_color_bins(df, n_bins=n_bins, columns=["kpi"])

# Créer l'application Dash
app = dash.Dash(__name__)

# Définir les colonnes avec le style conditionnel pour les dégradés de couleurs
columns = [
    {"headerName": "Ideal", "field": "Ideal"},
    {"headerName": "Average", "field": "Average"},
    {"headerName": "Car Number", "field": "carNumber"},
    {
        "headerName": "KPI",
        "field": "kpi",
        "cellStyle": {"styleConditions": styleConditions},  # Appliquer les styles conditionnels ici
    },
]

# Définir la mise en page de l'application
app.layout = html.Div([
    dag.AgGrid(
        id="grid",
        columnDefs=columns,
        rowData=df.to_dict("records"),
        defaultColDef={"sortable": True, "filter": True, "resizable": True},
        style={'height': '800px', 'width': '100%'},
        dashGridOptions={"animateRows": False}  # Option pour désactiver l'animation des lignes
    ),
    html.Div(legend, style={"padding": "5px 0 5px 0"})  # Afficher la légende
])

# Exécuter l'application
if __name__ == '__main__':
    app.run_server(debug=True)
