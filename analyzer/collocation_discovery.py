__author__ = 'kafuinutakor'

from scipy import stats
import numpy as np
from math import pow


# collocation discoverer
class CollocationDiscovery:
    def __init__(self):
        self.combined_freq = {}

    def dict_merger(self, freq1, freq2):
        """
        this method merges dicts to use as a reference in the computation below
        """
        self.combined_freq = freq1.copy()
        self.combined_freq.update(freq2)

    def cum_dist_func(self, chiSquare):
        """
        wrapper for cumulative distribution function
        """
        # use 1 degree of freedom given df = (R-1) * (C-1); df  == (2-1) * (2-1) == 1
        cs = 1.0 - float(stats.chi2.cdf(chiSquare, 1))
        #print stats.chi2.cdf(chiSquare, len(self.combined_freq) - 1)
        return cs

    def chi_square(self, collocation, freq):
        """
        computes 2 X 2 table and chi square statistic
        """
        freq = self.combined_freq
        terms = collocation.split()
        # compute 2 X 2 table here
        array = [[], []]
        array[0] = [float(freq[collocation]), float(freq[terms[1]] - freq[collocation])]
        # in element 2's computation adjust for collaction frequency with a  factor of 2; simply add 8 to each before s
        # before subtracting from n
        array[1] = [float(freq[terms[0]]) - float(freq[collocation]),
                    float(len(freq) - ((2.0 * float(freq[collocation])) + float(freq[terms[0]]) + float(freq[terms[1]])))]
        # numpy nd array cast
        array = np.array(array)
        # compute chi square statistic
        chi_square = (float(len(freq)) * pow(((array[0, 0] * array[1, 1]) - (array[0, 1] * array[1, 0])), 2)) /\
                    ((array[0, 0] + array[0, 1]) * (array[0, 0] + array[1, 0]) * (array[0, 1] + array[1, 1]) * (array[1, 0] + array[1, 1]))
        return chi_square

    def evaluate(self, collocation):
        """
        runs chi square test on given collocation
        """
        cs = self.chi_square(collocation, self.combined_freq)
        p_value = self.cum_dist_func(cs)
        #change this either to a parameter for the method or remove all together
        if p_value <= .1:
            return str(cs), str(p_value), str(self.combined_freq[collocation])
        else:
            return None


