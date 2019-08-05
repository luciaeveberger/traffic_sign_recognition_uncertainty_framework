#from environmental import WeatherSampler
import TargetApplicationScope

t = TargetApplicationScope.TargetApplicationScope()
environmental_stats = t.get_environmental_stat()
air_temp = environmental_stats['air_temp']
precipitation = environmental_stats['precip']
p_value = 0.001

class Environmental:
    # may want to add other parameters
    def __init__(self,
                 timestamp,
                 month_stamp,
                 coordinates,
                 temperature_sensor,
                 rain_sensor
                 ):
        
        self.timestamp = timestamp
        self.month_date = month_stamp
        self.coordinates = coordinates
        self.temperature = temperature_sensor
        self.rain_sensor = rain_sensor
        self.params = 2


    ## need to be transformed to be distributions/sampling from historical readings
    def validate_monthly_air_temp(self):
        """ checks the value is larger than p_value per month """
        subset = air_temp.get(str(self.month_date))
        temp = int(self.temperature)
        probability = 0
        for val in subset:
            if val[0] == temp:
                probability = val[1]
                print(probability)
        if probability > p_value:
            return 1
        return 0

    def valid_rain_sample(self):
        subset = precipitation.get(str(self.month_date))
        precip_sample = int(self.rain_sensor)
        probability = 0
        for val in subset:
            if val[0] == precip_sample:
                probability = val[1]
                print(probability)
        if probability > p_value:
            return 1
        return 0

    def verify_environmental_parameters(self):
        compiled_score = ((self.validate_monthly_air_temp() +
                          self.valid_rain_sample()) /self.params)
        return compiled_score
