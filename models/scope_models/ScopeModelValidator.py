import Environmental
import Geographical
import ImageBased


class ScopeModelValidator:
    # Data point (timestamp, temperature, coordinates, sign_type, road_type, velocity, rain_sensor)
    def __init__(self, timestamp, temperature, coordinates, sign_type, road_type, velocity, rain_sensor):
        environmental = Environmental(timestamp, temperature, coordinates, rain_sensor)
        geographical = Geographical()
        img_based_measures = ImageBased()

        ## each of the models
        compiled_score = environmental.validateMeasures()
        return compiled_score

## test set -> should be an instances of the base_test_data
test_set = []
test_set_scope_validators = []
for item in test_set:
    s = ScopeModelValidator(item)
    test_set_scope_validators.add(s)