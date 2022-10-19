import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.patches import Rectangle


def plot_matches(matches):
    figure = plt.figure(figsize=(16, 16))
    grid = GridSpec(3, 2, figure=figure, height_ratios=[0.4, 0.3, 0.3])

    value_counts_plot = figure.add_subplot(grid[1,0])
    value_counts_plot.set_title('Fragment types')
    matches['Ion'].value_counts().plot(ax=value_counts_plot, kind='bar')

    hist_plot = figure.add_subplot(grid[1,1])
    hist_plot.set_title('Error histogram')
    matches.hist(ax=hist_plot, column='MassErrorPpm', bins=50)

    stem_plot = figure.add_subplot(grid[0,:])
    stem_plot.set_title('Matched fragments')
    stem_plot.yaxis.set_major_formatter(plt.FuncFormatter('{:.0f}'.format))

    observedMasses = matches['ObservedMass']
    intensities = matches['Intensity']
    stem_plot.stem(observedMasses, intensities, use_line_collection=True)

    for i, match in matches.iterrows():
        if match['Intensity'] > 30000:
            txt = f"{match['Ion']} {match['Series']}"
            stem_plot.annotate(txt, (observedMasses[i], intensities[i]))

    total_counts = matches.groupby('Ion')['Intensity'].sum()
    total_intensity = total_counts.sum()
    total_normalised_intensities = total_counts.map(
        lambda x: x / total_intensity)

    total_normalised_intensity_plot = figure.add_subplot(grid[2, 0])
    total_normalised_intensity_plot.set_title(
        'Total normalised intensity by ion type')
    total_normalised_intensities.sort_values(ascending=False).plot.bar(
        ax=total_normalised_intensity_plot)

    total_counts_plot = figure.add_subplot(grid[2, 1])
    total_counts_plot.set_title(
        'Total counts by ion type')
    total_counts.sort_values(ascending=False).plot.bar(ax=total_counts_plot)


def plot_spectrum(plt, suspectPeak, spectrum):
    mzWindowSize = 0.5
    minMz = spectrum['Mz'] >= suspectPeak['Mz'] - mzWindowSize
    maxMz = spectrum['Mz'] <= suspectPeak['Mz'] + mzWindowSize
    spectrumAroundPeak = spectrum[minMz & maxMz]

    title = "Peak at {mz:.4f}, intensity {intensity:.4f}, background {background}"
    plt.set_title(title.format(
        mz=suspectPeak["Mz"], intensity=suspectPeak["Intensity"], background=suspectPeak["ABS"]))

    plt.set_xlabel("m/z")
    plt.set_ylabel("Intensity")
    plt.ticklabel_format(useOffset=False)
    plt.plot(spectrumAroundPeak['Mz'], spectrumAroundPeak['Intensity'])
    plt.add_patch(Rectangle(
        (suspectPeak["Mz"] - 0.02, 0), 0.04, suspectPeak["Intensity"], facecolor="yellow"))


def plot_spectrum(plt, spectrum):
    plt.set_xlabel("m/z")
    plt.set_ylabel("Intensity")
    plt.ticklabel_format(useOffset=False)
    plt.plot(spectrum['Mz'], spectrum['Intensity'])
