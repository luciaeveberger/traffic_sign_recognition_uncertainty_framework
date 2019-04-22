import pandas as pd
import numpy as np
import requests
import json
import time
from datetime import datetime


url = "https://elevation-api.io/api/elevation?points="
json_file_path = "data/data_lookup_params.json"
loc_url = "https://nominatim.openstreetmap.org/reverse?format=jsonv2"


def generate_dataset(file_path):
    """
    generates mock sensor_data to be tested
    in the scope model, data sufficiency & compliancy
    :param file_path:
    :return: dataframe
    """

    print("GENERATING COORDINATES DATA")
    df = pd.read_csv(file_path)

    with open(json_file_path) as json_data:
        # @note -> df[shape] can be changed to whatever size we want to randomize
        d = json.load(json_data)

        #   randomized elements
        df['Latitude'] = np.random.uniform(d["latitude"][0], d["latitude"][1], df.shape[0])
        df['Longitude'] = np.random.uniform(d['longitude'][0], d['longitude'][1], df.shape[0])
        df['Coordinates'] = tuple(zip(df['Latitude'], df['Longitude']))

        # creates the date-time data based on a year long of random
        # start and end
        print("DATETIME DATA")
        df['Datetime'] = np.random.randint(d['datetime'][0], d['datetime'][1], df.shape[0])
        df['formattedTime'] = pd.to_datetime(df['Datetime'], unit='s')

        df['month'] = pd.to_datetime(df['formattedTime']).dt.strftime('%m')

        temperature_generator = list()
        precipitation_generator = list()

        count = 0
        for month in df['month']:
            for event in d['temp']:
                if month == event:
                    temperature_generator.append(
                        np.random.uniform(d['temp'][event][0], d['temp'][event][1]))
                    precipitation_generator.append(
                        np.random.uniform(d['precip'][event][0], d['precip'][event][1]))
                # adds random noise
                if count % 550:
                    temperature_generator.append(40)
                    precipitation_generator.append(120)

        df['Temperature'] = temperature_generator
        df['Precipitation'] = precipitation_generator

    # profiles based on the randomized data
    print("ELEVATION DATA GENERATING")
    #df['Elevation'] = calculate_elevations(df)

    print("ELEVATION DATA GENERATING")

    print("GENERATING GEOGRAPHICAL PROFILE & RoadType")
    df['Open_Data'] = calculate_open_data(df)
    #
    # # elevations generated
    #
    # df['Speed'] = np.random.uniform(0,130, df.shape[0])
    #
    # # @toDO: refine temperature & precipitation profiles
    # print("TEMPERATURE SAMPLING")
    #
    #
    # # Environmental Elements -> need to do -> based on high and low on those months
    # df['Temperature'] = np.random.uniform(-20,  35, df.shape[0])
    # df['Precipitation'] = np.random.uniform(0, 20, df.shape[0])

    # ImageBased Elements
    df.to_csv("data/generated_data1.csv")
    return df


def calculate_open_data(df):
    """
    gathers the open_Data points on the location, including the region, & name
    :param df: coordinates
    :return: list of open-data json objects
    """

    open_map_data = list()
    count = 0
    for i in df.index:
        val = df.loc[i,'Coordinates']
        revised_url = \
            loc_url + "&lat=" + str(val[0]) + "&lon=" + str(val[1])
        try:
            r = requests.get(revised_url, headers={'User-agent': '0.' + str(count)})
        except requests.exceptions.HTTPError as err:
            r = err
        print(r.text)
        open_map_data.append(r.text)
        count = count + 1
        if count % 300 == 0:
            time.sleep(30)
    return open_map_data


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


generate_dataset("data/base_test_data.csv")


