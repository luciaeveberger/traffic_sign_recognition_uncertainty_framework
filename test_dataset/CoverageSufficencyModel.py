import sys
sys.path.append("..")
import TargetApplicationScope

## defines the parameter ranges we should be looking for
t = TargetApplicationScope.TargetApplicationScope()
lookup_table = t.__dict__
appropriate_test_cases = 5


def validate_all_parameters(data_set, lookup_table):
    temp_params = lookup_table['temperature']


    print(data_set)
    return

validate_all_parameters(data_set="hello", lookup_table=lookup_table)

# def validate_range_based_input():
#         """range of values for scope factors
#         (e.g., comparing min/max temperature values of
#         target application scope (TAS) with min/max values of TD) """
#
#         # + temperatureRange(temperature, min_temp, max_temp):
#         # +yearRange(year, timestamp)
#         # +velocityRange(min_velocity, max_velocity)
#         # +rainSensorRange(min_rain, max_rain)
#         ##
#
#     return

    # def validate_distribution_input(self):
    #
    #     """
    #      density of cases in the TD to
    #       detect potential gaps (e.g., covering each
    #       area larger than 4km^2, each hour of a day …
    #       with at least x cases).
    #     """
    #     # + locationDensity(coordinates, max_coordinate, min_coordinate, test_case_based)
    #     # + temperatureDensity(temperature, min_temp, max_temp):
    #     # +timeDensity(timestamp.hour, test_cases)
    # return


