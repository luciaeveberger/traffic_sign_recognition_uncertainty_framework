import requests
from target_application_scope import TargetApplicationScope
import json

t = TargetApplicationScope.TargetApplicationScope()
url = "https://nominatim.openstreetmap.org/reverse?format=json"

# https://nominatim.opgitenstreetmap.org/reverse?format=json&lat=52.5487429714954&lon=-1.81602098644987&zoom=18&addressdetails=1
class Geographical:
    def __init__(self, coordinates):
        self.coordinates = coordinates
        self.country = t.get_country()

    def verifyCoordinates(self):
        revised_url = \
            url + "&lat=" + str(self.coordinates[0]) + "&lon=" + str(self.coordinates[1])
        r = requests.get(revised_url)
        coordinates_country = json.loads(r.text)["address"]['country']
        if coordinates_country == self.country:
            return True
        else:
            return False

g = Geographical([52.548742971495,1.81602098644987])
print(g.verifyCoordinates())