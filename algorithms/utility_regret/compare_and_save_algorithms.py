__author__ = 'wolfenfeld'

from algorithms.utility_regret import doubler, sparring_thompson, improved_doubler_thompson_sampling, sparring, \
    forgetful_doubler, balanced_doubler, btm, improved_doubler, savage, forgetful_doubler_thompson_sampling, rcs, rucb, \
    sparring_thompson_turbo
from data.real_data import DataSet
from data.bernoulli_arms import BernoulliArms
import numpy as np
import itertools

USE_REAL_DATA = True

chosen_data_set_name = "MQ2007"

# The number of iterations for this test.
iterations = 20
horizon = 2**17
n_arms = 8

# The list of algorithm available fpr test:
# "RUCB", "RCS", "Sparring", "Balanced Doubler", "Doubler", "Improved Doubler"
# "Improved Doubler TS", "SAVAGE", "BTM", "Forgetful Doubler", "Sparring TS"

simulated_algorithms = [
    "RUCB", "RCS",
    "Sparring",
    "Balanced Doubler",
    "Doubler", "Improved Doubler",
    "Improved Doubler TS", "SAVAGE",
    "BTM",
    "Forgetful Doubler",
    "Sparring TS",
    "Sparring TS Turbo"
]

# "One Strong Arm", "Linear List", "Close Arms"

# simulated_data_sets = ["Linear List", "Close Arms", "One Strong Arm", "Random"]
simulated_data_sets = [1]

# Running the test simulation
for algorithm, data_sets in itertools.product(simulated_algorithms, simulated_data_sets):

    if USE_REAL_DATA:
        data_type = "Real_data"
        arms = DataSet(chosen_data_set_name)
        arms.set_data()
        means = arms.means[0:n_arms]

    else:
        # Setting the arms (One Strong Arm, Linear List, Close Arms)
        if data_sets == "One Strong Arm":
            means = [1]+list(np.linspace(0, 0.5, n_arms-1))
        elif data_sets == "Linear List":
            means = np.linspace(0, 1, n_arms)
        elif data_sets == "Close Arms":
            means = list(np.linspace(1, 0.99, 3)) + list(np.linspace(0.4, 0.5, n_arms-3))
        else:
            means = np.random.random([n_arms])
        arms = BernoulliArms(means)

        data_type = "Synthetic_data_{0}".format(data_sets)

    if algorithm == "BTM" and not USE_REAL_DATA:
        btm.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)
        print "Done with BTM"

    if algorithm == "Sparring TS":
        sparring_thompson.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)
        print "Done with Sparring TS"

    elif algorithm == "Sparring TS Turbo":
        sparring_thompson_turbo.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)
        print "Done with Sparring TS Turbo"

    elif algorithm == "Balanced Doubler":
        balanced_doubler.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)
        print "Done with Balanced Doubler"

    elif algorithm == "RUCB":
        rucb.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)
        print "Done with RUCB"

    elif algorithm == "Sparring":
        sparring.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)
        print "Done with Sparring"

    elif algorithm == "RCS":
        rcs.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)
        print "Done with RCS"

    elif algorithm == "Doubler":
        doubler.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)
        print "Done with Doubler"

    elif algorithm == "Improved Doubler":
        improved_doubler.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)
        print "Done with Improved Doubler"

    elif algorithm == "Improved Doubler TS":
        improved_doubler_thompson_sampling.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)

        print "Done with Improved Doubler TS"

    elif algorithm == "SAVAGE":
        savage.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)
        print "Done with SAVAGE"

    elif algorithm == "Forgetful Doubler":
        forgetful_doubler.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)
        print "Done with Forgetful Doubler"

    elif algorithm == "Forgetful Thompson Sampling Doubler":
        forgetful_doubler_thompson_sampling.run_several_iterations_and_save_results(
            algorithm, iterations, arms, n_arms, horizon, means, data_type)
        print "Done with Forgetful Thompson Sampling Doubler"
