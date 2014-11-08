__author__ = 'wolfenfeld'
import rucb
import sparring
import rcs
import balanced_doubler
import doubler
import improved_doubler
import improved_doubler_thompson_sampling
from data.real_data import DataSet
from data.bernoulli_arms import BernoulliArms
import matplotlib.pyplot as plt
import numpy as np

USE_REAL_DATA = False

horizon = 2**16

chosen_data_set_name = "MQ2007"

# The number of iterations for this test.
iterations = 7

n_arms = 32

if USE_REAL_DATA:
    #Setting the arms
    arms = DataSet(chosen_data_set_name)
    arms.set_data()
    means = arms.means[0:n_arms]

else:
    #Setting the arms
    means = np.random.random([n_arms])
    arms = BernoulliArms(means)

# The list of algorithm available fpr test: "RUCB", "RCS", "Sparring", "Balanced Doubler", "Doubler", "Improved Doubler"
# "Improved Doubler TS"
simulated_algorithms = ["Improved Doubler", "Sparring", "Improved Doubler TS", "Doubler"]

# Running the test simulation

if "Balanced Doubler" in simulated_algorithms:
    balanced_doubler_results = balanced_doubler.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), balanced_doubler_results, 'r--', label="Balanced Doubler")
    print "Done with Balanced Doubler"

if "RUCB" in simulated_algorithms:
    rucb_results = rucb.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), rucb_results, 'm--', label="RUCB")
    print "Done with RUCB"

if "Sparring" in simulated_algorithms:
    sparring_results = sparring.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), sparring_results, 'k--', label="Sparring")
    print "Done with Sparring"

if "RCS" in simulated_algorithms:
    rcs_results = rcs.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), rcs_results, 'g--', label="RCS")
    print "Done with RCS"

if "Doubler" in simulated_algorithms:
    doubler_results = doubler.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), doubler_results, 'y--', label="Doubler")
    print "Done with Doubler"

if "Improved Doubler" in simulated_algorithms:
    improved_doubler_results = improved_doubler.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), improved_doubler_results, 'b--', label="Improved Doubler")
    print "Done with Improved Doubler"

if "Improved Doubler TS" in simulated_algorithms:
    improved_doubler_thompson_sampling_results = improved_doubler_thompson_sampling.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), improved_doubler_thompson_sampling_results, 'p--', label="Improved Doubler Turbo")
    print "Done with Improved Doubler Turbo"

plt.legend(loc='upper left', shadow=True)
plt.show()
