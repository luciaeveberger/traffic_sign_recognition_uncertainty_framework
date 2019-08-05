import os
import pandas as pd

root_directory = os.path.dirname(os.getcwd())

class GenerateHistoricalData():
    def __init__(self, input_file_path):
        self.input_file_path = input_file_path
        self.historical_data = self.create_monthly_historical_data(input_file_path)


    def create_monthly_historical_data(self, input_file_path):
        print("GENERATING HISTORICAL DATA")
        df = pd.read_csv(root_directory+input_file_path[0] + input_file_path[1],";")
        df['formattedTime'] = pd.to_datetime(df['MESS_DATUM'].astype(str), format='%Y%m%d%H', errors='ignore')
        df['month'] = pd.to_datetime(df['formattedTime']).dt.strftime('%m')
        df["month"] = df.month.astype(float)
        return df.to_csv(root_directory + input_file_path[0] + "hourly_air_temp_compiled_by_month.csv")



hourly_air_lookup =  ["/test_dataset/weather_data/hourly/air_temperature/recent/", "hourly_air_temp_compiled.csv"]
g = GenerateHistoricalData(hourly_air_lookup)
print(g)





