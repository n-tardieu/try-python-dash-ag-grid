import colorlover
from constantes.carColors import carColors
from colorlover import scales
import matplotlib.pyplot as plt
import numpy as np
from constantes.colors import redToBlueScale


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

    return styleConditions

def discrete_background_color(df, n_bins=9, columns="all"):
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    if columns == "all":
        df_numeric_columns = df.select_dtypes("number")
    else:
        df_numeric_columns = df[columns]
    df_max = df_numeric_columns.max().max()
    df_min = df_numeric_columns.min().min()
    ranges = [((df_max - df_min) * i) + df_min for i in bounds]
    styleConditions = []
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

    return styleConditions




def discrete_background_color_red_by_blue(df, n_bins=255, columns="all"):
    colorScale = redToBlueScale(n_bins)

    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    if columns == "all":
        df_numeric_columns = df.select_dtypes("number")
    else:
        df_numeric_columns = df[columns]
    df_max = df_numeric_columns.max().max()
    df_min = df_numeric_columns.min().min()
    ranges = [((df_max - df_min) * i) + df_min for i in bounds]
    
    styleConditions = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        if i == len(bounds) - 1:
            max_bound += 1

        backgroundColor = colorScale[i - 1]
        color = "white" if i > len(bounds) / 2.0 else "inherit"

        styleConditions.append(
            {
                "condition": f"params.value >= {min_bound} && params.value < {max_bound}",
                "style": {"backgroundColor": backgroundColor, "color": color},
            }
        )

    return styleConditions

def create_car_style(df, column: str):  # Assurez-vous que column est bien une str

    if column not in df.columns:
        raise ValueError(f"La colonne {column} n'existe pas dans le DataFrame.")

    styleConditions = []
    unique_values = [str(value) for value in df[column].unique()]

    for value in unique_values:
        if value in carColors:
            styleConditions.append({
                "condition": f"params.value == '{value}'",
                "style": {"backgroundColor": carColors[value], "color": "white"},
            })
    return styleConditions


def discrete_background_color_bins_for_datagrid(df, n_bins=5, columns='all'):
    import colorlover
    bounds = [i * (1.0 / n_bins) for i in range(n_bins + 1)]
    if columns == 'all':
        if 'id' in df:
            df_numeric_columns = df.select_dtypes('number').drop(['id'], axis=1)
        else:
            df_numeric_columns = df.select_dtypes('number')
    else:
        df_numeric_columns = df[columns]
    df_max = df_numeric_columns.max().max()
    df_min = df_numeric_columns.min().min()
    ranges = [
        ((df_max - df_min) * i) + df_min
        for i in bounds
    ]
    styles = []
    for i in range(1, len(bounds)):
        min_bound = ranges[i - 1]
        max_bound = ranges[i]
        backgroundColor = colorlover.scales[str(n_bins)]['seq']['Blues'][i - 1]
        color = 'white' if i > len(bounds) / 2. else 'inherit'

        for column in df_numeric_columns:
            styles.append({
                'if': {
                    'filter_query': (
                        '{{{column}}} >= {min_bound}' +
                        (' && {{{column}}} < {max_bound}' if (i < len(bounds) - 1) else '')
                    ).format(column=column, min_bound=min_bound, max_bound=max_bound),
                    'column_id': column
                },
                'backgroundColor': backgroundColor,
                'color': color
            })

    return styles