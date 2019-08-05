import pandas as pd
import numpy as np
import os
from os.path import dirname
import GenerateHistoricalData
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import scipy.stats as st


from scipy import spatial
root_directory = os.path.dirname(os.getcwd())


class WeatherSampler:
    def __init__(self, month, input_file_path, station_id=None):
        """

        :param month:
        :param input_file_path:
        :param station_id:
        """
        #self.g = GenerateHistoricalData.GenerateHistoricalData(input_file_path)
        self.df = pd.read_csv(root_directory +
                              input_file_path[0] +
                              input_file_path[1])
        self.month = month
        self.station_id = station_id
        if station_id:
            self.subsample = self.subsample_dataframe(self.df, self.month, self.station_id)


    def subsample_dataframe(self, df, month, station_id):
        return df.loc[(df['month'] == month) & (df['STATIONS_ID'] == station_id)]['TT_TU']


    def verify_distribution(self, subsample):
        k2, p = scipy.stats.normaltest(subsample)
        alpha = 1e-3
        print("p = {:g}".format(p))
        p = 3.27207e-11
        if p < alpha:  # null hypothesis: x comes from a normal distribution
            print("Normal distribution ")
        return

    def build_probability_list(self, subsample):
        std = (np.std(subsample))
        mean = (np.mean(subsample))
        print("MEAN: {} & STD: {}".format(mean, std))
        print(mean)
        list_of_prob = list()
        for i in range(-40, 40):
            #print(i)
            if i > mean :
                prob = scipy.stats.norm.sf(i,mean,std)
            if i < mean :
                prob = scipy.stats.norm.cdf(i,mean,std)
            list_of_prob.append([i, prob])
        print(list_of_prob)
        return list_of_prob

hourly_air_lookup =  ["/test_dataset/weather_data/hourly/air_temperature/recent/",
                      "hourly_air_temp_compiled_by_month.csv"]
ws = WeatherSampler(hourly_air_lookup, 5)
print(ws.build_probability_list)