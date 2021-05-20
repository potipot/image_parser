import json
import pandas as pd


def to_csv(json_filepath, csv_filepath):
    """
    Function that converts json label files to csv files using pandas DataFrame
    :param json_filepath:
    :param csv_filepath:
    :return:
    """
    with open(json_filepath) as infile:
        data = json.load(infile)

    df = pd.DataFrame.from_dict(data['files'], orient='index')
    df.reset_index(inplace=True)
    df.rename(columns={'index': 'filepath', 0: 'label'}, inplace=True)
    df.to_csv(csv_filepath, index=False)
