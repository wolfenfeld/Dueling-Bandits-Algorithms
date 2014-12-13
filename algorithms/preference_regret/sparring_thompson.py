import numpy as np
import random
from black_boxes.thompson_sampling import *


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


def run_sparring_algorithm(arms, horizon):
    """ run_sparring_algorithm() - This function runs the Sparring algorithm. """

    # Assigning the black-boxes with the UCB 1 algorithm
    left_black_box = UCB_TS([], [], [])
    right_black_box = UCB_TS([], [], [])

    n_arms = arms.n_arms

    # Initializing the black-boxes.
    left_black_box.initialize(n_arms)
    right_black_box.initialize(n_arms)

    # Initializing regrets

    regret = np.zeros(horizon)

    cumulative_regret = np.zeros(horizon)

    for t in range(horizon):

        # Using the black-boxes to select the arms
        left_arm = left_black_box.select_arm()
        right_arm = right_black_box.select_arm()

        # Acquiring the rewards
        [left_reward, right_reward] = arms.draw(left_arm, right_arm)

        b = observe_b_t(left_reward, right_reward)
        b_not = 1 - b

        # Updating the black-boxes
        left_black_box.update(left_arm, b_not)
        right_black_box.update(right_arm, b)

        # Assigning the regret
        regret[t] = arms.get_regret(left_arm, right_arm)

        update_regret(regret, cumulative_regret, t)

    # Returning the average regret.
    return cumulative_regret


def run_several_iterations(iterations, arms, horizon):
    """ test_several_iterations() - This function runs several iterations of the Sparring algorithm. """

    # Initializing the results vector.
    results = np.zeros(horizon)

    for iteration in range(iterations):

        # The current cumulative regret.
        results += run_sparring_algorithm(arms, horizon)

    # Returning the average cumulative regret.
    return results/(iterations + .0)