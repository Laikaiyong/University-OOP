import math
import matplotlib.pyplot as plt


class Gausian():
    """ Gaussian distribution class 

    Calculate and visualize Gaussian distribution for a specific values

    Attributes:
        mean (float): mean of the distribution
        stdev (float): standard deviation of distribution
        data_list (list of floats): Extract list of floats from data file
    """

    def __init__(self, prefix_mu=0, sigma=1):
        self.mean = prefix_mu
        self.stdev = sigma
        self.data = []

    def mean(self):
        """ The mean method that calculate mean of data set

        Args: None

        Returns: 
            mean of dataset (float)
        """

        average = 1.0 * sum(self.data)/len(self.data)
        self.mean = average
        return self.mean

    def stdev(self, sample=True):
        """ The stdev method that calculate standard deviation of data set

        Args: 
            sample (bool): check data represents sample or population

        Returns: 
            standard deviation of dataset (float)
        """

        if sample:
            n = len(self.data) - 1
        else:
            n = len(self.data)

        mean = self.mean

        sigma = 0

        for data in self.data:
            sigma += (data - mean) ** 2

        sigma = math.sqrt(sigma / n)

        self.stdev = sigma

        return self.stdev

    def read_data(self, file_name, sample=True):
        """The read_data function to extract data from .txt file"""
