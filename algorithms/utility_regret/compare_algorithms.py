from algorithms.utility_regret import doubler, sparring_thompson, improved_doubler_thompson_sampling, sparring, \
    forgetful_doubler, balanced_doubler, btm, improved_doubler, savage, forgetful_doubler_thompson_sampling, rcs, rucb

__author__ = 'wolfenfeld'
from data.real_data import DataSet
from data.bernoulli_arms import BernoulliArms
import matplotlib.pyplot as plt
import numpy as np

USE_REAL_DATA = False

horizon = 2**20

chosen_data_set_name = "MQ2007"

# The number of iterations for this test.
iterations = 2

n_arms = 16

if USE_REAL_DATA:
    # Setting the arms
    arms = DataSet(chosen_data_set_name)
    arms.set_data()
    means = arms.means[0:n_arms]

else:
    # Setting the arms
    means = np.random.random([n_arms])
    arms = BernoulliArms(means)

# The list of algorithm available fpr test:
# "RUCB", "RCS", "Sparring", "Balanced Doubler", "Doubler", "Improved Doubler"
# "Improved Doubler TS", "SAVAGE", "BTM", "Forgetful Doubler", "Sparring TS"

simulated_algorithms = ["Sparring", "Balanced Doubler", "Improved Doubler"]
                        # "Improved Doubler TS", "BTM", "Sparring TS"]

plot_line_style = ['b--', 'g--', 'r--', 'c--', 'm--', 'k--', 'b-.', 'g-.', 'r-.', 'c-.', 'm-.', 'k-.']
number_of_plots = 0

# Running the test simulation

if ("BTM" in simulated_algorithms) and not USE_REAL_DATA:
    btm_results = btm.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), btm_results, plot_line_style[number_of_plots], label="BTM")
    number_of_plots += 1
    print "Done with BTM"

if "Sparring TS" in simulated_algorithms:
    sparring_thompson_results = sparring_thompson.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), sparring_thompson_results, plot_line_style[number_of_plots], label="Sparring TS")
    number_of_plots += 1
    print "Done with Sparring TS"

if "Balanced Doubler" in simulated_algorithms:
    balanced_doubler_results = balanced_doubler.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), balanced_doubler_results, plot_line_style[number_of_plots], label="Balanced Doubler")
    number_of_plots += 1
    print "Done with Balanced Doubler"

if "RUCB" in simulated_algorithms:
    rucb_results = rucb.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), rucb_results, plot_line_style[number_of_plots], label="RUCB")
    number_of_plots += 1
    print "Done with RUCB"

if "Sparring" in simulated_algorithms:
    sparring_results = sparring.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), sparring_results, plot_line_style[number_of_plots], label="Sparring")
    number_of_plots += 1
    print "Done with Sparring"

if "RCS" in simulated_algorithms:
    rcs_results = rcs.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), rcs_results, plot_line_style[number_of_plots], label="RCS")
    number_of_plots += 1
    print "Done with RCS"

if "Doubler" in simulated_algorithms:
    doubler_results = doubler.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), doubler_results, plot_line_style[number_of_plots], label="Doubler")
    number_of_plots += 1
    print "Done with Doubler"

if "Improved Doubler" in simulated_algorithms:
    improved_doubler_results = improved_doubler.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), improved_doubler_results, plot_line_style[number_of_plots], label="Improved Doubler")
    number_of_plots += 1
    print "Done with Improved Doubler"

if "Improved Doubler TS" in simulated_algorithms:
    improved_doubler_thompson_sampling_results = \
        improved_doubler_thompson_sampling.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), improved_doubler_thompson_sampling_results, plot_line_style[number_of_plots],
             label="Un-forgetful Doubler TS")
    number_of_plots += 1
    print "Done with Improved Doubler TS"

if "SAVAGE" in simulated_algorithms:
    savage_results = savage.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), savage_results, plot_line_style[number_of_plots], label="SAVAGE")
    number_of_plots += 1
    print "Done with SAVAGE"

if "Forgetful Doubler" in simulated_algorithms:
    forgetful_doubler_results = forgetful_doubler.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), forgetful_doubler_results, plot_line_style[number_of_plots], label="Forgetful Doubler")
    number_of_plots += 1
    print "Done with Forgetful Doubler"

if "Forgetful Thompson Sampling Doubler" in simulated_algorithms:
    forgetful_doubler_thompson_sampling_results = \
        forgetful_doubler_thompson_sampling.run_several_iterations(iterations, arms, n_arms, horizon, means)
    plt.plot(range(horizon), forgetful_doubler_thompson_sampling_results, plot_line_style[number_of_plots],
             label="Forgetful Thompson Sampling Doubler")
    number_of_plots += 1
    print "Done with Forgetful Thompson Sampling Doubler"

plt.legend(loc='upper left', shadow=True)
plt.show()
