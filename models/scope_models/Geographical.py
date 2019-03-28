import requests
from target_application_scope import TargetApplicationScope
import json

output_format = "json"
t = TargetApplicationScope.TargetApplicationScope()
url = "https://nominatim.openstreetmap.org/reverse?format=" + output_format

class Geographical:
    def __init__(self, coordinates, road_type, velocity):
        self.coordinates = coordinates
        self.country = t.get_country()
        self.road_types = road_type
        self.velocity = velocity


    def verify_coordinates(self):
        """ reverse geo-coding to check if coordinates are contained
            parses API message
         """
        revised_url = \
            url + "&lat=" + str(self.coordinates[0]) + "&lon=" + str(self.coordinates[1])
        r = requests.get(revised_url)
        coordinates_country = json.loads(r.text)["address"]['country']
        if coordinates_country == self.country:
            return 1
        else:
            return 0

    def verify_road_type(self):
        return 1

    def verify_velocity(self):
        if self.velocity > 0 & self.velocity <100:
            return 1
        else:
            return 0

    def verify_geographical_parameters(self):
        """ returns final geographical score """
        return self.verify_coordinates() + self.verify_road_type() + self.verify_velocity()


g = Geographical([52.548742971495,1.81602098644987], "highway", 100)
#print(g.verify_geographical_parameters())