#from __future__ import division
import time
import pandas as pd
import numpy as np


import ScopeModelValidator



annoted_test_path = "/Users/luciaeve/Documents/EMSE/KAISERSLAUTERN/" \
                    "THESIS/code/CompiledCode/TSD/DT_PROTOTYPE/scope_annotated_data.csv"
data_output = "scope_model_results.csv"

def compile_scope_probabilites(df_sampled):
    df_sampled['env_probability '] = 0
    df_sampled['geo_probability '] = 0
    df_sampled['Scope_Probability_Verbose'] = ""
    df_sampled['Scope_Probability'] = 0.00
    df_sampled['RoadTypes'] = "road"

    location_data = ""
    for i, row in df_sampled.iterrows():
        if 'Open_Data' in df_sampled.columns:
            location_data = row.Open_Data
        s = ScopeModelValidator.ScopeModelValidator(timestamp=row.Datetime,
                                                    month_stamp=row.month,
                                                    temperature=row.Temperature,
                                                    coordinates=row.Coordinates_Joined,
                                                    sign_type=1,
                                                    road_type=row.RoadTypes,
                                                    velocity=row.velocity,
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
    df = pd.read_csv(annoted_test_path)
    print(df.columns)
    df['Coordinates_Joined'] = list(zip(df.Longitude, df.Latitude))
    print("Actual size {}".format(len(df)))
    scope_probabilities_df = compile_scope_probabilites(df)
    scope_probabilities_df.to_csv(data_output, index=False)