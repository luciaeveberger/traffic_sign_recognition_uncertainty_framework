import pandas as pd

# @todo: figure out what is needed for environmental
import Environmental
import Geographical
import ImageBased

data_file_path = "test_dataset/data/generated_data.csv"


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


        self.geographical = Geographical.Geographical(coordinates,
                                                      road_type,
                                                      velocity)
        self.img_based_measures = ImageBased.ImageBased(sign_type,
                                                        "right")
        self.environmental = Environmental.Environmental(timestamp,
                                                         coordinates,
                                                         temperature,
                                                         rain_sensor)
        self.params = 3

    def calculate_scope(self):
        compiled_score = (self.geographical.verify_geographical_parameters() +
                          self.img_based_measures.verify_image_based_parameters() +
                          self.environmental.verify_environmental_parameters()
                          ) / self.params
        return compiled_score


df = pd.read_csv(data_file_path)
# to make the coordinates easier to use
df['Coordinates_Joined'] = list(zip(df.Longitude, df.Latitude))
df['Scope_Score'] = 0

# can replace the scope column
s = ScopeModelValidator(timestamp=df.Datetime[6],
                        temperature=df.Temperature[6],
                        coordinates=df.Coordinates_Joined[6],
                        sign_type=df.ClassId[6],
                        road_type="highway",
                        velocity=df.Speed[6],
                        rain_sensor=0
                        )

print(s.calculate_scope())

s2 = ScopeModelValidator(timestamp=df.Datetime[3],
                        temperature=df.Temperature[3],
                        coordinates=df.Coordinates_Joined[3],
                        sign_type=df.ClassId[3],
                        road_type="highway",
                        velocity=df.Speed[3],
                        rain_sensor=0
                        )

print(s2.calculate_scope())