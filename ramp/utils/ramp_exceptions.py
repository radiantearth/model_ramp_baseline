
# base class for all custom exceptions in Ramp code
class RampError(Exception):
    pass


# thrown when gdal.Open fails
class GdalReadError(RampError):
    pass
