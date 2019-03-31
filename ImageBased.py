## import global SignTypes list

class ImageBased():
    def __init__(self, sign_type, driving_direction):
        self.sign_type = sign_type
        self.driving_direction = driving_direction
        self.parameters = 2

    def verify_sign_type(self, sign_type):
        return 1

    def verify_driving_direction(self, driving_direction):
        return 1

    def verify_image_based_parameters(self):
        """ returns final geographical score """
        factor_eval = 100/self.parameters
        return (factor_eval * (self.verify_sign_type()
                               + self.verify_driving_direction()
                               )/100)
