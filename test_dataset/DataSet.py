import pandas as pd
import numpy as np

import sys
sys.path.append("..")
import TargetApplicationScope

## defines the parameter ranges we should be looking for
t = TargetApplicationScope.TargetApplicationScope()
lookup_table = t.__dict__
appropriate_test_cases = 5


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
    print(lookup_table)
    return
