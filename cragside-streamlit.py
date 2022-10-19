# Run this app with `streamlit run cragside-streamlit.py --server.port 5998` and

import pandas as pd
import streamlit as st
import results_database_plot_builder

filename = "Processing_Results.db"
spectrum = "1_ TOF MSMS 1430_(100-4000) 30eV ESI-_D1422_d4b5a1e3-4a1a-4ab7-8770-80482d9385de"

database = "C:\\CragsideProcessing\\Noise\\" + spectrum + "\\" + filename

(similarity_plot, similarity_with_rejects_plot, similarity_new_normalization_plot, noise_plot, spacing_plot, spacing_mad_plot, masserror_plot, masserror_mad_plot, isotope_fit_against_spacing_mad_plot, isotope_fit_against_isotope_rejects_plot, isotope_fit_against_new_normalization) = results_database_plot_builder.build_plots_and_dataframes_from_database(database)

st.title('D1422 1430 CE30')

st.plotly_chart(similarity_plot, use_container_width=True)
st.plotly_chart(similarity_with_rejects_plot, use_container_width=True)
st.plotly_chart(similarity_new_normalization_plot, use_container_width=True)
st.plotly_chart(isotope_fit_against_isotope_rejects_plot, use_container_width=True)
st.plotly_chart(isotope_fit_against_new_normalization, use_container_width=True)
st.plotly_chart(noise_plot, use_container_width=True)
st.plotly_chart(spacing_plot, use_container_width=True)
st.plotly_chart(spacing_mad_plot, use_container_width=True)
st.plotly_chart(masserror_plot, use_container_width=True)
st.plotly_chart(masserror_mad_plot, use_container_width=True)
st.plotly_chart(isotope_fit_against_spacing_mad_plot, use_container_width=True)
