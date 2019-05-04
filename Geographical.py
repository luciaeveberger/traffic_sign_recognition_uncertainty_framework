import requests
import TargetApplicationScope
import json


output_format = "json"
t = TargetApplicationScope.TargetApplicationScope()
velocity_constraint = t.get_velocity()
country_constraint = t.get_country()


url = "https://nominatim.openstreetmap.org/reverse?format=jsonv2"


class Geographical:
    def __init__(self,
                 coordinates,
                 road_type,
                 velocity):
        self.coordinates = coordinates
        self.road_type = road_type
        self.velocity = velocity
        self.parameters = 3


    def verify_lat(self):
        # @todo: based on the border
        return

    def verify_long(self):
        # @todo: based on the border
        return

    def verify_coordinates(self):
        """
            input: coordinates list, [0] Long, [1] Lat
            reverse geo-coding to check if coordinates are contained
            parses API message
         """
        # call child methods here


        revised_url = \
            url + "&lat=" + str(self.coordinates[1]) + "&lon=" + str(self.coordinates[0])


        r = requests.get(revised_url)
        print(json.loads(r.text)["address"]['country'])
        # @todo for 400
        coordinates_country = json.loads(r.text)["address"]['country']
        if coordinates_country == country_constraint:
            return 1
        else:
            return 0

    def verify_road_type(self):
        ### chategory type => can parse from here

        """
        :return:
        """
        if self.road_type in t.get_road_types():
            return 1
        return 0

    def verify_velocity(self):
        if velocity_constraint['min_velocity'] <= \
                self.velocity  \
                <= velocity_constraint['max_velocity']:
            return 1
        return 0

    def verify_geographical_parameters(self):
        """ returns final geographical score """
        factor_eval = 100/self.parameters
        probability = self.verify_coordinates() \
                      *(factor_eval * (self.verify_coordinates()
                                       + self.verify_road_type()
                                       + self.verify_velocity())
                        )/100
        print(probability)
        return probability
