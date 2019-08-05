#from __future__ import division
import time
import pandas as pd
import numpy as np


import ScopeModelValidator
#"input_files/fail_input.csv"
annoted_test_path = "input_files/UC1_Testset_Germany/contextInfo.csv"
data_output = "input_files/contextInfoScope.csv"

scope_constant_factor = 0.981
scope_constant_year = 2018

def calculate_concept_drift(test_point, sc_factor, sc_year, test_year):
    return test_point*sc_factor**(abs(1+sc_year - test_year))


def compile_scope_probabilites(df_sampled):
    df_sampled['env_probability '] = 0
    df_sampled['geo_probability '] = 0
    df_sampled['Scope_Probability_Verbose'] = ""
    df_sampled['Scope_Probability'] = 0.00
    df_sampled['month'] = pd.DatetimeIndex(df_sampled['DATE']).month
    df_sampled['year'] = pd.DatetimeIndex(df_sampled['DATE']).year

    location_data = ""
    for i, row in df_sampled.iterrows():
        if 'Open_Data' in df_sampled.columns:
            location_data = row.Open_Data
        s = ScopeModelValidator.ScopeModelValidator(timestamp=row.DATE,
                                                    month_stamp=row.month,
                                                    temperature=row.TEMPERATURE,
                                                    coordinates=row.Coordinates_Joined,
                                                    sign_type=1,
                                                    road_type=row.ROADTYPE,
                                                    velocity=row.VEHICLESPEED,
                                                    rain_sensor=row.PRECIPITATION_AMOUNT,
                                                    location_data=location_data
                                                    )
        all_probabilities = s.calculate_scope()
        print(all_probabilities)
        df_sampled.at[i, 'temp_probability'] = all_probabilities.get('env')
        df_sampled.at[i, 'geo_probability'] = all_probabilities.get('geo')
        df_sampled.at[i,'Scope_Probability_Verbose'] = all_probabilities
        scope_probability = all_probabilities.get('total')/3

        total = calculate_concept_drift(scope_probability,
                                        scope_constant_factor,
                                        scope_constant_year,
                                        row['year'])

        print("SCOPE PROBABILITY {}".format(total))
        df_sampled.at[i, 'Scope_Probability'] = total

        if not location_data and  i % 25 == 0:
            # to be used with the api
            time.sleep(15)
    return df_sampled


if __name__ == '__main__':
    #print(calculate_concept_drift(scope_constant_factor, scope_constant_year, 2018))
    df = pd.read_csv(annoted_test_path, error_bad_lines=False)
    print(df.columns)
    df['Coordinates_Joined'] = list(zip(df.LONGITUDE, df.LATITUDE))
    scope_probabilities_df = compile_scope_probabilites(df)
    scope_probabilities_df = scope_probabilities_df.reindex(sorted(scope_probabilities_df.columns), axis=1)
    scope_probabilities_df.to_csv(data_output, index=False)