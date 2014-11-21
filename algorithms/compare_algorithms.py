__author__ = 'wolfenfeld'
import rucb
import sparring
import rcs
import balanced_doubler
import doubler
import improved_doubler
import improved_doubler_thompson_sampling
import savage
import btm
import forgetful_doubler
import forgetful_doubler_thompson_sampling
from data.real_data import DataSet
from data.bernoulli_arms import BernoulliArms
import matplotlib.pyplot as plt
import numpy as np

USE_REAL_DATA = True

horizon = 2**17

chosen_data_set_name = "MQ2007"

# The number of iterations for this test.
iterations = 7

n_arms = 10

if USE_REAL_DATA:
    # Setting the arms
    arms = DataSet(chosen_data_set_name)
    arms.set_data()
    means = arms.means[0:n_arms]

else:
    # Setting the arms
    means = np.random.random([n_arms])
    arms = BernoulliArms(means)

# The list of algorithm available fpr test: "RUCB", "RCS", "Sparring", "Balanced Doubler", "Doubler", "Improved Doubler"
# "Improved Doubler TS", "SAVAGE", "BTM", "Forgetful Doubler"
simulated_algorithms = ["Forgetful Doubler", "Sparring", "Forgetful Thompson Sampling Doubler"]

# Running the test simulation

if "BTM" in simulated_algorithms:
    btm_results = btm.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), btm_results, 'k--', label="BTM")
    print "Done with BTM"

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

if "SAVAGE" in simulated_algorithms:
    savage_results = savage.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), savage_results, 'r--', label="SAVAGE")
    print "Done with SAVAGE"

if "Forgetful Doubler" in simulated_algorithms:
    forgetful_doubler_results = forgetful_doubler.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), forgetful_doubler_results, 'r--', label="Forgetful Doubler")
    print "Done with Forgetful Doubler"

if "Forgetful Thompson Sampling Doubler" in simulated_algorithms:
    forgetful_doubler_thompson_sampling_results = \
        forgetful_doubler_thompson_sampling.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), forgetful_doubler_thompson_sampling_results, 'g--',
             label="Forgetful Thompson Sampling Doubler")
    print "Done with Forgetful Thompson Sampling Doubler"

plt.legend(loc='upper left', shadow=True)
plt.show()
