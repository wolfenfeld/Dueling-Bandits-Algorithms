import math
from black_boxes.thompson_sampling import *
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
    right_black_box = UCB_TS([], [], [])

    # Initializing the black-box.
    right_black_box.initialize(n_arms)

    # The b observation
    observed_b = np.zeros(2**log_horizon)

    # Regret  tracking
    regret = np.zeros(2**log_horizon)
    cumulative_regret = np.zeros(2**log_horizon)

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
            right_black_box.update(right_arm, observed_b[t])

            # Assigning the regret
            regret[t] = arms.get_regret(left_arm, right_arm)

            update_regret(regret, cumulative_regret, t)

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