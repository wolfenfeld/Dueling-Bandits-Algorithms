import numpy as np
from black_boxes.ucb1 import *
import random


def time_interval(p):
    """ time_interval() - This function returns the time interval T_p. """
    return [value for value in range(int(2**(p-1)), int(2**p))]


def observe_b_t(left_reward, right_reward):
    """ observe_b_t() - This function returns b_t."""

    if left_reward > right_reward:
        return 0
    elif right_reward > left_reward:
        return 1
    else:
        return random.choice([1, 0])


def update_regret(current_regret, cumulative_regret, t):

    # Assigning the cumulative regret and rewards
    if t == 1:

        cumulative_regret[t] = current_regret[t]
    else:

        cumulative_regret[t] = current_regret[t] + cumulative_regret[t-1]


def calculate_f_p(f_p, t_interval, b, p):
    """ calculate_f_p() - This function returns the f_p factor according to b in the t_interval. """

    # The relevant b values of the t_interval
    b_p = [b[value] for value in t_interval]

    # The factor that will be added to last epoch f_p
    factor = float(sum(b_p))/((2**(p-1))+.0)

    return f_p + factor - 0.5


def choose_from_probability_vector(probability_vector):
    """ choose_from_probability_vector() - This function receives a probability vector and returns the chosen index."""
    r = random.random()
    index = 0

    while r >= 0 and index < len(probability_vector):

        r -= probability_vector[index]

        index += 1

    return index - 1


def construct_probability_vector(histogram):
    """ construct_probability_vector() - This function returns the normalized histogram."""

    return histogram/(sum(histogram)+.0)


def run_doubler_algorithm(arms, log_horizon):
    """ run_doubler_algorithm() - This function runs the doubler / improved doubler algorithm and returns the
        cumulative regret. """

    n_arms = arms.n_arms

    my_left_set = np.ones(n_arms, dtype=bool)

    # Assigning the black-boxes with the UCB 1 algorithm
    right_black_box = UCB1([], [])

    # Initializing the black-boxes.
    right_black_box.initialize(n_arms)

    # The b observation
    observed_b = np.zeros(2**log_horizon)

    # Regret and reward tracking
    regret = np.zeros(2**log_horizon)
    cumulative_regret = np.zeros(2**log_horizon)

    # The f factor
    f = np.zeros(log_horizon+2)

    # The Doubler algorithm :
    for current_p in range(0, log_horizon+1):

        # The arms used in this current round
        arms_histogram = np.zeros(n_arms)

        # This round time interval.
        current_time_interval = time_interval(current_p)

        # The Improved Doubler algorithm.

        for t in current_time_interval:

            # Choosing the left arm from the multi-set L.
            left_arm = choose_from_probability_vector(construct_probability_vector(my_left_set))

            # Choosing an arm using the right black box.
            right_arm = right_black_box.select_arm()

            # Updating the histogram for the next time interval
            arms_histogram[right_arm] += 1

            # Choosing the arms
            [current_left_reward, current_right_reward] = arms.draw(left_arm, right_arm)

            # Observing b_t
            observed_b[t] = observe_b_t(current_left_reward, current_right_reward)

            # Updating the right black-box with b_t and f_p
            right_black_box.update(right_arm, observed_b[t] + f[current_p])

            # Assigning the regret
            regret[t] = arms.get_regret(left_arm, right_arm)

            update_regret(regret, cumulative_regret, t)

        # Calculating the f_p
        f[current_p+1] = calculate_f_p(f[current_p], current_time_interval, observed_b, current_p)

        # Updating the left set of arms that can be used in the next round.
        my_left_set = arms_histogram

    return cumulative_regret


def run_several_iterations(iterations, arms, horizon):
    """ run_several_iterations() - This function runs several iterations of the Doubler/Improved Doubler algorithm. """

    # Initializing the  results vector
    results = np.zeros(horizon)

    # log(horizon)
    log_horizon = int(math.log(horizon, 2))

    for iteration in range(iterations):

        # The current cumulative regret.
        results += run_doubler_algorithm(arms, log_horizon=log_horizon)

    # Returning the average cumulative regret.
    return results/(iterations + .0)

def run_several_iterations_and_save_results(algorithm, iterations, arms, n_arms, horizon, data_type):
    """ test_several_iterations() - This function runs several iterations of the Sparring algorithm. """

    # Initializing the results vector.
    result = np.zeros([horizon, iterations])
    log_horizon = int(math.log(horizon, 2))
    file_name = "{0}_{1}_arms_{2}_horizon_{3}".format(algorithm, data_type, n_arms, horizon)

    for iteration in range(iterations):

        # The current cumulative regret.
        result[:, iteration] = run_doubler_algorithm(arms, log_horizon)

    np.save(file_name, result)