#from environmental import WeatherSampler
import TargetApplicationScope

t = TargetApplicationScope.TargetApplicationScope()
environmental_stats = t.get_environmental_stat()
air_temp = environmental_stats['air_temp']
p_value = 0.05

class Environmental:
    # need to see if we need to check the other params
    def __init__(self,
                 timestamp,
                 month_stamp,
                 coordinates,
                 temperature_sensor,
                 rain_sensor):
        self.timestamp = timestamp
        self.month_date = month_stamp
        self.coordinates = coordinates
        self.temperature = temperature_sensor
        self.rain_sensor = rain_sensor
        self.params = 3

    ## need to be transformed to be distributions/sampling from historical readings
    def validate_monthly_air_temp(self):
        """ checks the value is larger than p_value """
        subset = air_temp.get(str(self.month_date))
        temp = int(self.temperature)

        probability = 0
        for val in subset:
            if val[0] == temp:
                probability = val[1]
                print(probability)
        print("EVALUATING {} for month {}".format(temp, self.month_date))
        print("Calculated {}".format(probability))
        print("Compare with a value {}".format(p_value))
        if probability > p_value:
            return 1
        return 0

    def valid_climate_reading(self):
        return 1

    def valid_rain_sample(self):
        return 1

    def verify_environmental_parameters(self):
        #print("PROBABILITY {}".format(self.validate_monthly_air_temp()))
        compiled_score = (self.validate_monthly_air_temp() +
                          self.valid_rain_sample() +
                          self.valid_rain_sample())/self.params
        return compiled_score

#e = Environmental()
