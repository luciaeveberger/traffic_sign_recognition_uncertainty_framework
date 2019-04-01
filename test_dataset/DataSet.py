import pandas as pd
import numpy as np

import sys
sys.path.append("..")
import TargetApplicationScope

## defines the parameter ranges we should be looking for
t = TargetApplicationScope.TargetApplicationScope()
lookup_table = t.__dict__
appropriate_test_cases = 5

def return_min_max(column):
    """ returns the max & min on column [min, max]"""
    return [min(column), max(column)]

def check_range(tas_parms, column):
    min_max = return_min_max(column)
    for key in tas_parms:
        if "min" in key:
            print(tas_parms[key])
            if tas_parms[key] >= min_max[0]:
                print("YAY")
        if "max" in key:
            if tas_parms[key] <= min_max[1]:
                print("YAY")

    ## may check regular distribution
    ## check that the tas_params are less than the column values
    return


def generate_dataset(file_path):
    df = pd.read_csv(file_path)

    # Geographical Elements
    df['Latitude'] = np.random.uniform(30, 50, df.shape[0])
    df['Longitude'] = np.random.uniform(0, 50, df.shape[0])
    df['Altitude'] = np.random.uniform(-500,  2962, df.shape[0])
    df['Datetime'] = np.random.randint(1459138574, 1553746574, df.shape[0])
    df['Speed'] = np.random.uniform(0,130, df.shape[0])

    # Environmental Elements

    # ImageBased Elements
    return df

def validate_params(data):
    """
     Range-based:
    + coordinateRange(coordinates, max_coordinate, min_coordinate)
    + temperatureRange(temperature, min_temp, max_temp):
    + yearRange(year, timestamp)
    + velocityRange(min_velocity, max_velocity)
    + rainSensorRange(min_rain, max_rain)
    """
    #  + velocityRange(min_velocity, max_velocity)
    velocity_data = data['Speed']
    velocity_params = lookup_table['velocity']
    check_range(velocity_params, velocity_data )

    temp_params = lookup_table['temperature']
    check_range(velocity_params, velocity_data )

    time_params = lookup_table['available_years']

    return
