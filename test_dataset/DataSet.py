import pandas as pd
import numpy as np
import requests
import json

url = "https://elevation-api.io/api/elevation?points="


def generate_dataset(file_path):
    print("GENERATING COORDINATES DATA")
    df = pd.read_csv(file_path)

    # Geographical Elements
    df['Latitude'] = np.random.uniform(46, 55, df.shape[0])
    df['Longitude'] = np.random.uniform(6, 14, df.shape[0])
    df['Coordinates'] = tuple(zip(df['Latitude'], df['Longitude']))

    print("GENERATING ELEVATION/ALTITUDE DATA")
    elevations = calculate_elevations(df)
    print("ELEVATION DATA FINISHED")


    df['Elevation'] = elevations

    print("DATETIME DATA")
    df['Datetime'] = np.random.randint(1522674299, 1553746574, df.shape[0])
    df['Speed'] = np.random.uniform(0,130, df.shape[0])

    # Environmental Elements -> need to do some sampling
    df['Temperature'] =  np.random.uniform(-20,  35, df.shape[0])

    # ImageBased Elements
    return df


def calculate_elevations(df):
    """
    uses the elevation API to calculate the elevations based on the
    coordinates

    :param df:
    :return: [] list of altitudes
    """
    elevations = list()

    for k,g in df.groupby(np.arange(len(df))//10):
        response_body = ""
        for element in g['Coordinates']:
            response_body = response_body + str(element).replace(" ", "") + ","
        response = json.loads(requests.get(url + response_body).text)['elevations']
        for index in range(len(response)):
            elevations.append(response[index]['elevation'])

    return elevations


