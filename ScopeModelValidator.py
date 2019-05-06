# @todo: figure out what is needed for environmental
import Environmental
import Geographical
import ImageBased



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
        compiled_score =  (self.geographical.verify_geographical_parameters()*
                          self.img_based_measures.verify_image_based_parameters() *
                          self.environmental.verify_environmental_parameters())

        return compiled_score
