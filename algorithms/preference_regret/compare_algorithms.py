from algorithms.preference_regret import doubler, sparring_thompson, improved_doubler_thompson_sampling, sparring, \
    forgetful_doubler, improved_doubler, savage, forgetful_doubler_thompson_sampling, rcs, rucb
from data.preference_matrices.preference_matrix import PreferenceMatrix

import matplotlib.pyplot as plt

# The number of iterations for this test.
iterations = 1


arms = PreferenceMatrix()
arms.init('/home/wolfenfeld/Studies/Dueling-Bandits-Algorithms/data/PMat.npy')

horizon = 2**20

# The list of algorithm available fpr test:
# "RUCB", "RCS", "Sparring", "Doubler", "Improved Doubler"
# "Improved Doubler TS", "SAVAGE", "BTM", "Forgetful Doubler", "Sparring TS","Forgetful Thompson Sampling Doubler"

simulated_algorithms = ["Sparring TS", "RUCB"]

plot_line_style = ['b--', 'g--', 'r--', 'c--', 'm--', 'k--', 'b-.', 'g-.', 'r-.', 'c-.', 'm-.', 'k-.']
number_of_plots = 0

# Running the test simulation

if "Sparring TS" in simulated_algorithms:
    sparring_thompson_results = sparring_thompson.run_several_iterations(iterations, arms, horizon)
    plt.plot(range(horizon), sparring_thompson_results, plot_line_style[number_of_plots], label="Sparring TS")
    number_of_plots += 1
    print "Done with Sparring TS"

if "RUCB" in simulated_algorithms:
    rucb_results = rucb.run_several_iterations(iterations, arms, horizon)
    plt.plot(range(horizon), rucb_results, plot_line_style[number_of_plots], label="RUCB")
    number_of_plots += 1
    print "Done with RUCB"

if "Sparring" in simulated_algorithms:
    sparring_results = sparring.run_several_iterations(iterations, arms, horizon)
    plt.plot(range(horizon), sparring_results, plot_line_style[number_of_plots], label="Sparring")
    number_of_plots += 1
    print "Done with Sparring"

if "RCS" in simulated_algorithms:
    rcs_results = rcs.run_several_iterations(iterations, arms, horizon)
    plt.plot(range(horizon), rcs_results, plot_line_style[number_of_plots], label="RCS")
    number_of_plots += 1
    print "Done with RCS"

if "Doubler" in simulated_algorithms:
    doubler_results = doubler.run_several_iterations(iterations, arms, horizon)
    plt.plot(range(horizon), doubler_results, plot_line_style[number_of_plots], label="Doubler")
    number_of_plots += 1
    print "Done with Doubler"

if "Improved Doubler" in simulated_algorithms:
    improved_doubler_results = improved_doubler.run_several_iterations(iterations, arms, horizon)
    plt.plot(range(horizon), improved_doubler_results, plot_line_style[number_of_plots], label="Improved Doubler")
    number_of_plots += 1
    print "Done with Improved Doubler"

if "Improved Doubler TS" in simulated_algorithms:
    improved_doubler_thompson_sampling_results = \
        improved_doubler_thompson_sampling.run_several_iterations(iterations, arms, horizon)
    plt.plot(range(horizon), improved_doubler_thompson_sampling_results, plot_line_style[number_of_plots],
             label="Improved Doubler TS")
    number_of_plots += 1
    print "Done with Improved Doubler TS"

if "SAVAGE" in simulated_algorithms:
    savage_results = savage.run_several_iterations(iterations, arms, horizon)
    plt.plot(range(horizon), savage_results, plot_line_style[number_of_plots], label="SAVAGE")
    number_of_plots += 1
    print "Done with SAVAGE"

if "Forgetful Doubler" in simulated_algorithms:
    forgetful_doubler_results = forgetful_doubler.run_several_iterations(iterations, arms, horizon)
    plt.plot(range(horizon), forgetful_doubler_results, plot_line_style[number_of_plots], label="Forgetful Doubler")
    number_of_plots += 1
    print "Done with Forgetful Doubler"

if "Forgetful Thompson Sampling Doubler" in simulated_algorithms:
    forgetful_doubler_thompson_sampling_results = \
        forgetful_doubler_thompson_sampling.run_several_iterations(iterations, arms, horizon)
    plt.plot(range(horizon), forgetful_doubler_thompson_sampling_results, plot_line_style[number_of_plots],
             label="Forgetful Thompson Sampling Doubler")
    number_of_plots += 1
    print "Done with Forgetful Thompson Sampling Doubler"

plt.legend(loc='upper left', shadow=True)
plt.show()
