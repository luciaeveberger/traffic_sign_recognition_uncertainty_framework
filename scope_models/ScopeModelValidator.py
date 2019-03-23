import Environmental


class ScopeModelValidator:
    # Data point (timestamp, temperature, coordinates, sign_type, road_type, velocity, rain_sensor)
    def __init__(self, timestamp, temperature, coordinates, sign_type, road_type, velocity, rain_sensor):
        environmental = Environmental (timestamp, temperature, coordinates, rain_sensor)
        ## each of the models
        compiled_score = environmental.validateMeasures()
