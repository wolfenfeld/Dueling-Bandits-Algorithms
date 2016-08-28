import numpy as np
from arms.bernoulli import *
import math


def update_regret(current_regret, cumulative_regret, t):

    # Assigning the cumulative regret and rewards
    if t == 1:

        cumulative_regret[t] = current_regret[t]
    else:

        cumulative_regret[t] = current_regret[t] + cumulative_regret[t-1]


class RUCB():
    """ The RUCB object. """

    def __init__(self, n_arms, alpha):
        """__init__() - The constructor of the RUCB object. """

        # The "bonus"
        self.alpha = alpha

        # The utility matrix.
        self.utility = np.zeros([n_arms, n_arms])

        # The wins matrix - counts the number of wins for each arms-pair.
        self.wins = np.zeros([n_arms, n_arms])

        # The "Best" vector.
        self.b_vector = np.zeros(n_arms, dtype=bool)

        # The "Champions" vector.
        self.c_vector = np.zeros(n_arms, dtype=bool)

        return

    def initialize(self):
        """initialize() - This function initializes the utility matrix main axis to 1/2."""

        # The number of arms.
        n_arms = len(self.wins)

        # Assigning 1/2 to all the elements in the main axis.
        for arm in range(n_arms):
            self.utility[arm, arm] = 0.5

        return

    def select_arms(self, t):
        """select_arms() - This function returns the selected arms according to the RUCB algorithm. """

        # Updating the utility matrix
        self.update_utility_matrix(t)

        # Updating the c_vector
        self.create_champion_set()

        # Choosing the left arm.
        chosen_left_arm = self.chose_left_arm()

        # Choosing the right arm.
        chosen_right_arm = self.chose_right_arm(chosen_left_arm)

        # Returning arms index.
        return [chosen_left_arm, chosen_right_arm]

    def update_utility_matrix(self, t):
        """ update_utility_matrix() - This function updates the utility matrix. """

        # Number of arms
        n_arms = len(self.wins)

        # Updating the utility for this round according to the wins of all the arms.
        # For each left arms-pair
        for left_arm in range(n_arms):

            for right_arm in range(n_arms):

                # Calculating the denominator.
                denominator = float(self.wins[left_arm, right_arm] + self.wins.T[left_arm, right_arm])

                # If the denominator is 0.
                if denominator == 0:

                    if self.wins[left_arm, right_arm] == 0:
                        exploitation = 0
                    else:
                        exploitation = 1

                    if t == 1:
                        exploration = 0
                    else:
                        exploration = 1

                else:

                    exploitation = float(self.wins[left_arm, right_arm])/denominator

                    exploration = np.sqrt(float(self.alpha * math.log(t))/denominator)

                self.utility[left_arm, right_arm] = exploration + exploitation

        # Updating the utility in the main axis.
        for arm in range(n_arms):
            self.utility[arm, arm] = 0.5

    def create_champion_set(self):
        """create_champion_set() - This function determines which arms are in the champions set. """
        n_arms = len(self.wins)

        # Looking for an arm that satisfies utility[left_arm][:] >= 1/2
        half_matrix = np.ones([n_arms, n_arms])*0.5

        greater_then_half_matrix = self.utility >= half_matrix

        for left_arm in range(n_arms):

            if np.all(greater_then_half_matrix[left_arm, :]):
                self.c_vector[left_arm] = True
            else:
                self.c_vector[left_arm] = False

    def chose_left_arm(self):
        """ chose_left_arm() - This function returns the chosen left arm. """

        # The total number of arms.
        n_arms = len(self.wins)

        # The number of arms in the champion set.
        number_of_optional_arms = np.sum(self.c_vector)

        # If there are no arms in the champion set -
        if number_of_optional_arms == 0:

            # A random arm is chosen.
            chosen_left_arm = random.choice(range(n_arms))

            # Updating the best set vector.
            self.b_vector = self.b_vector & self.c_vector

        # If there is only one arm in the champions set -
        elif number_of_optional_arms == 1:

            # That arm is chosen as the best arm.
            chosen_left_arm = int((np.where(self.c_vector))[0])

            # Updating the best set vector.
            self.b_vector[chosen_left_arm] = True

        else:

            # If there are more then one arm in the champions set we draw an arm according to the RUCB algorithm.
            chosen_left_arm = self.draw_arm_from_c()

        # Returning the chosen left arm.
        return chosen_left_arm

    def chose_right_arm(self, left_arm):
        """ chose_right_arm() - Choosing the right arm according to the RUCB algorithm. """

        # The u_jc vector.
        u_jc = self.utility[:, left_arm]

        # The max utility in the u_jc vector.
        max_utility = max(u_jc)

        # The location of the max utility.
        max_vector = (u_jc == max_utility)

        # The index of arms with the max value.
        arms_with_max_value = (np.where(max_vector))[0]

        # We need to chose the right arm to be the argmax_j(u_jc)
        # and there are 2 arms with the max value we choose an arm that is different from the left arm.
        if (left_arm in arms_with_max_value) and (np.sum(max_vector) > 1):
            chosen_right_arm = left_arm

            # If there are 2 arms with the max value we choose the right arm to be different from the left arm.
            while chosen_right_arm == left_arm:

                chosen_right_arm = random.choice(arms_with_max_value)

        # If the left arm does not hold the highest value:
        else:
            chosen_right_arm = random.choice(arms_with_max_value)

        return chosen_right_arm

    def update_wins_matrix(self, chosen_left_arm, chosen_right_arm, better_arm):
        """ update_wins_matrix() updating the wins matrix according to the arm value. """

        if better_arm == "left":

            self.wins[chosen_left_arm, chosen_right_arm] += 1

        elif better_arm == "right":

            self.wins[chosen_right_arm, chosen_left_arm] += 1

        return

    def draw_arm_from_c(self):
        """ draw_arm_from_c() - This function chooses an arm from the champions vector."""

        # Arms that are no in the Best set.
        inverted_b_vector = ~self.b_vector

        # Arms that are only in the champions vector.
        arms_only_in_c = self.c_vector & inverted_b_vector

        # Calculating the probability vector according to the RUCB algorithm.
        probability_vector = \
            np.multiply(0.5, self.b_vector) +\
            np.multiply(float((1/(float(2**(np.sum(self.b_vector)))*float(np.sum(arms_only_in_c))))), arms_only_in_c)

        # Choosing an arm according to the probability vector.
        chosen_arm = choose_from_probability_vector(probability_vector=probability_vector)

        # Returning the chosen arm.
        return chosen_arm

    def chose_best_arm(self):
        """ chose_best_arm() - This function returns the arm when the algorithm finishes it's run. """

        # The total number of arms.
        n_arms = len(self.wins)

        # The wins matrix.
        wins = np.zeros([n_arms, n_arms])

        # The wins ration matrix.
        wins_ratio = np.zeros([n_arms, n_arms])

        # Iterating over all the arm pairs.
        for left_arm in range(n_arms):

            for right_arm in range(n_arms):

                if self.wins[left_arm, right_arm] + self.wins.T[left_arm, right_arm] == 0:

                    wins[left_arm, right_arm] = 0
                    wins_ratio[left_arm, right_arm] = 0

                else:

                    wins_ratio[left_arm, right_arm] = \
                        (
                            float(self.wins[left_arm, right_arm]) /
                            float(self.wins[left_arm, right_arm] + self.wins.T[left_arm, right_arm])
                        )

                    wins[left_arm, right_arm] = wins_ratio[left_arm, right_arm] >= 0.5

        total_wins = np.zeros(n_arms)

        for arm in range(n_arms):
            total_wins[arm] = np.sum(wins[arm, :])

        return np.argmax(total_wins)


