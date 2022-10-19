import pandas as pd


def load_matches(path):
    matches = pd.read_csv(path)
    matches.columns = ['Ion', 'Series', 'Direction', 'ObservedMass', 'Intensity', 'ExpectedMass', 'MassErrorPpm']
    return matches


def load_detected_peaks(path):
    peaks = pd.read_csv(path)
    return peaks


def load_spectrum(path):
    spectrum = pd.read_csv(path)
    spectrum.columns = ['Mz', 'Intensity']
    return spectrum
