import requests
from target_application_scope import TargetApplicationScope
import json


output_format = "json"
t = TargetApplicationScope.TargetApplicationScope()
velocity_constraint = t.get_velocity()
country_constraint = t.get_country()

url = "https://nominatim.openstreetmap.org/reverse?format=" + output_format

class Geographical:
    def __init__(self, coordinates, road_type, velocity):
        self.coordinates = coordinates
        self.road_types = road_type
        self.velocity = velocity
        self.parameters = 3

    def verify_coordinates(self):
        """
            reverse geo-coding to check if coordinates are contained
            parses API message
         """
        revised_url = \
            url + "&lat=" + str(self.coordinates[0]) + "&lon=" + str(self.coordinates[1])
        r = requests.get(revised_url)
        coordinates_country = json.loads(r.text)["address"]['country']
        if coordinates_country == country_constraint:
            return 1
        else:
            return 0

    def verify_road_type(self):
        """
        :return:
        """
        return 1

    def verify_velocity(self):
        if self.velocity >= velocity_constraint['min_velocity']  \
                and self.velocity <= velocity_constraint['max_velocity']:
            return 1
        else:
            return 0

    def verify_geographical_parameters(self):
        """ returns final geographical score """
        factor_eval = 100/self.parameters
        return (factor_eval * (self.verify_coordinates()
                               + self.verify_road_type()
                               + self.verify_velocity())
                )/100



## in UK
g = Geographical([52.548742971495,
                  1.81602098644987], "highway", 100)
print(g.verify_geographical_parameters())

## in Germany
g = Geographical([52.52,
                  13.404954], "highway", 100)
print(g.verify_geographical_parameters())

## over speed limit
g = Geographical([52.52,
                  13.404954], "highway", -100)
print(g.verify_geographical_parameters())