def choose_from_probability_vector(probability_vector):
    """ choose_from_probability_vector() - This function receives a probability vector and returns the chosen index."""
    r = random.random()
    index = 0

    while r >= 0 and index < len(probability_vector):

        r -= probability_vector[index]

        index += 1

    return index - 1


def run_rucb_algorithm(arms, horizon):
    """ run_rucb_algorithm() - This function runs the RUCB algorithm. """

    n_arms = arms.n_arms

    # Initializing the regret vector.
    regret = np.zeros(horizon)

    # Initializing the cumulative regret vector.
    cumulative_regret = np.zeros(horizon)

    # Constructing the RUCB algorithm object.
    algorithm = RUCB(n_arms=n_arms, alpha=0.5)

    # Initializing the algorithm.
    algorithm.initialize()

    for t in range(horizon):

        # Selecting the arms.
        [chosen_left_arm, chosen_right_arm] = algorithm.select_arms(t+1)

        # Obtaining the rewards.
        [left_reward, right_reward] = arms.draw(chosen_left_arm, chosen_right_arm)

        # Choosing the better arm.

        # Tie breaking rule.
        if left_reward == right_reward:

            better_arm = random.choice(["left", "right"])

        elif left_reward > right_reward:

            better_arm = "left"

        else:

            better_arm = "right"

        # Updating the wins matrix.
        algorithm.update_wins_matrix(chosen_left_arm, chosen_right_arm, better_arm)

        # Assigning the regret
        regret[t] = arms.get_regret(chosen_left_arm, chosen_right_arm)

        update_regret(regret, cumulative_regret, t)

    # Returning the cumulative regret.
    return cumulative_regret


def run_several_iterations(iterations, real_arms, horizon):
    """ run_several_iterations() - This function runs several iterations of the RUCB algorithm."""

    # Initializing the results vector.
    results = np.zeros(horizon)

    for iteration in range(iterations):

        # Adding the regret.
        results += run_rucb_algorithm(real_arms, horizon)

    return results/(iterations + .0)

def run_several_iterations_and_save_results(algorithm, iterations, arms, n_arms, horizon, data_type):
    """ test_several_iterations() - This function runs several iterations of the Sparring algorithm. """

    # Initializing the results vector.
    result = np.zeros([horizon, iterations])

    file_name = "{0}_{1}_arms_{2}_horizon_{3}".format(algorithm, data_type, n_arms, horizon)

    for iteration in range(iterations):

        # The current cumulative regret.
        result[:, iteration] = run_rucb_algorithm(arms, horizon)

    np.save(file_name, result)