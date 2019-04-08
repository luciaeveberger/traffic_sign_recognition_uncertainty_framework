import pandas as pd

# @todo: figure out what is needed for environmental
#import Environmental
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
        # self.environmental = Environmental.Environmental(timestamp, temperature, lat, long, rain_sensor)
        self.geographical = Geographical.Geographical(coordinates, road_type, velocity)
        self.img_based_measures = ImageBased.ImageBased(sign_type, "right")

    def calculate_scope(self):
        compiled_score = self.geographical.verify_geographical_parameters() + self.img_based_measures.verify_image_based_parameters()
        return compiled_score


df = pd.read_csv(data_file_path)

# to make the coordinates easier to use
df['Coordinates_Joined'] = list(zip(df.Longitude, df.Latitude))

s = ScopeModelValidator(timestamp=df['Datetime'][5],
                        temperature=df['Temperature'][5],
                        coordinates=df['Coordinates_Joined'][5],
                        sign_type=df['ClassId'][5],
                        road_type="highway",
                        velocity=df['Speed'][5],
                        rain_sensor=0
                        )
print(s.calculate_scope())


# for all the points
# for index, row in df.iterrows():
#     s =  ScopeModelValidator(row['Datetime'],

