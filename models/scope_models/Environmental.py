class Environmental:
    def __init__(self, timestamp, coordinates, temperature, rain_sensor_reading):
        self.timestamp = timestamp
        self.coordinates = coordinates
        self.temperature = temperature
        self.rain_sensor_reading = rain_sensor_reading

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
