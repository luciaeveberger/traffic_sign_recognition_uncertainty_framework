import pandas as pd

# @todo: figure out what is needed for environmental
#import Environmental
import Geographical
import ImageBased



class ScopeModelValidator:
    # Data point (timestamp, temperature, coordinates, sign_type, road_type, velocity, rain_sensor)
    def __init__(self,
                 timestamp,
                 temperature,
                 coordinates,
                 sign_type,
                 road_type,
                 velocity,
                 rain_sensor):
        #self.environmental = Environmental.Environmental(timestamp, temperature, lat, long, rain_sensor)
        self.geographical = Geographical.Geographical(coordinates, road_type, velocity)
        self.img_based_measures = ImageBased.ImageBased(sign_type, "right")

        ## each of the models
    def calculate_scope(self):
        compiled_score = self.geographical.verify_geographical_parameters()
        return compiled_score

## testset
df = pd.read_csv("test_dataset/data/generated_data.csv")

df['Coordinates_Joined'] = list(zip(df.Longitude, df.Latitude))

s =  ScopeModelValidator(df['Datetime'][5],
                         df['Temperature'][5],
                         df['Coordinates_Joined'][5],
                         "stop",
                         "highway",
                         df['Speed'][5],
                         "1000")
print(s.calculate_scope())
#print(df.head)

## for all the points
# for index, row in df.iterrows():
#     s =  ScopeModelValidator(row['Datetime'],
#                              row['Temperature'],
#                              row['Coordinates_Joined'],
#                              "stop",
#                              "highway",
#                              row['Speed'],
#                              "1000")
#     s.calculate_scope()
#     pass
    #print(row['Temperature'])
