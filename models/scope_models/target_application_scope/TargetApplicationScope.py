import json
path = "/Users/luciaeve/Documents/EMSE/KAISERSLAUTERN/THESIS/code/tsr_uncertainy_framework/models/scope_models/target_application_scope/Germany/"

class TargetApplicationScope:
    def __init__(self):
        with open(path + 'GermanyTAS.json') as json_data:
            d = json.load(json_data)
            self.country = d['country']
            self.coordinates = d['coordinates']
            self.set_of_signs = d['set_of_signs']
            self.available_years = d['available_years']
            self.road_types = d['road_types']
            self.temperature = d['temperature']
            self.velocity = d['velocity']
            self.driving_direction = d['driving_direction']

    def get_velocity(self):
        return self.velocity

    def get_country(self):
        return self.country

