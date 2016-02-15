__author__ = 'kafuinutakor'

from math import pow
import numpy as np
from scipy import stats


class CollocationDiscovery:
    """provides the functionality for collocation extraction; currently only supports chi square based strategy
    """
    def __init__(self):
        self.combined_freq = {}

    def merge_dicts(self, freq1, freq2):
        self.combined_freq = freq1.copy()
        self.combined_freq.update(freq2)

    def cum_dist_func(self, chi_square_stat):
        """wrapper for cumulative distribution function; returns p-value
        """
        # use 1 degree of freedom given df = (R-1) * (C-1); df  == (2-1) * (2-1) == 1
        p_value = 1.0 - float(stats.chi2.cdf(chi_square_stat, 1))
        return p_value

    def chi_square(self, collocation):
        """computes 2 X 2 table and returns chi square statistic
        """
        terms = collocation.split()

        # compute 2 X 2 table here
        array = [[], []]
        array[0] = [float(self.combined_freq[collocation]), float(self.combined_freq[terms[1]] - self.combined_freq[collocation])]
        array[1] = [float(self.combined_freq[terms[0]]) - float(self.combined_freq[collocation]),
                    float(len(self.combined_freq) - ((2.0 * float(self.combined_freq[collocation])) +
                                                     float(self.combined_freq[terms[0]]) + float(self.combined_freq[terms[1]])))]

        # convert to nd array
        array = np.array(array)

        # compute chi square statistic
        chi_square = (float(len(self.combined_freq)) * pow(((array[0, 0] * array[1, 1]) - (array[0, 1] * array[1, 0])), 2)) /\
                    ((array[0, 0] + array[0, 1]) * (array[0, 0] + array[1, 0]) * (array[0, 1] + array[1, 1]) *
                     (array[1, 0] + array[1, 1]))
        return chi_square

    def evaluate(self, collocation, p_value_thresh=.1):
        """runs chi square test on given collocation
        """
        cs = self.chi_square(collocation)
        p_value = self.cum_dist_func(cs)

        if p_value <= p_value_thresh:
            return str(cs), str(p_value), str(self.combined_freq[collocation])



