#from __future__ import division
import time
import pandas as pd
import numpy as np


import ScopeModelValidator

data_file_path = "test_dataset/data/generated_data1.csv"
data_output = "scope_model_results.csv"

def compile_scope_probabilites(df_sampled):
    df_sampled['env_probability '] = 0
    df_sampled['geo_probability '] = 0
    df_sampled['Scope_Probability_Verbose'] = ""
    df_sampled['Scope_Probability'] = 0.00

    location_data = ""
    for i, row in df_sampled.iterrows():
        if 'Open_Data' in df_sampled.columns:
            location_data = row.Open_Data
        s = ScopeModelValidator.ScopeModelValidator(timestamp=row.Datetime,
                                                    month_stamp=row.month,
                                                    temperature=row.Temperature,
                                                    coordinates=row.Coordinates_Joined,
                                                    sign_type=row.ClassId,
                                                    road_type=row.RoadTypes,
                                                    velocity=row.Speed,
                                                    rain_sensor=4,
                                                    location_data=location_data
                                                    )
        all_probabilities = s.calculate_scope()
        df_sampled.at[i, 'temp_probability'] = all_probabilities.get('env')
        df_sampled.at[i, 'geo_probability'] = all_probabilities.get('geo')
        df_sampled.at[i,'Scope_Probability_Verbose'] = all_probabilities
        total = all_probabilities.get('total')/3
        print("SCOPE PROBABILITY {}".format(total))
        df_sampled.at[i, 'Scope_Probability'] = total
        if not location_data and  i % 25 == 0:
            # to be used with the api
            time.sleep(30)
    return df_sampled


if __name__ == '__main__':
    df = pd.read_csv(data_file_path)
    df['Coordinates_Joined'] = list(zip(df.Longitude, df.Latitude))
    print("Actual size {}".format(len(df)))
    sample = df.head(10000)
    scope_probabilities_df = compile_scope_probabilites(sample)
    scope_probabilities_df.to_csv(data_output)