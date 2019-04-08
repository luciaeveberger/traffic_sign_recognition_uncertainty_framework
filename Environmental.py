class Environmental:
    # need to see if we need to check the other params
    def __init__(self,
                 timestamp,
                 lat,
                 long
                 temperature_sensor,
                 rain_sensor
                 #temperature_forecast,
                 #rain_forecast
                  ):
        self.timestamp = timestamp
        self.coordinates = coordinates
        self.temperature = temperature_sensor
        self.rain_sensor = rain_sensor
        # self.temperature_forecast = self.temperature_forecast
        # self.rain_forecast = self.rain_forecast

    ## need to be transformed to be distributions/sampling from historical readings

    def validTemperature(self, timestamp, coordinates, temperature):
        return True

    def validClimateReading(self):
        return True

    def validRainReading(self, timestamp, coordinates, rain_sensor_reading):
        return True

    def validateMeasures(self):
        temperature_score = self.validTemperature()
        climate_score = self.validClimateReading()
        rain_score = self.validRainReading()
        compiled_score = temperature_score + climate_score + rain_score
        return compiled_score
