import numpy as np
import random
from black_boxes.thompson_sampling import *


def observe_b_t(left_reward, right_reward):
    """ observe_b_t() - This function returns b_t."""

    random_variable = random.random()

    if random_variable >= (left_reward - right_reward + 1.0)/2:
        return 1
    else:
        return 0


def run_sparring_algorithm(arms, n_arms, horizon, means):
    """ run_sparring_algorithm() - This function runs the Sparring algorithm. """

    # Assigning the black-boxes with the UCB 1 algorithm
    left_black_box = UCB_TS([], [], [])
    right_black_box = UCB_TS([], [], [])

    # Initializing the black-boxes.
    left_black_box.initialize(n_arms)
    right_black_box.initialize(n_arms)

    # Initializing rewards and regrets
    average_reward = np.zeros(horizon)

    regret = np.zeros(horizon)

    cumulative_average_reward = np.zeros(horizon)

    cumulative_regret = np.zeros(horizon)

    for t in range(horizon):

        # Using the black-boxes to select the arms
        left_arm = left_black_box.select_arm(t)
        right_arm = right_black_box.select_arm(t)

        # Acquiring the rewards
        [left_reward, right_reward] = arms.draw(left_arm, right_arm)

        b = observe_b_t(left_reward, right_reward)
        b_not = 1 - b

        # Updating the black-boxes
        left_black_box.update(left_arm, b_not)
        right_black_box.update(right_arm, b)

        # Assigning the average reward.
        average_reward[t] = float(right_reward + left_reward) / 2

        # Assigning the regret
        regret[t] = max(means) - average_reward[t]

        # Assigning the cumulative regret and rewards
        if t == 1:
            cumulative_average_reward[t] = average_reward[t]

            cumulative_regret[t] = regret[t]
        else:
            cumulative_average_reward[t] = average_reward[t] + cumulative_average_reward[t-1]

            cumulative_regret[t] = regret[t] + cumulative_regret[t-1]

    # Returning the average regret.
    return cumulative_regret


def run_several_iterations(iterations, arms, n_arms, horizon, means):
    """ test_several_iterations() - This function runs several iterations of the Sparring algorithm. """

    # Initializing the results vector.
    results = np.zeros(horizon)
    result = np.zeros([horizon, iterations])
    mean_error = np.zeros(horizon)
    for iteration in range(iterations):

        # The current cumulative regret.
        result[:,iteration] = run_sparring_algorithm(arms, n_arms, horizon, means)
        results += result[:,iteration]

    # Returning the average cumulative regret.
    mean_results = results/(iterations + .0)
    for iteration in range(iterations):
        # mean_error += abs(mean_results - result[:, iteration])

        mean_error += np.power(mean_results - result[:, iteration], 2)

    # mean_error += np.sqrt(abs(np.power(mean_results, 2) - np.power(result[:, iteration], 2)))

    return mean_results, np.sqrt(mean_error/(iterations + .0))

def run_several_iterations_and_save_results(algorithm, iterations, arms, n_arms, horizon, means, data_type):
    """ test_several_iterations() - This function runs several iterations of the Sparring algorithm. """

    # Initializing the results vector.
    result = np.zeros([horizon, iterations])

    file_name = "{0}_{1}_arms_{2}_horizon_{3}".format(algorithm, data_type, n_arms, horizon)

    for iteration in range(iterations):

        # The current cumulative regret.
        result[:, iteration] = run_sparring_algorithm(arms, n_arms, horizon, means)

    np.save(file_name, result)
