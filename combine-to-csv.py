import sqlite3
import pandas as pd


def read_from_database(database):
    conn = sqlite3.connect(database)
    df = pd.read_sql_query("SELECT * FROM targeted_clustering_matched_fragments;", conn)
    print(f'Read data from {database}')
    return df.drop(['id'], axis=1).assign(origin=database)


files_to_combine = [
    "C:\\CragsideProcessing\\Noise\\5d119ba6-8403-4d5b-8184-9ccad0d72669\\Processing_Results.db",
    "C:\\CragsideProcessing\\D1422_MSMS_1430_CE_30_2.2-2.5\\Processing_Results.db"
]

output_file = "C:\\CragsideProcessing\\combined_databases.csv"

combined_results = pd.concat([read_from_database(file) for file in files_to_combine])

print(f'Writing combined fragment matches to {output_file}')

combined_results.to_csv(output_file)
