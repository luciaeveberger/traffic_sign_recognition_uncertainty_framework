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
                 rain_sensor,
                 location_data = ""
                 ):

        self.geographical = Geographical.Geographical(coordinates,
                                                      road_type,
                                                      velocity,
                                                      location_data)
        self.img_based_measures = ImageBased.ImageBased(sign_type,
                                                        "right")

        self.environmental = Environmental.Environmental(timestamp,
                                                         month_stamp,
                                                         coordinates,
                                                         temperature,
                                                         rain_sensor)
        self.params = 3
        #@todo: clean up! 
        # self.geo_probabaility = self.geographical.verify_geographical_parameters()
        # self.image_probability = self.img_based_measures.verify_image_based_parameters()
        # env_probability = self.environmental.verify_environmental_parameters()



    def calculate_scope(self):
        geo_probability = self.geographical.verify_geographical_parameters()
        image_probability = self.img_based_measures.verify_image_based_parameters()
        env_probability = self.environmental.verify_environmental_parameters()
        if geo_probability == 0:
            # not in germany!
            compiled_probability = 0
        else:
            # calculate compiled score!
            compiled_probability =  (geo_probability +  env_probability + image_probability)

        return {"geo": geo_probability,
                "env": env_probability,
                "img": image_probability,
                "total": compiled_probability}