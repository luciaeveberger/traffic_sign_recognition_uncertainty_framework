## import global SignTypes list
import TargetApplicationScope

t = TargetApplicationScope.TargetApplicationScope()
available_sign_types = t.get_set_of_sign()
country_driving_direction = t.get_driving_direction()


class ImageBased:
    def __init__(self, sign_type, driving_direction):
        self.sign_type = sign_type
        self.driving_direction = driving_direction
        self.parameters = 2

    def verify_sign_type(self):
        """
        if in data-set
        :return: true or false
        """
        if self.sign_type in available_sign_types:
            return 1
        return 0

    def verify_driving_direction(self):
        """

        :return: true or false
        """
        if self.driving_direction == country_driving_direction:
            return 1
        return 0

    def verify_image_based_parameters(self):
        """ returns final geographical score """
        factor_eval = 100/self.parameters
        return (factor_eval * (self.verify_sign_type()
                               + self.verify_driving_direction()
                               )/100)
