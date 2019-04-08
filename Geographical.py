import requests
import TargetApplicationScope
import json


output_format = "json"
t = TargetApplicationScope.TargetApplicationScope()
velocity_constraint = t.get_velocity()
country_constraint = t.get_country()

#url = "https://nominatim.openstreetmap.org/reverse?format=" + output_format
url = "http://188.40.207.242/nominatim/reverse?format=jsonv2"


class Geographical:
    def __init__(self,
                 coordinates,
                 road_type,
                 velocity):
        self.coordinates = coordinates
        self.road_types = road_type
        self.velocity = velocity
        self.parameters = 3

    def verify_coordinates(self):
        """
            input: coordinates list, [0] Long, [1] Lat
            reverse geo-coding to check if coordinates are contained
            parses API message
         """

        revised_url = \
            url + "&lat=" + str(self.coordinates[1]) + "&lon=" + str(self.coordinates[0])


        r = requests.get(revised_url)
        print(r.text)
        # @todo for 400
        coordinates_country = json.loads(r.text)["address"]['country']
        if coordinates_country == country_constraint:
            return 1
        else:
            return 0
        #return

    def verify_road_type(self):
        ### chategory type => can parse from here

        """
        :return:
        """
        return 1

    def verify_velocity(self):
        ## @toDo based on place?
        print(self.velocity)
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



# (54.48086620605899, 7.578818052368505)

## in UK
# g = Geographical(54.48,
#                  7.57, "highway", 100)
# print(g.verify_geographical_parameters())
# #
# # ## in Germany
#
#
# g = Geographical([52.52,
#                   13.404954], "highway", 100)
# print(g.verify_geographical_parameters())
#
# ## over speed limit
# g = Geographical([52.52,
#                   13.404954], "highway", -100)
# print(g.verify_geographical_parameters())