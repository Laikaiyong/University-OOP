from .Distribution import Distribution
from collections import Counter


class General(Distribution):
    """ General distribution class for calculating mode and median

    Attributes:
            mode (float/int) representing the mode value of the distribution
            median (float/int/str) representing the standard deviation of the distribution
    """

    def __init__(self, mode, median):
        self.mode = mode
        self.median = median

    def mode(self):
        """Function to calculate the mode of the data set.

        Args: 
                None

        Returns: 
                float / int / string(no mode): mode of the data set

        """
        data = Counter(self.data)
        get_mode = dict(data)
        mode = [k for k, v in get_mode.items() if v == max(list(data.values()))]

        if len(mode) == len(self.data):
            self.mode = "No mode found"
        else:
            self.mode = mode

        return self.mode

    def median(self):
        """Function to calculate the median of the data set.

        Args: 
                None

        Returns: 
                float / int: median of the data set

        """
        data_list = self.data
        data_list.sort()

        if len(self.data) % 2 == 0:
            median_one = data_list[len(self.data)//2]
            median_two = data_list[len(self.data)//2 - 1]
            self.median = (median_one + median_two)/2
        else:
            self.median = data_list[len(self.data)//2]

        return self.median
