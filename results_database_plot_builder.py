import sqlite3
import pandas as pd
import plotly.express as px


def get_fragment_labels(fragment_list):
    return [f'{fragment.ion} {fragment.series}' for (i, fragment) in fragment_list.iterrows()]


def get_fragment_from_label(fragment_label):
    split = fragment_label.split()
    return {'ion': split[0], 'series': split[1]}


def build_plot(x, y, xlabel, ylabel, matched_fragments):
    annotations = get_fragment_labels(matched_fragments)
    fig = px.scatter(
        x=x,
        y=y,
        title=f'{ylabel} vs {xlabel}',
        text=annotations,
        labels={'x': xlabel, 'y': ylabel})
    fig.update_traces(textposition='top center')
    fig.update_xaxes(range=[0, x.max() * 1.1])
    fig.update_yaxes(range=[0, y.max() * 1.1])
    return fig


def build_plots_and_dataframes_from_database(database):
    conn = sqlite3.connect(database)

    matched_fragments = pd.read_sql_query("SELECT * FROM targeted_clustering_matched_fragments;", conn)

    intensities = matched_fragments.intensity
    isotope_similarity_scores = matched_fragments.isotope_similarity_score
    isotope_similarity_with_rejects = matched_fragments.isotope_score_with_rejects
    isotope_score_new_normalization = matched_fragments.isotope_score_new_normalization
    noise_factors = matched_fragments.noise_factor
    mean_isotope_spacings = matched_fragments.mean_isotope_spacing
    isotope_spacing_mads = matched_fragments.isotope_spacing_mad
    mean_mass_errors = matched_fragments.mean_mass_error
    mass_error_mads = matched_fragments.mass_error_mad

    similarity_plot = build_plot(isotope_similarity_scores, intensities, 'Isotope Similarity Score (higher values are better)', 'Intensity', matched_fragments)
    similarity_with_rejects_plot = build_plot(isotope_similarity_with_rejects, intensities, 'Isotope Similarity Score Including Rejects (higher values are better)', 'Intensity', matched_fragments)
    similarity_new_normalization_plot = build_plot(isotope_score_new_normalization, intensities, 'Isotope Similarity Score  - Normalization to expected isotopes (higher values are better)', 'Intensity', matched_fragments)
    noise_plot = build_plot(noise_factors, intensities, 'Noise Factor (lower values are better)', 'Intensity', matched_fragments)
    spacing_plot = build_plot(mean_isotope_spacings, intensities, 'Mean Isotope Spacing (values further from 1 are probably worse)', 'Intensity', matched_fragments)
    spacing_mad_plot = build_plot(isotope_spacing_mads, intensities, 'Isotope Spacing MAD (lower values mean less variation in spacing, which is probably good)', 'Intensity', matched_fragments)
    masserror_plot = build_plot(mean_mass_errors, intensities, "Mean Mass Error (lower is better but we don't know what the true value should true, so maybe not)", 'Intensity', matched_fragments)
    masserror_mad_plot = build_plot(mass_error_mads, intensities, 'Mass Error MAD (lower values mean less variation in mass error, which is probably good)', 'Intensity', matched_fragments)

    isotope_fit_against_isotope_rejects_plot = build_plot(isotope_similarity_with_rejects, isotope_similarity_scores, 'Isotope Similarity Score Including Rejects', 'Isotope Similarity Score', matched_fragments)

    isotope_fit_against_new_normalization = build_plot(isotope_score_new_normalization, isotope_similarity_scores, 'Isotope Similarity Score  - Normalization to expected isotopes', 'Isotope Similarity Score', matched_fragments)

    isotope_fit_against_spacing_mad_plot = build_plot(mass_error_mads, isotope_similarity_scores, 'Mass Error MAD', 'Isotope Similarity', matched_fragments)
    
    #ck added 15 Nov 21
    masserror_against_masserror_mad_plot = build_plot (mean_mass_errors, mass_error_mads, 'Mean Mass Error', 'Mass Error MAD', matched_fragments)
    
    isotope_rejects_against_new_normalisation_plot = build_plot (isotope_similarity_with_rejects, isotope_score_new_normalization, 'Isotope Similarity Score Including Rejects', 'Isotope Similarity Score  - Normalization to expected isotopes', matched_fragments) 
    

    return (similarity_plot, similarity_with_rejects_plot, similarity_new_normalization_plot, noise_plot,
            spacing_plot, spacing_mad_plot, masserror_plot, masserror_mad_plot, isotope_fit_against_spacing_mad_plot,
            isotope_fit_against_isotope_rejects_plot, isotope_fit_against_new_normalization, masserror_against_masserror_mad_plot,
            isotope_rejects_against_new_normalisation_plot)
