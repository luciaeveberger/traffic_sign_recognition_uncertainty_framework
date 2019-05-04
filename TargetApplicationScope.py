import json
import os.path

abs_path = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(abs_path, "target_application_scope/Germany/GermanyTAS.json")


class TargetApplicationScope:
    def __init__(self):
        with open(file_path) as json_data:
            d = json.load(json_data)
            self.country = d['country']
            self.coordinates = d['coordinates']
            self.set_of_signs = d['set_of_signs']
            self.available_years = d['available_years']
            self.road_types = d['road_types']
            self.temperature = d['temperature']
            self.velocity = d['velocity']
            self.driving_direction = d['driving_direction']
            self.time_frame = d['years']
            self.elevation = d['elevation']
            self.environmental_stats = d['environmental_stats']

    def get_velocity(self):
        return self.velocity

    def get_country(self):
        return self.country

    def get_set_of_sign(self):
        return self.set_of_signs

    def get_road_types(self):
        return self.road_types

    def get_temperature_contraints(self):
        return self.temperature

    def get_velocity_contrainsts(self):
        return self.velocity

    def get_driving_direction(self):
        return self.driving_direction

    def get_environmental_stat(self):
        return self.environmental_stats




t = TargetApplicationScope()
print(t.get_country())