# @todo: figure out what is needed for environmental
import Environmental
import Geographical
import ImageBased

import pandas as pd
data_file_path = "test_dataset/data/generated_data1.csv"


class ScopeModelValidator:
    # Data point (timestamp, temperature, coordinates, sign_type, road_type, velocity, rain_sensor)
    def __init__(self,
                 timestamp,
                 month_stamp,
                 temperature,
                 coordinates,
                 sign_type,
                 road_type,
                 velocity,
                 rain_sensor):

        self.geographical = Geographical.Geographical(coordinates,
                                                      road_type,
                                                      velocity)
        self.img_based_measures = ImageBased.ImageBased(sign_type,
                                                        "right")

        self.environmental = Environmental.Environmental(timestamp,
                                                         month_stamp,
                                                         coordinates,
                                                         temperature,
                                                         rain_sensor)
        self.params = 3

    def calculate_scope(self):
        print(self.geographical.verify_geographical_parameters())
        compiled_score = self.geographical.verify_geographical_parameters()*\
                         (self.geographical.verify_geographical_parameters() *
                          self.img_based_measures.verify_image_based_parameters() +
                          self.environmental.verify_environmental_parameters()
                          ) / self.params
        print(compiled_score)
        return compiled_score


df = pd.read_csv(data_file_path)
print(df.columns)

# to make the coordinates easier to use
df['Coordinates_Joined'] = list(zip(df.Longitude, df.Latitude))
df['Scope_Score'] = 0

# inside of scope
ind = 100

s = ScopeModelValidator(timestamp=df.Datetime[ind],
                        month_stamp=df.month[ind],
                        temperature=4,
                        coordinates=df.Coordinates_Joined[ind],
                        sign_type=df.ClassId[ind],
                        road_type=df.RoadTypes[ind],
                        velocity=df.Speed[ind],
                        rain_sensor=4
                        )

scope_score = s.calculate_scope()
print("calculated scope score: {}".format(scope_score))
df.at['Scope_Score', ind] = scope_score


# outside of scope
# ind = 3
# s2 = ScopeModelValidator(timestamp=df.Datetime[ind],
#
#                                              temperature=df.Temperature[ind],
#                                              coordinates=df.Coordinates_Joined[ind],
#                                              sign_type=df.ClassId[ind],
#                                              road_type=df.RoadTypes[ind],
#                                              velocity=df.Speed[ind],
#                                              rain_sensor=0
#                                              )
#
# scope_score2 = s2.calculate_scope()
# print("calculated scope score: {}".format(scope_score2))
# df.at['Scope_Score', ind] = scope_score2
