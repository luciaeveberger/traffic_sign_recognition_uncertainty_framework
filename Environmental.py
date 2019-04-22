class Environmental:
    # need to see if we need to check the other params
    def __init__(self,
                 timestamp,
                 coordinates,
                 temperature_sensor,
                 rain_sensor):
        self.timestamp = timestamp
        self.coordinates = coordinates
        self.temperature = temperature_sensor
        self.rain_sensor = rain_sensor
        self.params = 3

    ## need to be transformed to be distributions/sampling from historical readings
    def valid_temperature(self):
        return 1

    def valid_climate_reading(self):
        return 1

    def valid_rain_sample(self):
        return 1

    def verify_environmental_parameters(self):
        compiled_score = (self.valid_temperature() +
                          self.valid_rain_sample() +
                          self.valid_rain_sample())/self.params
        return compiled_score
