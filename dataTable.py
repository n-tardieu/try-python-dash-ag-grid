import pandas as pd

from dash import Dash, dash_table, html
from collections import OrderedDict
from utils.styleCondition import discrete_background_color_bins_for_datagrid

data = pd.read_json("./stintFile.json")
df = pd.DataFrame(data)

# Générer les conditions de style pour la coloration des cellules
n_bins = 5  # Nombre de bins pour la coloration

all_columns_styles = []
all_columns_styles.extend(discrete_background_color_bins_for_datagrid(df, n_bins=n_bins, columns=["kpi"]))
all_columns_styles.extend(discrete_background_color_bins_for_datagrid(df, n_bins=n_bins, columns=["carNumber"]))

app = Dash(__name__)

app.layout = html.Div([
    dash_table.DataTable(
        data=df.to_dict('records'),
        sort_action='native',
        columns=[{'name': i, 'id': i} for i in df.columns],
        style_data_conditional=all_columns_styles
    ),
])

if __name__ == '__main__':
    app.run(debug=True)
