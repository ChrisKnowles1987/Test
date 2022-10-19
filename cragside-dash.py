# Run this app with `python cragside-dash.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
from pathlib import Path
import results_database_plot_builder


app = dash.Dash(__name__)

database = (r"C:\Users\Chris\Python projects\IONIS\IONIS test\Processing_Results.db")

(similarity_plot, similarity_with_rejects_plot, similarity_new_normalization_plot, noise_plot, spacing_plot, spacing_mad_plot, masserror_plot, masserror_mad_plot, isotope_fit_against_spacing_mad_plot, isotope_fit_against_isotope_rejects_plot, isotope_fit_against_new_normalization, masserror_against_masserror_mad_plot, isotope_rejects_against_new_normalisation_plot) = results_database_plot_builder.build_plots_and_dataframes_from_database(database)

app.layout = html.Div(children=[
    html.H1(children=str(database)),

    dcc.Graph(
        figure=similarity_plot
    ),
    dcc.Graph(
        figure=similarity_with_rejects_plot
    ),
    dcc.Graph(
        figure=similarity_new_normalization_plot
    ),
    dcc.Graph(
        figure=isotope_fit_against_isotope_rejects_plot
    ),
    dcc.Graph(
        figure=isotope_fit_against_new_normalization
    ),
    dcc.Graph(
        figure=noise_plot
    ),
    dcc.Graph(
        figure=spacing_plot
    ),
    dcc.Graph(
        figure=spacing_mad_plot
    ),
    dcc.Graph(
        figure=masserror_plot
    ),
    dcc.Graph(
        figure=masserror_mad_plot
    ),
    dcc.Graph(
        figure=isotope_fit_against_spacing_mad_plot
    ),
    dcc.Graph(
        figure=masserror_against_masserror_mad_plot
    ),
    dcc.Graph(
        figure=isotope_rejects_against_new_normalisation_plot
    ),
])


if __name__ == '__main__':
    app.run_server(debug=True)
