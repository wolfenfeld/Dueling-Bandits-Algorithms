__author__ = 'wolfenfeld'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fontP = FontProperties()
fontP.set_size('small')

###############
# The figures #
###############

# One strong arm - 8 arms
fig_one_strong_arm_8 = plt.figure()
ax_one_strong_arm_8 = plt.subplot(111)

# One strong arm - 16 arms
fig_one_strong_arm_16 = plt.figure()
ax_one_strong_arm_16 = plt.subplot(111)

# One strong arm - 46 arms
fig_one_strong_arm_46 = plt.figure()
ax_one_strong_arm_46 = plt.subplot(111)


# Linear Arms - 8 arms
fig_linear_arm_8 = plt.figure()
ax_linear_arm_8 = plt.subplot(111)

# Linear Arms - 16 arms
fig_linear_arm_16 = plt.figure()
ax_linear_arm_16 = plt.subplot(111)

# Linear Arms - 46 arms
fig_linear_arm_46 = plt.figure()
ax_linear_arm_46 = plt.subplot(111)

# Close arms - 8 arms
fig_close_arm_8 = plt.figure()
ax_close_arm_8 = plt.subplot(111)

# Close Arms - 16 arms
fig_close_arm_16 = plt.figure()
ax_close_arm_16 = plt.subplot(111)

# Close Arms - 46 arms
fig_close_arm_46 = plt.figure()
ax_close_arm_46 = plt.subplot(111)

# Random Data - 8 arms
fig_random_data_8 = plt.figure()
ax_random_data_8 = plt.subplot(111)

# Random Data - 16 arms
fig_random_data_16 = plt.figure()
ax_random_data_16 = plt.subplot(111)

# Random Data - 46 arms
fig_random_data_46 = plt.figure()
ax_random_data_46 = plt.subplot(111)

# Real Data - 8 arms
fig_real_data_8 = plt.figure()
ax_real_data_8 = plt.subplot(111)

# Real Data - 16 arms
fig_real_data_16 = plt.figure()
ax_real_data_16 = plt.subplot(111)

# Real Data - 46 arms
fig_real_data_46 = plt.figure()
ax_real_data_46 = plt.subplot(111)


####################
# Balanced Doubler #
####################

# One strong arm - 8 arms
balanced_doubler_one_strong_arm_8 = \
    np.load('Balanced Doubler_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
horizon, number_of_iteration = balanced_doubler_one_strong_arm_8.shape
avg_balanced_doubler_one_strong_arm_8 = balanced_doubler_one_strong_arm_8.sum(axis=1)/number_of_iteration
ax_one_strong_arm_8.plot(range(horizon), avg_balanced_doubler_one_strong_arm_8, 'b--',
                         label="Balanced Doubler")

# One strong arm - 16 arms
balanced_doubler_one_strong_arm_16 = \
    np.load('Balanced Doubler_Synthetic_data_One Strong Arm_arms_16_horizon_131072.npy')
horizon, number_of_iteration = balanced_doubler_one_strong_arm_16.shape
avg_balanced_doubler_one_strong_arm_16 = balanced_doubler_one_strong_arm_16.sum(axis=1)/number_of_iteration
ax_one_strong_arm_16.plot(range(horizon), avg_balanced_doubler_one_strong_arm_16, 'b--',
                          label="Balanced Doubler")

# # One strong arm - 46 arms
# balanced_doubler_one_strong_arm_46 = \
#     np.load('Balanced Doubler_Synthetic_data_One Strong Arm_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = balanced_doubler_one_strong_arm_46.shape
# avg_balanced_doubler_one_strong_arm_46 = balanced_doubler_one_strong_arm_46.sum(axis=1)/number_of_iteration
# ax_one_strong_arm_46.plot(range(horizon), avg_balanced_doubler_one_strong_arm_46, 'b--',
#                           label="Balanced Doubler ")

# Close arm - 8 arms
balanced_doubler_close_arm_8 = \
    np.load('Balanced Doubler_Synthetic_data_Close Arms_arms_8_horizon_131072.npy')
horizon, number_of_iteration = balanced_doubler_close_arm_8.shape
avg_balanced_doubler_close_arm_8 = balanced_doubler_close_arm_8.sum(axis=1)/number_of_iteration
ax_close_arm_8.plot(range(horizon), avg_balanced_doubler_close_arm_8, 'b--',
                    label="Balanced Doubler")

# Close arm - 16 arms
# balanced_doubler_close_arm_16 = \
#     np.load('Balanced Doubler_Synthetic_data_Close Arms_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = balanced_doubler_close_arm_16.shape
# avg_balanced_doubler_close_arm_16 = balanced_doubler_close_arm_16.sum(axis=1)/number_of_iteration
# ax_close_arm_16.plot(range(horizon), avg_balanced_doubler_close_arm_16, 'b--',
#                      label="Balanced Doubler ")

# # Close arm - 46 arms
# balanced_doubler_close_arm_46 = \
#     np.load('Balanced Doubler_Synthetic_data_Close Arms_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = balanced_doubler_close_arm_46.shape
# avg_balanced_doubler_close_arm_46 = balanced_doubler_close_arm_46.sum(axis=1)/number_of_iteration
# ax_close_arm_16.plot(range(horizon), avg_balanced_doubler_close_arm_46, 'b--',
#                      label="Balanced Doubler ")

# Linear arm - 8 arms
balanced_doubler_linear_arm_8 = \
    np.load('Balanced Doubler_Synthetic_data_Linear List_arms_8_horizon_131072.npy')
horizon, number_of_iteration = balanced_doubler_linear_arm_8.shape
avg_balanced_doubler_linear_arm_8 = balanced_doubler_linear_arm_8.sum(axis=1)/number_of_iteration
ax_linear_arm_8.plot(range(horizon), avg_balanced_doubler_linear_arm_8, 'b--',
                     label="Balanced Doubler ")

# Linear arm - 16 arms
# balanced_doubler_linear_arm_16 = \
#     np.load('Balanced Doubler_Synthetic_data_Linear List_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = balanced_doubler_linear_arm_16.shape
# avg_balanced_doubler_linear_arm_16 = balanced_doubler_linear_arm_16.sum(axis=1)/number_of_iteration
# ax_linear_arm_16.plot(range(horizon), avg_balanced_doubler_linear_arm_16, 'b--',
#                       label="Balanced Doubler ")

# # Close arm - 46 arms
# balanced_doubler_linear_arm_46 = \
#     np.load('Balanced Doubler_Synthetic_data_Linear List_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = balanced_doubler_linear_arm_46.shape
# avg_balanced_doubler_linear_arm_46 = balanced_doubler_linear_arm_46.sum(axis=1)/number_of_iteration
# ax_linear_arm_16.plot(range(horizon), avg_balanced_doubler_linear_arm_46, 'b--',
#                       label="Balanced Doubler ")


# Random arms - 8 arms
balanced_doubler_random_arm_8 = \
    np.load('Balanced Doubler_Synthetic_data_Random_arms_8_horizon_131072.npy')
horizon, number_of_iteration = balanced_doubler_random_arm_8.shape
avg_balanced_doubler_random_arm_8 = balanced_doubler_random_arm_8.sum(axis=1)/number_of_iteration
ax_random_data_8.plot(range(horizon), avg_balanced_doubler_random_arm_8, 'b--',
                      label="Balanced Doubler ")

# Random arms - 16 arms
# balanced_doubler_random_arm_16 = \
#     np.load('Balanced Doubler_Synthetic_data_Random_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = balanced_doubler_random_arm_16.shape
# avg_balanced_doubler_random_arm_16 = balanced_doubler_random_arm_16.sum(axis=1)/number_of_iteration
# ax_random_data_16.plot(range(horizon), avg_balanced_doubler_random_arm_16, 'b--',
#                        label="Balanced Doubler ")

# # Random arms - 46 arms
# balanced_doubler_random_arm_46 = \
#     np.load('Balanced Doubler_Synthetic_data_Random_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = balanced_doubler_random_arm_46.shape
# avg_balanced_doubler_random_arm_46 = balanced_doubler_random_arm_46.sum(axis=1)/number_of_iteration
# ax_random_data_46.plot(range(horizon), avg_balanced_doubler_random_arm_46, 'b--',
#                        label="Balanced Doubler ")

# Real arms - 8 arms
balanced_doubler_real_arm_8 = \
    np.load('Balanced Doubler_Real_data_arms_8_horizon_131072.npy')
horizon, number_of_iteration = balanced_doubler_real_arm_8.shape
avg_balanced_doubler_real_arm_8 = balanced_doubler_real_arm_8.sum(axis=1)/number_of_iteration
ax_real_data_8.plot(range(horizon), avg_balanced_doubler_real_arm_8, 'b--',
                    label="Balanced Doubler ")

# Real arms - 16 arms
balanced_doubler_real_arm_16 = \
    np.load('Balanced Doubler_Real_data_arms_16_horizon_131072.npy')
horizon, number_of_iteration = balanced_doubler_real_arm_16.shape
avg_balanced_doubler_real_arm_16 = balanced_doubler_real_arm_16.sum(axis=1)/number_of_iteration
ax_real_data_16.plot(range(horizon), avg_balanced_doubler_real_arm_16, 'b--',
                     label="Balanced Doubler ")

# # Real arms - 46 arms
# balanced_doubler_real_arm_46 = \
#     np.load('Balanced Doubler_Real_data_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = balanced_doubler_real_arm_46.shape
# avg_balanced_doubler_real_arm_46 = balanced_doubler_real_arm_46.sum(axis=1)/number_of_iteration
# ax_real_data_46.plot(range(horizon), avg_balanced_doubler_real_arm_46, 'b--',
#                      label="Balanced Doubler ")

############
# Sparring #
############

sparring_one_strong_arm_8 = \
    np.load('Sparring_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_one_strong_arm_8.shape
avg_sparring_one_strong_arm_8 = sparring_one_strong_arm_8.sum(axis=1)/number_of_iteration
ax_one_strong_arm_8.plot(range(horizon), avg_sparring_one_strong_arm_8, 'g--',
                         label="Sparring ")

sparring_one_strong_arm_16 = \
    np.load('Sparring_Synthetic_data_One Strong Arm_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_one_strong_arm_16.shape
avg_sparring_one_strong_arm_16 = sparring_one_strong_arm_16.sum(axis=1)/number_of_iteration
ax_one_strong_arm_16.plot(range(horizon), avg_sparring_one_strong_arm_16, 'g--',
                          label="Sparring ")

sparring_one_strong_arm_46 = \
    np.load('Sparring_Synthetic_data_One Strong Arm_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_one_strong_arm_46.shape
avg_sparring_one_strong_arm_46 = sparring_one_strong_arm_46.sum(axis=1)/number_of_iteration
ax_one_strong_arm_46.plot(range(horizon), avg_sparring_one_strong_arm_46, 'g--',
                          label="Sparring ")

sparring_close_arm_8 = \
    np.load('Sparring_Synthetic_data_Close Arms_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_close_arm_8.shape
avg_sparring_close_arm_8 = sparring_close_arm_8.sum(axis=1)/number_of_iteration
ax_close_arm_8.plot(range(horizon), avg_sparring_close_arm_8, 'g--',
                    label="Sparring ")

sparring_close_arm_16 = \
    np.load('Sparring_Synthetic_data_Close Arms_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_close_arm_16.shape
avg_sparring_close_arm_16 = sparring_close_arm_16.sum(axis=1)/number_of_iteration
ax_close_arm_16.plot(range(horizon), avg_sparring_close_arm_16, 'g--',
                     label="Sparring ")

sparring_close_arm_46 = \
    np.load('Sparring_Synthetic_data_Close Arms_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_close_arm_46.shape
avg_sparring_close_arm_46 = sparring_close_arm_46.sum(axis=1)/number_of_iteration
ax_close_arm_46.plot(range(horizon), avg_sparring_close_arm_46, 'g--',
                     label="Sparring ")

sparring_linear_arm_8 = \
    np.load('Sparring_Synthetic_data_Linear List_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_linear_arm_8.shape
avg_sparring_linear_arm_8 = sparring_linear_arm_8.sum(axis=1)/number_of_iteration
ax_linear_arm_8.plot(range(horizon), avg_sparring_linear_arm_8, 'g--',
                     label="Sparring ")

sparring_linear_arm_16 = \
    np.load('Sparring_Synthetic_data_Linear List_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_linear_arm_16.shape
avg_sparring_linear_arm_16 = sparring_linear_arm_16.sum(axis=1)/number_of_iteration
ax_linear_arm_16.plot(range(horizon), avg_sparring_linear_arm_16, 'g--',
                      label="Sparring ")

sparring_linear_arm_46 = \
    np.load('Sparring_Synthetic_data_Linear List_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_linear_arm_46.shape
avg_sparring_linear_arm_46 = sparring_linear_arm_46.sum(axis=1)/number_of_iteration
ax_linear_arm_46.plot(range(horizon), avg_sparring_linear_arm_46, 'g--',
                      label="Sparring ")

sparring_random_arm_8 = \
    np.load('Sparring_Synthetic_data_Random_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_random_arm_8.shape
avg_sparring_random_arm_8 = sparring_random_arm_8.sum(axis=1)/number_of_iteration
ax_random_data_8.plot(range(horizon), avg_sparring_random_arm_8, 'g--',
                      label="Sparring ")

sparring_random_arm_16 = \
    np.load('Sparring_Synthetic_data_Random_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_random_arm_16.shape
avg_sparring_random_arm_16 = sparring_random_arm_16.sum(axis=1)/number_of_iteration
ax_random_data_16.plot(range(horizon), avg_sparring_random_arm_16, 'g--',
                       label="Sparring ")

sparring_random_arm_46 = \
    np.load('Sparring_Synthetic_data_Random_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_random_arm_46.shape
avg_sparring_random_arm_46 = sparring_random_arm_46.sum(axis=1)/number_of_iteration
ax_random_data_46.plot(range(horizon), avg_sparring_random_arm_46, 'g--',
                       label="Sparring ")

sparring_real_arm_8 = \
    np.load('Sparring_Real_data_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_real_arm_8.shape
avg_sparring_real_arm_8 = sparring_real_arm_8.sum(axis=1)/number_of_iteration
ax_real_data_8.plot(range(horizon), avg_sparring_real_arm_8, 'g--',
                    label="Sparring ")

sparring_real_arm_16 = \
    np.load('Sparring_Real_data_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_real_arm_16.shape
avg_sparring_real_arm_16 = sparring_real_arm_16.sum(axis=1)/number_of_iteration
ax_real_data_16.plot(range(horizon), avg_sparring_real_arm_16, 'g--',
                     label="Sparring ")

# sparring_real_arm_46 = \
#     np.load('Sparring_Real_data_Random_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = sparring_real_arm_46.shape
# avg_sparring_real_arm_46 = sparring_real_arm_46.sum(axis=1)/number_of_iteration
# ax_real_data_46.plot(range(horizon), avg_sparring_real_arm_46, 'g--',
#                      label="Sparring ")


###############
# Sparring TS #
###############

sparring_ts_one_strong_arm_8 = \
    np.load('Sparring TS_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_one_strong_arm_8.shape
avg_sparring_ts_one_strong_arm_8 = sparring_ts_one_strong_arm_8.sum(axis=1)/number_of_iteration
ax_one_strong_arm_8.plot(range(horizon), avg_sparring_ts_one_strong_arm_8, 'r--',
                         label="Sparring Thompson Sampling ")

sparring_ts_one_strong_arm_16 = \
    np.load('Sparring TS_Synthetic_data_One Strong Arm_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_one_strong_arm_16.shape
avg_sparring_ts_one_strong_arm_16 = sparring_ts_one_strong_arm_16.sum(axis=1)/number_of_iteration
ax_one_strong_arm_16.plot(range(horizon), avg_sparring_ts_one_strong_arm_16, 'r--',
                          label="Sparring Thompson Sampling ")

sparring_ts_one_strong_arm_46 = \
    np.load('Sparring TS_Synthetic_data_One Strong Arm_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_one_strong_arm_46.shape
avg_sparring_ts_one_strong_arm_46 = sparring_ts_one_strong_arm_46.sum(axis=1)/number_of_iteration
ax_one_strong_arm_46.plot(range(horizon), avg_sparring_ts_one_strong_arm_46, 'r--',
                          label="Sparring Thompson Sampling ")

sparring_ts_close_arm_8 = \
    np.load('Sparring TS_Synthetic_data_Close Arms_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_close_arm_8.shape
avg_sparring_ts_close_arm_8 = sparring_ts_close_arm_8.sum(axis=1)/number_of_iteration
ax_close_arm_8.plot(range(horizon), avg_sparring_ts_close_arm_8, 'r--',
                    label="Sparring Thompson Sampling ")

sparring_ts_close_arm_16 = \
    np.load('Sparring TS_Synthetic_data_Close Arms_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_close_arm_16.shape
avg_sparring_ts_close_arm_16 = sparring_ts_close_arm_16.sum(axis=1)/number_of_iteration
ax_close_arm_16.plot(range(horizon), avg_sparring_ts_close_arm_16, 'r--',
                     label="Sparring Thompson Sampling ")

sparring_ts_close_arm_46 = \
    np.load('Sparring TS_Synthetic_data_Close Arms_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_close_arm_46.shape
avg_sparring_ts_close_arm_46 = sparring_ts_close_arm_46.sum(axis=1)/number_of_iteration
ax_close_arm_46.plot(range(horizon), avg_sparring_ts_close_arm_46, 'r--',
                     label="Sparring Thompson Sampling ")

sparring_ts_linear_arm_8 = \
    np.load('Sparring TS_Synthetic_data_Linear List_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_linear_arm_8.shape
avg_sparring_ts_linear_arm_8 = sparring_ts_linear_arm_8.sum(axis=1)/number_of_iteration
ax_linear_arm_8.plot(range(horizon), avg_sparring_ts_linear_arm_8, 'r--',
                     label="Sparring Thompson Sampling ")

sparring_ts_linear_arm_16 = \
    np.load('Sparring TS_Synthetic_data_Linear List_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_linear_arm_16.shape
avg_sparring_ts_linear_arm_16 = sparring_ts_linear_arm_16.sum(axis=1)/number_of_iteration
ax_linear_arm_16.plot(range(horizon), avg_sparring_ts_linear_arm_16, 'r--',
                      label="Sparring Thompson Sampling ")

sparring_ts_linear_arm_46 = \
    np.load('Sparring TS_Synthetic_data_Linear List_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_linear_arm_46.shape
avg_sparring_ts_linear_arm_46 = sparring_ts_linear_arm_46.sum(axis=1)/number_of_iteration
ax_linear_arm_46.plot(range(horizon), avg_sparring_ts_linear_arm_46, 'r--',
                      label="Sparring Thompson Sampling ")

sparring_ts_random_arm_8 = \
    np.load('Sparring TS_Synthetic_data_Random_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_random_arm_8.shape
avg_sparring_ts_random_arm_8 = sparring_ts_random_arm_8.sum(axis=1)/number_of_iteration
ax_random_data_8.plot(range(horizon), avg_sparring_ts_random_arm_8, 'r--',
                      label="Sparring Thompson Sampling ")

sparring_ts_random_arm_16 = \
    np.load('Sparring TS_Synthetic_data_Random_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_random_arm_16.shape
avg_sparring_ts_random_arm_16 = sparring_ts_random_arm_16.sum(axis=1)/number_of_iteration
ax_random_data_16.plot(range(horizon), avg_sparring_ts_random_arm_16, 'r--',
                       label="Sparring Thompson Sampling ")

sparring_ts_random_arm_46 = \
    np.load('Sparring TS_Synthetic_data_Random_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_random_arm_46.shape
avg_sparring_ts_random_arm_46 = sparring_ts_random_arm_46.sum(axis=1)/number_of_iteration
ax_random_data_46.plot(range(horizon), avg_sparring_ts_random_arm_46, 'r--',
                       label="Sparring Thompson Sampling ")

sparring_ts_real_arm_8 = \
    np.load('Sparring TS_Real_data_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_real_arm_8.shape
avg_sparring_ts_real_arm_8 = sparring_ts_real_arm_8.sum(axis=1)/number_of_iteration
ax_real_data_8.plot(range(horizon), avg_sparring_ts_real_arm_8, 'r--',
                    label="Sparring Thompson Sampling ")

sparring_ts_real_arm_16 = \
    np.load('Sparring TS_Real_data_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_real_arm_16.shape
avg_sparring_ts_real_arm_16 = sparring_ts_real_arm_16.sum(axis=1)/number_of_iteration
ax_real_data_16.plot(range(horizon), avg_sparring_ts_real_arm_16, 'r--',
                     label="Sparring Thompson Sampling ")

sparring_ts_real_arm_46 = \
    np.load('Sparring TS_Real_data_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_real_arm_46.shape
avg_sparring_ts_real_arm_46 = sparring_ts_real_arm_46.sum(axis=1)/number_of_iteration
ax_real_data_46.plot(range(horizon), avg_sparring_ts_real_arm_46, 'r--',
                     label="Sparring Thompson Sampling ")

#####################
# Sparring TS Turbo #
#####################

sparring_ts_turbo_one_strong_arm_8 = \
    np.load('Sparring TS Turbo_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_one_strong_arm_8.shape
avg_sparring_ts_turbo_one_strong_arm_8 = sparring_ts_turbo_one_strong_arm_8.sum(axis=1)/number_of_iteration
ax_one_strong_arm_8.plot(range(horizon), avg_sparring_ts_turbo_one_strong_arm_8, 'c--',
                         label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_one_strong_arm_16 = \
    np.load('Sparring TS Turbo_Synthetic_data_One Strong Arm_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_one_strong_arm_16.shape
avg_sparring_ts_turbo_one_strong_arm_16 = sparring_ts_turbo_one_strong_arm_16.sum(axis=1)/number_of_iteration
ax_one_strong_arm_16.plot(range(horizon), avg_sparring_ts_turbo_one_strong_arm_16, 'c--',
                          label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_one_strong_arm_46 = \
    np.load('Sparring TS Turbo_Synthetic_data_One Strong Arm_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_one_strong_arm_46.shape
avg_sparring_ts_turbo_one_strong_arm_46 = sparring_ts_turbo_one_strong_arm_46.sum(axis=1)/number_of_iteration
ax_one_strong_arm_46.plot(range(horizon), avg_sparring_ts_turbo_one_strong_arm_46, 'c--',
                          label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_close_arm_8 = \
    np.load('Sparring TS Turbo_Synthetic_data_Close Arms_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_close_arm_8.shape
avg_sparring_ts_turbo_close_arm_8 = sparring_ts_turbo_close_arm_8.sum(axis=1)/number_of_iteration
ax_close_arm_8.plot(range(horizon), avg_sparring_ts_turbo_close_arm_8, 'c--',
                    label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_close_arm_16 = \
    np.load('Sparring TS Turbo_Synthetic_data_Close Arms_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_close_arm_16.shape
avg_sparring_ts_turbo_close_arm_16 = sparring_ts_turbo_close_arm_16.sum(axis=1)/number_of_iteration
ax_close_arm_16.plot(range(horizon), avg_sparring_ts_turbo_close_arm_16, 'c--',
                     label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_close_arm_46 = \
    np.load('Sparring TS Turbo_Synthetic_data_Close Arms_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_close_arm_46.shape
avg_sparring_ts_turbo_close_arm_46 = sparring_ts_turbo_close_arm_46.sum(axis=1)/number_of_iteration
ax_close_arm_46.plot(range(horizon), avg_sparring_ts_turbo_close_arm_46, 'c--',
                     label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_linear_arm_8 = \
    np.load('Sparring TS Turbo_Synthetic_data_Linear List_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_linear_arm_8.shape
avg_sparring_ts_turbo_linear_arm_8 = sparring_ts_turbo_linear_arm_8.sum(axis=1)/number_of_iteration
ax_linear_arm_8.plot(range(horizon), avg_sparring_ts_turbo_linear_arm_8, 'c--',
                     label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_linear_arm_16 = \
    np.load('Sparring TS Turbo_Synthetic_data_Linear List_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_linear_arm_16.shape
avg_sparring_ts_turbo_linear_arm_16 = sparring_ts_turbo_linear_arm_16.sum(axis=1)/number_of_iteration
ax_linear_arm_16.plot(range(horizon), avg_sparring_ts_turbo_linear_arm_16, 'c--',
                      label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_linear_arm_46 = \
    np.load('Sparring TS Turbo_Synthetic_data_Linear List_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_linear_arm_46.shape
avg_sparring_ts_turbo_linear_arm_46 = sparring_ts_turbo_linear_arm_46.sum(axis=1)/number_of_iteration
ax_linear_arm_46.plot(range(horizon), avg_sparring_ts_turbo_linear_arm_46, 'c--',
                      label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_random_arm_8 = \
    np.load('Sparring TS Turbo_Synthetic_data_Random_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_random_arm_8.shape
avg_sparring_ts_turbo_random_arm_8 = sparring_ts_turbo_random_arm_8.sum(axis=1)/number_of_iteration
ax_random_data_8.plot(range(horizon), avg_sparring_ts_turbo_random_arm_8, 'c--',
                      label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_random_arm_16 = \
    np.load('Sparring TS Turbo_Synthetic_data_Random_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_random_arm_16.shape
avg_sparring_ts_turbo_random_arm_16 = sparring_ts_turbo_random_arm_16.sum(axis=1)/number_of_iteration
ax_random_data_16.plot(range(horizon), avg_sparring_ts_turbo_random_arm_16, 'c--',
                       label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_random_arm_46 = \
    np.load('Sparring TS Turbo_Synthetic_data_Random_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_random_arm_46.shape
avg_sparring_ts_turbo_random_arm_46 = sparring_ts_turbo_random_arm_46.sum(axis=1)/number_of_iteration
ax_random_data_46.plot(range(horizon), avg_sparring_ts_turbo_random_arm_46, 'c--',
                       label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_real_arm_8 = \
    np.load('Sparring TS Turbo_Real_data_arms_8_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_real_arm_8.shape
avg_sparring_ts_turbo_real_arm_8 = sparring_ts_turbo_real_arm_8.sum(axis=1)/number_of_iteration
ax_real_data_8.plot(range(horizon), avg_sparring_ts_turbo_real_arm_8, 'c--',
                    label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_real_arm_16 = \
    np.load('Sparring TS Turbo_Real_data_arms_16_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_real_arm_16.shape
avg_sparring_ts_turbo_real_arm_16 = sparring_ts_turbo_real_arm_16.sum(axis=1)/number_of_iteration
ax_real_data_16.plot(range(horizon), avg_sparring_ts_turbo_real_arm_16, 'c--',
                     label="Sparring Thompson Sampling Turbo ")

sparring_ts_turbo_real_arm_46 = \
    np.load('Sparring TS Turbo_Real_data_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_real_arm_46.shape
avg_sparring_ts_turbo_real_arm_46 = sparring_ts_turbo_real_arm_46.sum(axis=1)/number_of_iteration
ax_real_data_46.plot(range(horizon), avg_sparring_ts_turbo_real_arm_46, 'c--',
                     label="Sparring Thompson Sampling Turbo ")

#######
# BTM #
#######

btm_one_strong_arm_8 = np.load('BTM_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
horizon, number_of_iteration = btm_one_strong_arm_8.shape
avg_btm_one_strong_arm_8 = btm_one_strong_arm_8.sum(axis=1)/number_of_iteration
ax_one_strong_arm_8.plot(range(horizon), avg_btm_one_strong_arm_8, 'm--',
                         label="BTM ")

btm_one_strong_arm_16 = np.load('BTM_Synthetic_data_One Strong Arm_arms_16_horizon_131072.npy')
horizon, number_of_iteration = btm_one_strong_arm_16.shape
avg_btm_one_strong_arm_16 = btm_one_strong_arm_16.sum(axis=1)/number_of_iteration
ax_one_strong_arm_16.plot(range(horizon), avg_btm_one_strong_arm_16, 'm--',
                          label="BTM ")

btm_one_strong_arm_46 = np.load('BTM_Synthetic_data_One Strong Arm_arms_46_horizon_131072.npy')
horizon, number_of_iteration = btm_one_strong_arm_46.shape
avg_btm_one_strong_arm_46 = btm_one_strong_arm_46.sum(axis=1)/number_of_iteration
ax_one_strong_arm_46.plot(range(horizon), avg_btm_one_strong_arm_46, 'm--',
                          label="BTM ")

btm_close_arm_8 = np.load('BTM_Synthetic_data_Close Arms_arms_8_horizon_131072.npy')
horizon, number_of_iteration = btm_close_arm_8.shape
avg_btm_close_arm_8 = btm_close_arm_8.sum(axis=1)/number_of_iteration
ax_close_arm_8.plot(range(horizon), avg_btm_close_arm_8, 'm--',
                    label="BTM ")

btm_close_arm_16 = np.load('BTM_Synthetic_data_Close Arms_arms_16_horizon_131072.npy')
horizon, number_of_iteration = btm_close_arm_16.shape
avg_btm_close_arm_16 = btm_close_arm_16.sum(axis=1)/number_of_iteration
ax_close_arm_16.plot(range(horizon), avg_btm_close_arm_16, 'm--',
                     label="BTM ")

btm_close_arm_46 = np.load('BTM_Synthetic_data_Close Arms_arms_46_horizon_131072.npy')
horizon, number_of_iteration = btm_close_arm_46.shape
avg_btm_close_arm_46 = btm_close_arm_46.sum(axis=1)/number_of_iteration
ax_close_arm_46.plot(range(horizon), avg_btm_close_arm_46, 'm--',
                     label="BTM ")

btm_linear_arm_8 = np.load('BTM_Synthetic_data_Linear List_arms_8_horizon_131072.npy')
horizon, number_of_iteration = btm_linear_arm_8.shape
avg_btm_linear_arm_8 = btm_linear_arm_8.sum(axis=1)/number_of_iteration
ax_linear_arm_8.plot(range(horizon), avg_btm_linear_arm_8, 'm--',
                     label="BTM ")

btm_linear_arm_16 = np.load('BTM_Synthetic_data_Linear List_arms_16_horizon_131072.npy')
horizon, number_of_iteration = btm_linear_arm_16.shape
avg_btm_linear_arm_16 = btm_linear_arm_16.sum(axis=1)/number_of_iteration
ax_linear_arm_16.plot(range(horizon), avg_btm_linear_arm_16, 'm--',
                      label="BTM ")

btm_linear_arm_46 = np.load('BTM_Synthetic_data_Linear List_arms_46_horizon_131072.npy')
horizon, number_of_iteration = btm_linear_arm_46.shape
avg_btm_linear_arm_46 = btm_linear_arm_46.sum(axis=1)/number_of_iteration
ax_linear_arm_46.plot(range(horizon), avg_btm_linear_arm_46, 'm--',
                      label="BTM ")

btm_random_arm_8 = np.load('BTM_Synthetic_data_Random_arms_8_horizon_131072.npy')
horizon, number_of_iteration = btm_random_arm_8.shape
avg_btm_random_arm_8 = btm_random_arm_8.sum(axis=1)/number_of_iteration
ax_random_data_8.plot(range(horizon), avg_btm_random_arm_8, 'm--',
                      label="BTM ")

btm_random_arm_16 = np.load('BTM_Synthetic_data_Random_arms_16_horizon_131072.npy')
horizon, number_of_iteration = btm_random_arm_16.shape
avg_btm_random_arm_16 = btm_random_arm_16.sum(axis=1)/number_of_iteration
ax_random_data_16.plot(range(horizon), avg_btm_random_arm_16, 'm--',
                       label="BTM ")

btm_random_arm_46 = np.load('BTM_Synthetic_data_Random_arms_46_horizon_131072.npy')
horizon, number_of_iteration = btm_random_arm_46.shape
avg_btm_random_arm_46 = btm_random_arm_46.sum(axis=1)/number_of_iteration
ax_random_data_46.plot(range(horizon), avg_btm_random_arm_46, 'm--',
                       label="BTM ")

# btm_real_arm_8 = np.load('BTM_Real_data_arms_8_horizon_131072.npy')
# horizon, number_of_iteration = btm_real_arm_8.shape
# avg_btm_real_arm_8 = btm_real_arm_8.sum(axis=1)/number_of_iteration
# ax_real_data_8.plot(range(horizon), avg_btm_real_arm_8, 'm--',
#                     label="BTM ")
#
# btm_real_arm_16 = np.load('BTM_Real_data_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = btm_real_arm_16.shape
# avg_btm_real_arm_16 = btm_real_arm_16.sum(axis=1)/number_of_iteration
# ax_real_data_16.plot(range(horizon), avg_btm_real_arm_16, 'm--',
#                      label="BTM ")
#
# btm_real_arm_46 = np.load('BTM_Real_data_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = btm_real_arm_46.shape
# avg_btm_real_arm_46 = btm_real_arm_46.sum(axis=1)/number_of_iteration
# ax_real_data_46.plot(range(horizon), avg_btm_real_arm_46, 'm--',
#                      label="BTM ")

###########
# Doubler #
###########

# doubler_one_strong_arm_8 = \
#     np.load('Doubler_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
# horizon, number_of_iteration = doubler_one_strong_arm_8.shape
# avg_doubler_one_strong_arm_8 = doubler_one_strong_arm_8.sum(axis=1)/number_of_iteration
# ax_one_strong_arm_8.plot(range(horizon), avg_doubler_one_strong_arm_8, 'k--',
#                          label="Doubler ")

# doubler_one_strong_arm_16 = \
#     np.load('Doubler_Synthetic_data_One Strong Arm_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = doubler_one_strong_arm_16.shape
# avg_doubler_one_strong_arm_16 = doubler_one_strong_arm_16.sum(axis=1)/number_of_iteration
# ax_one_strong_arm_16.plot(range(horizon), avg_doubler_one_strong_arm_16, 'k--',
#                           label="Doubler ")

doubler_one_strong_arm_46 = \
    np.load('Doubler_Synthetic_data_One Strong Arm_arms_46_horizon_131072.npy')
horizon, number_of_iteration = doubler_one_strong_arm_46.shape
avg_doubler_one_strong_arm_46 = doubler_one_strong_arm_46.sum(axis=1)/number_of_iteration
ax_one_strong_arm_46.plot(range(horizon), avg_doubler_one_strong_arm_46, 'k--',
                          label="Doubler ")

doubler_close_arm_8 = \
    np.load('Doubler_Synthetic_data_Close Arms_arms_8_horizon_131072.npy')
horizon, number_of_iteration = doubler_close_arm_8.shape
avg_doubler_close_arm_8 = doubler_close_arm_8.sum(axis=1)/number_of_iteration
ax_close_arm_8.plot(range(horizon), avg_doubler_close_arm_8, 'k--',
                    label="Doubler ")

doubler_close_arm_16 = \
    np.load('Doubler_Synthetic_data_Close Arms_arms_16_horizon_131072.npy')
horizon, number_of_iteration = doubler_close_arm_16.shape
avg_doubler_close_arm_16 = doubler_close_arm_16.sum(axis=1)/number_of_iteration
ax_close_arm_16.plot(range(horizon), avg_doubler_close_arm_16, 'k--',
                     label="Doubler ")

doubler_close_arm_46 = \
    np.load('Doubler_Synthetic_data_Close Arms_arms_46_horizon_131072.npy')
horizon, number_of_iteration = doubler_close_arm_46.shape
avg_doubler_close_arm_46 = doubler_close_arm_46.sum(axis=1)/number_of_iteration
ax_close_arm_46.plot(range(horizon), avg_doubler_close_arm_46, 'k--',
                     label="Doubler ")

doubler_linear_arm_8 = \
    np.load('Doubler_Synthetic_data_Linear List_arms_8_horizon_131072.npy')
horizon, number_of_iteration = doubler_linear_arm_8.shape
avg_doubler_linear_arm_8 = doubler_linear_arm_8.sum(axis=1)/number_of_iteration
ax_linear_arm_8.plot(range(horizon), avg_doubler_linear_arm_8, 'k--',
                     label="Doubler ")

# doubler_linear_arm_16 = \
#     np.load('Doubler_Synthetic_data_Linear List_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = doubler_linear_arm_16.shape
# avg_doubler_linear_arm_16 = doubler_linear_arm_16.sum(axis=1)/number_of_iteration
# ax_linear_arm_16.plot(range(horizon), avg_doubler_linear_arm_16, 'k--',
#                       label="Doubler ")

doubler_linear_arm_46 = \
    np.load('Doubler_Synthetic_data_Linear List_arms_46_horizon_131072.npy')
horizon, number_of_iteration = doubler_linear_arm_46.shape
avg_doubler_linear_arm_46 = doubler_linear_arm_46.sum(axis=1)/number_of_iteration
ax_linear_arm_46.plot(range(horizon), avg_doubler_linear_arm_46, 'k--',
                      label="Doubler ")

doubler_random_arm_8 = \
    np.load('Doubler_Synthetic_data_Random_arms_8_horizon_131072.npy')
horizon, number_of_iteration = doubler_random_arm_8.shape
avg_doubler_random_arm_8 = doubler_random_arm_8.sum(axis=1)/number_of_iteration
ax_random_data_8.plot(range(horizon), avg_doubler_random_arm_8, 'k--',
                      label="Doubler ")

doubler_random_arm_16 = \
    np.load('Doubler_Synthetic_data_Random_arms_16_horizon_131072.npy')
horizon, number_of_iteration = doubler_random_arm_16.shape
avg_doubler_random_arm_16 = doubler_random_arm_16.sum(axis=1)/number_of_iteration
ax_random_data_16.plot(range(horizon), avg_doubler_random_arm_16, 'k--',
                       label="Doubler ")

doubler_random_arm_46 = \
    np.load('Doubler_Synthetic_data_Random_arms_46_horizon_131072.npy')
horizon, number_of_iteration = doubler_random_arm_46.shape
avg_doubler_random_arm_46 = doubler_random_arm_46.sum(axis=1)/number_of_iteration
ax_random_data_46.plot(range(horizon), avg_doubler_random_arm_46, 'k--',
                       label="Doubler ")

doubler_real_arm_8 = \
    np.load('Doubler_Real_data_arms_8_horizon_131072.npy')
horizon, number_of_iteration = doubler_real_arm_8.shape
avg_doubler_real_arm_8 = doubler_real_arm_8.sum(axis=1)/number_of_iteration
ax_real_data_8.plot(range(horizon), avg_doubler_real_arm_8, 'k--',
                    label="Doubler ")

doubler_real_arm_16 = \
    np.load('Doubler_Real_data_arms_16_horizon_131072.npy')
horizon, number_of_iteration = doubler_real_arm_16.shape
avg_doubler_real_arm_16 = doubler_real_arm_16.sum(axis=1)/number_of_iteration
ax_real_data_16.plot(range(horizon), avg_doubler_real_arm_16, 'k--',
                     label="Doubler ")

doubler_real_arm_46 = \
    np.load('Doubler_Real_data_arms_46_horizon_131072.npy')
horizon, number_of_iteration = doubler_real_arm_46.shape
avg_doubler_real_arm_46 = doubler_real_arm_46.sum(axis=1)/number_of_iteration
ax_real_data_46.plot(range(horizon), avg_doubler_real_arm_46, 'k--',
                     label="Doubler ")


######################
# Forgetful Doubler #
######################

forgetful_doubler_one_strong_arm_8 = \
    np.load('Forgetful Doubler_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_one_strong_arm_8.shape
avg_forgetful_doubler_one_strong_arm_8 = forgetful_doubler_one_strong_arm_8.sum(axis=1)/number_of_iteration
ax_one_strong_arm_8.plot(range(horizon), avg_forgetful_doubler_one_strong_arm_8, 'b-',
                         label="Forgetful Doubler ")

forgetful_doubler_one_strong_arm_16 = \
    np.load('Forgetful Doubler_Synthetic_data_One Strong Arm_arms_16_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_one_strong_arm_16.shape
avg_forgetful_doubler_one_strong_arm_16 = forgetful_doubler_one_strong_arm_16.sum(axis=1)/number_of_iteration
ax_one_strong_arm_16.plot(range(horizon), avg_forgetful_doubler_one_strong_arm_16, 'b-',
                          label="Forgetful Doubler ")

forgetfull_doubler_one_strong_arm_46 = \
    np.load('Forgetful Doubler_Synthetic_data_One Strong Arm_arms_46_horizon_131072.npy')
horizon, number_of_iteration = forgetfull_doubler_one_strong_arm_46.shape
avg_forgetfull_doubler_one_strong_arm_46 = forgetfull_doubler_one_strong_arm_46.sum(axis=1)/number_of_iteration
ax_one_strong_arm_46.plot(range(horizon), avg_forgetfull_doubler_one_strong_arm_46, 'b-',
                          label="Forgetful Doubler ")

forgetful_doubler_close_arm_8 = \
    np.load('Forgetful Doubler_Synthetic_data_Close Arms_arms_8_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_close_arm_8.shape
avg_forgetful_doubler_close_arm_8 = forgetful_doubler_close_arm_8.sum(axis=1)/number_of_iteration
ax_close_arm_8.plot(range(horizon), avg_forgetful_doubler_close_arm_8, 'b-',
                    label="Forgetful Doubler ")

forgetful_doubler_close_arm_16 = \
    np.load('Forgetful Doubler_Synthetic_data_Close Arms_arms_16_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_close_arm_16.shape
avg_forgetful_doubler_close_arm_16 = forgetful_doubler_close_arm_16.sum(axis=1)/number_of_iteration
ax_close_arm_16.plot(range(horizon), avg_forgetful_doubler_close_arm_16, 'b-',
                     label="Forgetful Doubler ")

forgetful_doubler_close_arm_46 = \
    np.load('Forgetful Doubler_Synthetic_data_Close Arms_arms_46_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_close_arm_46.shape
avg_forgetful_doubler_close_arm_46 = forgetful_doubler_close_arm_46.sum(axis=1)/number_of_iteration
ax_close_arm_46.plot(range(horizon), avg_forgetful_doubler_close_arm_46, 'b-',
                     label="Forgetful Doubler ")

forgetful_doubler_linear_arm_8 = \
    np.load('Forgetful Doubler_Synthetic_data_Linear List_arms_8_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_linear_arm_8.shape
avg_forgetful_doubler_linear_arm_8 = forgetful_doubler_linear_arm_8.sum(axis=1)/number_of_iteration
ax_linear_arm_8.plot(range(horizon), avg_forgetful_doubler_linear_arm_8, 'b-',
                     label="Forgetful Doubler ")

forgetful_doubler_linear_arm_16 = \
    np.load('Forgetful Doubler_Synthetic_data_Linear List_arms_16_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_linear_arm_16.shape
avg_forgetful_doubler_linear_arm_16 = forgetful_doubler_linear_arm_16.sum(axis=1)/number_of_iteration
ax_linear_arm_16.plot(range(horizon), avg_forgetful_doubler_linear_arm_16, 'b-',
                      label="Forgetful Doubler ")

forgetful_doubler_linear_arm_46 = \
    np.load('Forgetful Doubler_Synthetic_data_Linear List_arms_46_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_linear_arm_46.shape
avg_forgetful_doubler_linear_arm_46 = forgetful_doubler_linear_arm_46.sum(axis=1)/number_of_iteration
ax_linear_arm_46.plot(range(horizon), avg_forgetful_doubler_linear_arm_46, 'b-',
                      label="Forgetful Doubler ")

forgetful_doubler_random_arm_8 = \
    np.load('Forgetful Doubler_Synthetic_data_Random_arms_8_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_random_arm_8.shape
avg_forgetful_doubler_random_arm_8 = forgetful_doubler_random_arm_8.sum(axis=1)/number_of_iteration
ax_random_data_8.plot(range(horizon), avg_forgetful_doubler_random_arm_8, 'b-',
                      label="Forgetful Doubler ")

forgetful_doubler_random_arm_16 = \
    np.load('Forgetful Doubler_Synthetic_data_Random_arms_16_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_random_arm_16.shape
avg_forgetful_doubler_random_arm_16 = forgetful_doubler_random_arm_16.sum(axis=1)/number_of_iteration
ax_random_data_16.plot(range(horizon), avg_forgetful_doubler_random_arm_16, 'b-',
                       label="Forgetful Doubler ")

forgetful_doubler_random_arm_46 = \
    np.load('Forgetful Doubler_Synthetic_data_Random_arms_46_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_random_arm_46.shape
avg_forgetful_doubler_random_arm_46 = forgetful_doubler_random_arm_46.sum(axis=1)/number_of_iteration
ax_random_data_46.plot(range(horizon), avg_forgetful_doubler_random_arm_46, 'b-',
                       label="Forgetful Doubler ")

forgetful_doubler_real_arm_8 = \
    np.load('Forgetful Doubler_Real_data_arms_8_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_real_arm_8.shape
avg_forgetful_doubler_real_arm_8 = forgetful_doubler_real_arm_8.sum(axis=1)/number_of_iteration
ax_real_data_8.plot(range(horizon), avg_forgetful_doubler_real_arm_8, 'b-',
                    label="Forgetful Doubler ")

forgetful_doubler_real_arm_16 = \
    np.load('Forgetful Doubler_Real_data_arms_16_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_real_arm_16.shape
avg_forgetful_doubler_real_arm_16 = forgetful_doubler_real_arm_16.sum(axis=1)/number_of_iteration
ax_real_data_16.plot(range(horizon), avg_forgetful_doubler_real_arm_16, 'b-',
                     label="Forgetful Doubler ")

forgetful_doubler_real_arm_46 = \
    np.load('Forgetful Doubler_Real_data_arms_46_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_real_arm_46.shape
avg_forgetful_doubler_real_arm_46 = forgetful_doubler_real_arm_46.sum(axis=1)/number_of_iteration
ax_real_data_46.plot(range(horizon), avg_forgetful_doubler_real_arm_46, 'b-',
                     label="Forgetful Doubler ")


#######################
# Improved Doubler TS #
#######################

improved_doubler_ts_one_strong_arm_8 = \
    np.load('Improved Doubler TS_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_one_strong_arm_8.shape
avg_improved_doubler_ts_one_strong_arm_8 = improved_doubler_ts_one_strong_arm_8.sum(axis=1)/number_of_iteration
ax_one_strong_arm_8.plot(range(horizon), avg_improved_doubler_ts_one_strong_arm_8, 'g-',
                         label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_one_strong_arm_16 = \
    np.load('Improved Doubler TS_Synthetic_data_One Strong Arm_arms_16_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_one_strong_arm_16.shape
avg_improved_doubler_ts_one_strong_arm_16 = improved_doubler_ts_one_strong_arm_16.sum(axis=1)/number_of_iteration
ax_one_strong_arm_16.plot(range(horizon), avg_improved_doubler_ts_one_strong_arm_16, 'g-',
                          label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_one_strong_arm_46 = \
    np.load('Improved Doubler TS_Synthetic_data_One Strong Arm_arms_46_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_one_strong_arm_46.shape
avg_improved_doubler_ts_one_strong_arm_46 = improved_doubler_ts_one_strong_arm_46.sum(axis=1)/number_of_iteration
ax_one_strong_arm_46.plot(range(horizon), avg_improved_doubler_ts_one_strong_arm_46, 'g-',
                          label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_close_arm_8 = \
    np.load('Improved Doubler TS_Synthetic_data_Close Arms_arms_8_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_close_arm_8.shape
avg_improved_doubler_ts_close_arm_8 = improved_doubler_ts_close_arm_8.sum(axis=1)/number_of_iteration
ax_close_arm_8.plot(range(horizon), avg_improved_doubler_ts_close_arm_8, 'g-',
                    label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_close_arm_16 = \
    np.load('Improved Doubler TS_Synthetic_data_Close Arms_arms_16_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_close_arm_16.shape
avg_improved_doubler_ts_close_arm_16 = improved_doubler_ts_close_arm_16.sum(axis=1)/number_of_iteration
ax_close_arm_16.plot(range(horizon), avg_improved_doubler_ts_close_arm_16, 'g-',
                     label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_close_arm_46 = \
    np.load('Improved Doubler TS_Synthetic_data_Close Arms_arms_46_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_close_arm_46.shape
avg_improved_doubler_ts_close_arm_46 = improved_doubler_ts_close_arm_46.sum(axis=1)/number_of_iteration
ax_close_arm_46.plot(range(horizon), avg_improved_doubler_ts_close_arm_46, 'g-',
                     label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_linear_arm_8 = \
    np.load('Improved Doubler TS_Synthetic_data_Linear List_arms_8_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_linear_arm_8.shape
avg_improved_doubler_ts_linear_arm_8 = improved_doubler_ts_linear_arm_8.sum(axis=1)/number_of_iteration
ax_linear_arm_8.plot(range(horizon), avg_improved_doubler_ts_linear_arm_8, 'g-',
                     label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_linear_arm_16 = \
    np.load('Improved Doubler TS_Synthetic_data_Linear List_arms_16_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_linear_arm_16.shape
avg_improved_doubler_ts_linear_arm_16 = improved_doubler_ts_linear_arm_16.sum(axis=1)/number_of_iteration
ax_linear_arm_16.plot(range(horizon), avg_improved_doubler_ts_linear_arm_16, 'g-',
                      label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_linear_arm_46 = \
    np.load('Improved Doubler TS_Synthetic_data_Linear List_arms_46_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_linear_arm_46.shape
avg_improved_doubler_ts_linear_arm_46 = improved_doubler_ts_linear_arm_46.sum(axis=1)/number_of_iteration
ax_linear_arm_46.plot(range(horizon), avg_improved_doubler_ts_linear_arm_46, 'g-',
                      label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_random_arm_8 = \
    np.load('Improved Doubler TS_Synthetic_data_Random_arms_8_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_random_arm_8.shape
avg_improved_doubler_ts_random_arm_8 = improved_doubler_ts_random_arm_8.sum(axis=1)/number_of_iteration
ax_random_data_8.plot(range(horizon), avg_improved_doubler_ts_random_arm_8, 'g-',
                      label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_random_arm_16 = \
    np.load('Improved Doubler TS_Synthetic_data_Random_arms_16_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_random_arm_16.shape
avg_improved_doubler_ts_random_arm_16 = improved_doubler_ts_random_arm_16.sum(axis=1)/number_of_iteration
ax_random_data_16.plot(range(horizon), avg_improved_doubler_ts_random_arm_16, 'g-',
                       label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_random_arm_46 = \
    np.load('Improved Doubler TS_Synthetic_data_Random_arms_46_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_random_arm_46.shape
avg_improved_doubler_ts_random_arm_46 = improved_doubler_ts_random_arm_46.sum(axis=1)/number_of_iteration
ax_random_data_46.plot(range(horizon), avg_improved_doubler_ts_random_arm_46, 'g-',
                       label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_real_arm_8 = \
    np.load('Improved Doubler TS_Real_data_arms_8_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_real_arm_8.shape
avg_improved_doubler_ts_real_arm_8 = improved_doubler_ts_real_arm_8.sum(axis=1)/number_of_iteration
ax_real_data_8.plot(range(horizon), avg_improved_doubler_ts_real_arm_8, 'g-',
                    label="Improved Doubler Thompson Sampling ")

improved_doubler_ts_real_arm_16 = \
    np.load('Improved Doubler TS_Real_data_arms_16_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_real_arm_16.shape
avg_improved_doubler_ts_real_arm_16 = improved_doubler_ts_real_arm_16.sum(axis=1)/number_of_iteration
ax_real_data_16.plot(range(horizon), avg_improved_doubler_ts_real_arm_16, 'g-',
                     label="Improved Doubler Thompson Sampling ")

# improved_doubler_ts_real_arm_46 = \
#     np.load('Improved Doubler TS_Real_data_Random_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = improved_doubler_ts_real_arm_46.shape
# avg_improved_doubler_ts_real_arm_46 = improved_doubler_ts_real_arm_46.sum(axis=1)/number_of_iteration
# ax_real_data_46.plot(range(horizon), avg_improved_doubler_ts_real_arm_46, 'g-',
#                      label="Improved Doubler Thompson Sampling ")

####################
# Improved Doubler #
####################

improved_doubler_one_strong_arm_8 = \
    np.load('Improved Doubler_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_one_strong_arm_8.shape
avg_improved_doubler_one_strong_arm_8 = improved_doubler_one_strong_arm_8.sum(axis=1)/number_of_iteration
ax_one_strong_arm_8.plot(range(horizon), avg_improved_doubler_one_strong_arm_8, 'r-',
                         label="Improved Doubler ")

improved_doubler_one_strong_arm_16 = \
    np.load('Improved Doubler_Synthetic_data_One Strong Arm_arms_16_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_one_strong_arm_16.shape
avg_improved_doubler_one_strong_arm_16 = improved_doubler_one_strong_arm_16.sum(axis=1)/number_of_iteration
ax_one_strong_arm_16.plot(range(horizon), avg_improved_doubler_one_strong_arm_16, 'r-',
                          label="Improved Doubler ")

improved_doubler_one_strong_arm_46 = \
    np.load('Improved Doubler_Synthetic_data_One Strong Arm_arms_46_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_one_strong_arm_46.shape
avg_improved_doubler_one_strong_arm_46 = improved_doubler_one_strong_arm_46.sum(axis=1)/number_of_iteration
ax_one_strong_arm_46.plot(range(horizon), avg_improved_doubler_one_strong_arm_46, 'r-',
                          label="Improved Doubler ")

improved_doubler_close_arm_8 = \
    np.load('Improved Doubler_Synthetic_data_Close Arms_arms_8_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_close_arm_8.shape
avg_improved_doubler_close_arm_8 = improved_doubler_close_arm_8.sum(axis=1)/number_of_iteration
ax_close_arm_8.plot(range(horizon), avg_improved_doubler_close_arm_8, 'r-',
                    label="Improved Doubler ")

improved_doubler_close_arm_16 = \
    np.load('Improved Doubler_Synthetic_data_Close Arms_arms_16_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_close_arm_16.shape
avg_improved_doubler_close_arm_16 = improved_doubler_close_arm_16.sum(axis=1)/number_of_iteration
ax_close_arm_16.plot(range(horizon), avg_improved_doubler_close_arm_16, 'r-',
                     label="Improved Doubler ")

improved_doubler_close_arm_46 = \
    np.load('Improved Doubler_Synthetic_data_Close Arms_arms_46_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_close_arm_46.shape
avg_improved_doubler_close_arm_46 = improved_doubler_close_arm_46.sum(axis=1)/number_of_iteration
ax_close_arm_46.plot(range(horizon), avg_improved_doubler_close_arm_46, 'r-',
                     label="Improved Doubler ")

improved_doubler_linear_arm_8 = \
    np.load('Improved Doubler_Synthetic_data_Linear List_arms_8_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_linear_arm_8.shape
avg_improved_doubler_linear_arm_8 = improved_doubler_linear_arm_8.sum(axis=1)/number_of_iteration
ax_linear_arm_8.plot(range(horizon), avg_improved_doubler_linear_arm_8, 'r-',
                     label="Improved Doubler ")

improved_doubler_linear_arm_16 = \
    np.load('Improved Doubler_Synthetic_data_Linear List_arms_16_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_linear_arm_16.shape
avg_improved_doubler_linear_arm_16 = improved_doubler_linear_arm_16.sum(axis=1)/number_of_iteration
ax_linear_arm_16.plot(range(horizon), avg_improved_doubler_linear_arm_16, 'r-',
                      label="Improved Doubler ")

improved_doubler_linear_arm_46 = \
    np.load('Improved Doubler_Synthetic_data_Linear List_arms_46_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_linear_arm_46.shape
avg_improved_doubler_linear_arm_46 = improved_doubler_linear_arm_46.sum(axis=1)/number_of_iteration
ax_linear_arm_46.plot(range(horizon), avg_improved_doubler_linear_arm_46, 'r-',
                      label="Improved Doubler ")

improved_doubler_random_arm_8 = \
    np.load('Improved Doubler_Synthetic_data_Random_arms_8_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_random_arm_8.shape
avg_improved_doubler_random_arm_8 = improved_doubler_random_arm_8.sum(axis=1)/number_of_iteration
ax_random_data_8.plot(range(horizon), avg_improved_doubler_random_arm_8, 'r-',
                      label="Improved Doubler ")

improved_doubler_random_arm_16 = \
    np.load('Improved Doubler_Synthetic_data_Random_arms_16_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_random_arm_16.shape
avg_improved_doubler_random_arm_16 = improved_doubler_random_arm_16.sum(axis=1)/number_of_iteration
ax_random_data_16.plot(range(horizon), avg_improved_doubler_random_arm_16, 'r-',
                       label="Improved Doubler ")

improved_doubler_random_arm_46 = \
    np.load('Improved Doubler_Synthetic_data_Random_arms_46_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_random_arm_46.shape
avg_improved_doubler_random_arm_46 = improved_doubler_random_arm_46.sum(axis=1)/number_of_iteration
ax_random_data_46.plot(range(horizon), avg_improved_doubler_random_arm_46, 'r-',
                       label="Improved Doubler ")

improved_doubler_real_arm_8 = \
    np.load('Improved Doubler_Real_data_arms_8_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_real_arm_8.shape
avg_improved_doubler_real_arm_8 = improved_doubler_real_arm_8.sum(axis=1)/number_of_iteration
ax_real_data_8.plot(range(horizon), avg_improved_doubler_real_arm_8, 'r-',
                    label="Improved Doubler ")

improved_doubler_real_arm_16 = \
    np.load('Improved Doubler_Real_data_arms_16_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_real_arm_16.shape
avg_improved_doubler_real_arm_16 = improved_doubler_real_arm_16.sum(axis=1)/number_of_iteration
ax_real_data_16.plot(range(horizon), avg_improved_doubler_real_arm_16, 'r-',
                     label="Improved Doubler ")

improved_doubler_real_arm_46 = \
    np.load('Improved Doubler_Real_data_arms_46_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_real_arm_46.shape
avg_improved_doubler_real_arm_46 = improved_doubler_real_arm_46.sum(axis=1)/number_of_iteration
ax_real_data_46.plot(range(horizon), avg_improved_doubler_real_arm_46, 'r-',
                     label="Improved Doubler ")

#######
# RCS #
#######

rcs_one_strong_arm_8 = \
    np.load('RCS_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
horizon, number_of_iteration = rcs_one_strong_arm_8.shape
avg_rcs_one_strong_arm_8 = rcs_one_strong_arm_8.sum(axis=1)/number_of_iteration
ax_one_strong_arm_8.plot(range(horizon), avg_rcs_one_strong_arm_8, 'c-',
                         label="RCS ")

# rcs_one_strong_arm_16 = \
#     np.load('RCS_Synthetic_data_One Strong Arm_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = rcs_one_strong_arm_16.shape
# avg_rcs_one_strong_arm_16 = rcs_one_strong_arm_16.sum(axis=1)/number_of_iteration
# ax_one_strong_arm_16.plot(range(horizon), avg_rcs_one_strong_arm_16, 'c-',
#                           label="RCS ")
#
# rcs_one_strong_arm_46 = \
#     np.load('RCS_Synthetic_data_One Strong Arm_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = rcs_one_strong_arm_46.shape
# avg_rcs_one_strong_arm_46 = rcs_one_strong_arm_46.sum(axis=1)/number_of_iteration
# ax_one_strong_arm_46.plot(range(horizon), avg_rcs_one_strong_arm_46, 'c-',
#                           label="RCS ")

# rcs_close_arm_8 = \
#     np.load('RCS_Synthetic_data_Close Arms_arms_8_horizon_131072.npy')
# horizon, number_of_iteration = rcs_close_arm_8.shape
# avg_rcs_close_arm_8 = rcs_close_arm_8.sum(axis=1)/number_of_iteration
# ax_close_arm_8.plot(range(horizon), avg_rcs_close_arm_8, 'c-',
#                     label="RCS ")

# rcs_close_arm_16 = \
#     np.load('RCS_Synthetic_data_Close Arms_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = rcs_close_arm_16.shape
# avg_rcs_close_arm_16 = rcs_close_arm_16.sum(axis=1)/number_of_iteration
# ax_close_arm_16.plot(range(horizon), avg_rcs_close_arm_16, 'c-',
#                      label="RCS ")

# rcs_close_arm_46 = \
#     np.load('RCS_Synthetic_data_Close Arms_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = rcs_close_arm_46.shape
# avg_rcs_close_arm_46 = rcs_close_arm_46.sum(axis=1)/number_of_iteration
# ax_close_arm_46.plot(range(horizon), avg_rcs_close_arm_46, 'c-',
#                      label="RCS ")

rcs_linear_arm_8 = \
    np.load('RCS_Synthetic_data_Linear List_arms_8_horizon_131072.npy')
horizon, number_of_iteration = rcs_linear_arm_8.shape
avg_rcs_linear_arm_8 = rcs_linear_arm_8.sum(axis=1)/number_of_iteration
ax_linear_arm_8.plot(range(horizon), avg_rcs_linear_arm_8, 'c-',
                     label="RCS ")

# rcs_linear_arm_16 = \
#     np.load('RCS_Synthetic_data_Linear List_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = rcs_linear_arm_16.shape
# avg_rcs_linear_arm_16 = rcs_linear_arm_16.sum(axis=1)/number_of_iteration
# ax_linear_arm_16.plot(range(horizon), avg_rcs_linear_arm_16, 'c-',
#                       label="RCS ")

# rcs_linear_arm_46 = \
#     np.load('RCS_Synthetic_data_Linear List_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = rcs_linear_arm_46.shape
# avg_rcs_linear_arm_46 = rcs_linear_arm_46.sum(axis=1)/number_of_iteration
# ax_linear_arm_46.plot(range(horizon), avg_rcs_linear_arm_46, 'c-',
#                       label="RCS ")

rcs_random_arm_8 = \
    np.load('RCS_Synthetic_data_Random_arms_8_horizon_131072.npy')
horizon, number_of_iteration = rcs_random_arm_8.shape
avg_rcs_random_arm_8 = rcs_random_arm_8.sum(axis=1)/number_of_iteration
ax_random_data_8.plot(range(horizon), avg_rcs_random_arm_8, 'c-',
                      label="RCS ")

# rcs_random_arm_16 = \
#     np.load('RCS_Synthetic_data_Random_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = rcs_random_arm_16.shape
# avg_rcs_random_arm_16 = rcs_random_arm_16.sum(axis=1)/number_of_iteration
# ax_random_data_16.plot(range(horizon), avg_rcs_random_arm_16, 'c-',
#                        label="RCS ")
#
# rcs_random_arm_46 = \
#     np.load('RCS_Synthetic_data_Random_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = rcs_random_arm_46.shape
# avg_rcs_random_arm_46 = rcs_random_arm_46.sum(axis=1)/number_of_iteration
# ax_random_data_46.plot(range(horizon), avg_rcs_random_arm_46, 'c-',
#                        label="RCS ")

rcs_real_arm_8 = \
    np.load('RCS_Real_data_arms_8_horizon_131072.npy')
horizon, number_of_iteration = rcs_real_arm_8.shape
avg_rcs_real_arm_8 = rcs_real_arm_8.sum(axis=1)/number_of_iteration
ax_real_data_8.plot(range(horizon), avg_rcs_real_arm_8, 'c-',
                    label="RCS ")

# rcs_real_arm_16 = \
#     np.load('RCS_Real_data_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = rcs_real_arm_16.shape
# avg_rcs_real_arm_16 = rcs_real_arm_16.sum(axis=1)/number_of_iteration
# ax_real_data_16.plot(range(horizon), avg_rcs_real_arm_16, 'c-',
#                      label="RCS ")
#
# rcs_real_arm_46 = \
#     np.load('RCS_Real_data_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = rcs_real_arm_46.shape
# avg_rcs_real_arm_46 = rcs_real_arm_46.sum(axis=1)/number_of_iteration
# ax_real_data_46.plot(range(horizon), avg_rcs_real_arm_46, 'c-',
#                      label="RCS ")


########
# RUCB #
########

rucb_one_strong_arm_8 = \
    np.load('RUCB_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
horizon, number_of_iteration = rucb_one_strong_arm_8.shape
avg_rucb_one_strong_arm_8 = rucb_one_strong_arm_8.sum(axis=1)/number_of_iteration
ax_one_strong_arm_8.plot(range(horizon), avg_rucb_one_strong_arm_8, 'm-',
                         label="RUCB ")

rucb_one_strong_arm_16 = \
    np.load('RUCB_Synthetic_data_One Strong Arm_arms_16_horizon_131072.npy')
horizon, number_of_iteration = rucb_one_strong_arm_16.shape
avg_rucb_one_strong_arm_16 = rucb_one_strong_arm_16.sum(axis=1)/number_of_iteration
ax_one_strong_arm_16.plot(range(horizon), avg_rucb_one_strong_arm_16, 'm-',
                          label="RUCB ")

rucb_one_strong_arm_46 = \
    np.load('RUCB_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
horizon, number_of_iteration = rucb_one_strong_arm_46.shape
avg_rucb_one_strong_arm_46 = rucb_one_strong_arm_46.sum(axis=1)/number_of_iteration
ax_one_strong_arm_46.plot(range(horizon), avg_rucb_one_strong_arm_46, 'm-',
                          label="RUCB ")

rucb_close_arm_8 = \
    np.load('RUCB_Synthetic_data_Close Arms_arms_8_horizon_131072.npy')
horizon, number_of_iteration = rucb_close_arm_8.shape
avg_rucb_close_arm_8 = rucb_close_arm_8.sum(axis=1)/number_of_iteration
ax_close_arm_8.plot(range(horizon), avg_rucb_close_arm_8, 'm-',
                    label="RUCB ")

rucb_close_arm_16 = \
    np.load('RUCB_Synthetic_data_Close Arms_arms_16_horizon_131072.npy')
horizon, number_of_iteration = rucb_close_arm_16.shape
avg_rucb_close_arm_16 = rucb_close_arm_16.sum(axis=1)/number_of_iteration
ax_close_arm_16.plot(range(horizon), avg_rucb_close_arm_16, 'm-',
                     label="RUCB ")

rucb_close_arm_46 = \
    np.load('RUCB_Synthetic_data_Close Arms_arms_46_horizon_131072.npy')
horizon, number_of_iteration = rucb_close_arm_46.shape
avg_rucb_close_arm_46 = rucb_close_arm_46.sum(axis=1)/number_of_iteration
ax_close_arm_46.plot(range(horizon), avg_rucb_close_arm_46, 'm-',
                     label="RUCB ")

rucb_linear_arm_8 = \
    np.load('RUCB_Synthetic_data_Linear List_arms_8_horizon_131072.npy')
horizon, number_of_iteration = rucb_linear_arm_8.shape
avg_rucb_linear_arm_8 = rucb_linear_arm_8.sum(axis=1)/number_of_iteration
ax_linear_arm_8.plot(range(horizon), avg_rucb_linear_arm_8, 'm-',
                     label="RUCB ")

rucb_linear_arm_16 = \
    np.load('RUCB_Synthetic_data_Linear List_arms_16_horizon_131072.npy')
horizon, number_of_iteration = rucb_linear_arm_16.shape
avg_rucb_linear_arm_16 = rucb_linear_arm_16.sum(axis=1)/number_of_iteration
ax_linear_arm_16.plot(range(horizon), avg_rucb_linear_arm_16, 'm-',
                      label="RUCB ")

rucb_linear_arm_46 = \
    np.load('RUCB_Synthetic_data_Linear List_arms_46_horizon_131072.npy')
horizon, number_of_iteration = rucb_linear_arm_46.shape
avg_rucb_linear_arm_46 = rucb_linear_arm_46.sum(axis=1)/number_of_iteration
ax_linear_arm_46.plot(range(horizon), avg_rucb_linear_arm_46, 'm-',
                      label="RUCB ")

rucb_random_arm_8 = \
    np.load('RUCB_Synthetic_data_Random_arms_8_horizon_131072.npy')
horizon, number_of_iteration = rucb_random_arm_8.shape
avg_rucb_random_arm_8 = rucb_random_arm_8.sum(axis=1)/number_of_iteration
ax_random_data_8.plot(range(horizon), avg_rucb_random_arm_8, 'm-',
                      label="RUCB ")

rucb_random_arm_16 = \
    np.load('RUCB_Synthetic_data_Random_arms_16_horizon_131072.npy')
horizon, number_of_iteration = rucb_random_arm_16.shape
avg_rucb_random_arm_16 = rucb_random_arm_16.sum(axis=1)/number_of_iteration
ax_random_data_16.plot(range(horizon), avg_rucb_random_arm_16, 'm-',
                       label="RUCB ")

rucb_random_arm_46 = \
    np.load('RUCB_Synthetic_data_Random_arms_46_horizon_131072.npy')
horizon, number_of_iteration = rucb_random_arm_46.shape
avg_rucb_random_arm_46 = rucb_random_arm_46.sum(axis=1)/number_of_iteration
ax_random_data_46.plot(range(horizon), avg_rucb_random_arm_46, 'm-',
                       label="RUCB ")

rucb_real_arm_8 = \
    np.load('RUCB_Real_data_arms_8_horizon_131072.npy')
horizon, number_of_iteration = rucb_real_arm_8.shape
avg_rucb_real_arm_8 = rucb_real_arm_8.sum(axis=1)/number_of_iteration
ax_real_data_8.plot(range(horizon), avg_rucb_real_arm_8, 'm-',
                    label="RUCB ")

rucb_real_arm_16 = \
    np.load('RUCB_Real_data_arms_16_horizon_131072.npy')
horizon, number_of_iteration = rucb_real_arm_16.shape
avg_rucb_real_arm_16 = rucb_real_arm_16.sum(axis=1)/number_of_iteration
ax_real_data_16.plot(range(horizon), avg_rucb_real_arm_16, 'm-',
                     label="RUCB ")

rucb_real_arm_46 = \
    np.load('RUCB_Real_data_arms_46_horizon_131072.npy')
horizon, number_of_iteration = rucb_real_arm_46.shape
avg_rucb_real_arm_46 = rucb_real_arm_46.sum(axis=1)/number_of_iteration
ax_real_data_46.plot(range(horizon), avg_rucb_real_arm_46, 'm-',
                     label="RUCB ")

##########
# SAVAGE #
##########
#
# savage_one_strong_arm_8 = \
#     np.load('SAVAGE_Synthetic_data_One Strong Arm_arms_8_horizon_131072.npy')
# horizon, number_of_iteration = savage_one_strong_arm_8.shape
# avg_savage_one_strong_arm_8 = savage_one_strong_arm_8.sum(axis=1)/number_of_iteration
# ax_one_strong_arm_8.plot(range(horizon), avg_savage_one_strong_arm_8, 'k-',
#                          label="SAVAGE ")

# savage_one_strong_arm_16 = \
#     np.load('SAVAGE_Synthetic_data_One Strong Arm_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = savage_one_strong_arm_16.shape
# avg_savage_one_strong_arm_16 = savage_one_strong_arm_16.sum(axis=1)/number_of_iteration
# ax_one_strong_arm_16.plot(range(horizon), avg_savage_one_strong_arm_16, 'k-',
#                           label="SAVAGE ")

# savage_one_strong_arm_46 = \
#     np.load('SAVAGE_Synthetic_data_One Strong Arm_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = savage_one_strong_arm_46.shape
# avg_savage_one_strong_arm_46 = savage_one_strong_arm_46.sum(axis=1)/number_of_iteration
# ax_one_strong_arm_46.plot(range(horizon), avg_savage_one_strong_arm_46, 'k-',
#                           label="SAVAGE ")

savage_close_arm_8 = \
    np.load('SAVAGE_Synthetic_data_Close Arms_arms_8_horizon_131072.npy')
horizon, number_of_iteration = savage_close_arm_8.shape
avg_savage_close_arm_8 = savage_close_arm_8.sum(axis=1)/number_of_iteration
ax_close_arm_8.plot(range(horizon), avg_savage_close_arm_8, 'k-',
                    label="SAVAGE ")

# savage_close_arm_16 = \
#     np.load('SAVAGE_Synthetic_data_Close Arms_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = savage_close_arm_16.shape
# avg_savage_close_arm_16 = savage_close_arm_16.sum(axis=1)/number_of_iteration
# ax_close_arm_16.plot(range(horizon), avg_savage_close_arm_16, 'k-',
#                      label="SAVAGE ")

# savage_close_arm_46 = \
#     np.load('SAVAGE_Synthetic_data_Close Arms_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = savage_close_arm_46.shape
# avg_savage_close_arm_46 = savage_close_arm_46.sum(axis=1)/number_of_iteration
# ax_close_arm_46.plot(range(horizon), avg_savage_close_arm_46, 'k-',
#                      label="SAVAGE ")

savage_linear_arm_8 = \
    np.load('SAVAGE_Synthetic_data_Linear List_arms_8_horizon_131072.npy')
horizon, number_of_iteration = savage_linear_arm_8.shape
avg_savage_linear_arm_8 = savage_linear_arm_8.sum(axis=1)/number_of_iteration
ax_linear_arm_8.plot(range(horizon), avg_savage_linear_arm_8, 'k-',
                     label="SAVAGE ")

# savage_linear_arm_16 = \
#     np.load('SAVAGE_Synthetic_data_Linear List_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = savage_linear_arm_16.shape
# avg_savage_linear_arm_16 = savage_linear_arm_16.sum(axis=1)/number_of_iteration
# ax_linear_arm_16.plot(range(horizon), avg_savage_linear_arm_16, 'k-',
#                       label="SAVAGE ")

# savage_linear_arm_46 = \
#     np.load('SAVAGE_Synthetic_data_Linear List_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = savage_linear_arm_46.shape
# avg_savage_linear_arm_46 = savage_linear_arm_46.sum(axis=1)/number_of_iteration
# ax_linear_arm_46.plot(range(horizon), avg_savage_linear_arm_46, 'k-',
#                       label="SAVAGE ")

savage_random_arm_8 = \
    np.load('SAVAGE_Synthetic_data_Random_arms_8_horizon_131072.npy')
horizon, number_of_iteration = savage_random_arm_8.shape
avg_savage_random_arm_8 = savage_random_arm_8.sum(axis=1)/number_of_iteration
ax_random_data_8.plot(range(horizon), avg_savage_random_arm_8, 'k-',
                      label="SAVAGE Synthetic data Random Arm")

# savage_random_arm_16 = \
#     np.load('SAVAGE_Synthetic_data_Random_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = savage_random_arm_16.shape
# avg_savage_random_arm_16 = savage_random_arm_16.sum(axis=1)/number_of_iteration
# ax_random_data_16.plot(range(horizon), avg_savage_random_arm_16, 'k-',
#                        label="SAVAGE Synthetic data Random Arm")
#
# savage_random_arm_46 = \
#     np.load('SAVAGE_Synthetic_data_Random_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = savage_random_arm_46.shape
# avg_savage_random_arm_46 = savage_random_arm_46.sum(axis=1)/number_of_iteration
# ax_random_data_46.plot(range(horizon), avg_savage_random_arm_46, 'k-',
#                        label="SAVAGE Synthetic data Random Arm")

#
# savage_real_arm_8 = \
#     np.load('SAVAGE_Real_data_arms_8_horizon_131072.npy')
# horizon, number_of_iteration = savage_real_arm_8.shape
# avg_savage_real_arm_8 = savage_real_arm_8.sum(axis=1)/number_of_iteration
# ax_real_data_8.plot(range(horizon), avg_savage_real_arm_8, 'k-',
#                     label="SAVAGE Real data Arm")
#
# savage_real_arm_16 = \
#     np.load('SAVAGE_Real_data_arms_16_horizon_131072.npy')
# horizon, number_of_iteration = savage_real_arm_16.shape
# avg_savage_real_arm_16 = savage_real_arm_16.sum(axis=1)/number_of_iteration
# ax_real_data_16.plot(range(horizon), avg_savage_real_arm_16, 'k-',
#                      label="SAVAGE Real data Arm")
#
# savage_real_arm_46 = \
#     np.load('SAVAGE_Real_data_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = savage_real_arm_46.shape
# avg_savage_real_arm_46 = savage_real_arm_46.sum(axis=1)/number_of_iteration
# ax_real_data_46.plot(range(horizon), avg_savage_real_arm_46, 'k-',
#                      label="SAVAGE Real data Arm")

############################
# Plotting all the results #
############################

box_one_strong_arm_8 = ax_one_strong_arm_8.get_position()

ax_one_strong_arm_8.set_position(
    [box_one_strong_arm_8.x0,
     box_one_strong_arm_8.y0 + box_one_strong_arm_8.height * 0.3,
     box_one_strong_arm_8.width,
     box_one_strong_arm_8.height * 0.7])

ax_one_strong_arm_8.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_one_strong_arm_8.savefig("one_strong_arm_8.png", bbox_inches='tight')

box_one_strong_arm_16 = ax_one_strong_arm_16.get_position()

ax_one_strong_arm_16.set_position(
    [box_one_strong_arm_16.x0,
     box_one_strong_arm_16.y0 + box_one_strong_arm_16.height * 0.3,
     box_one_strong_arm_16.width,
     box_one_strong_arm_16.height * 0.7])

ax_one_strong_arm_16.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_one_strong_arm_16.savefig("one_strong_arm_16.png", bbox_inches='tight')

box_one_strong_arm_46 = ax_one_strong_arm_46.get_position()

ax_one_strong_arm_46.set_position(
    [box_one_strong_arm_46.x0,
     box_one_strong_arm_46.y0 + box_one_strong_arm_46.height * 0.3,
     box_one_strong_arm_46.width,
     box_one_strong_arm_46.height * 0.7])

ax_one_strong_arm_46.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_one_strong_arm_46.savefig("one_strong_arm_46.png", bbox_inches='tight')

box_close_arm_8 = ax_close_arm_8.get_position()

ax_close_arm_8.set_position(
    [box_close_arm_8.x0,
     box_close_arm_8.y0 + box_close_arm_8.height * 0.3,
     box_close_arm_8.width,
     box_close_arm_8.height * 0.8])

ax_close_arm_8.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_close_arm_8.savefig("close_arm_8.png", bbox_inches='tight')

box_close_arm_16 = ax_close_arm_16.get_position()

ax_close_arm_16.set_position(
    [box_close_arm_16.x0,
     box_close_arm_16.y0 + box_close_arm_16.height * 0.3,
     box_close_arm_16.width,
     box_close_arm_16.height * 0.7])

ax_close_arm_16.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_close_arm_16.savefig("close_arm_16.png", bbox_inches='tight')

box_close_arm_46 = ax_close_arm_46.get_position()

ax_close_arm_46.set_position(
    [box_close_arm_46.x0,
     box_close_arm_46.y0 + box_close_arm_46.height * 0.3,
     box_close_arm_46.width,
     box_close_arm_46.height * 0.7])

ax_close_arm_46.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_close_arm_46.savefig("close_arm_46.png", bbox_inches='tight')

box_linear_arm_8 = ax_linear_arm_8.get_position()

ax_linear_arm_8.set_position(
    [box_linear_arm_8.x0,
     box_linear_arm_8.y0 + box_linear_arm_8.height * 0.3,
     box_linear_arm_8.width,
     box_linear_arm_8.height * 0.7])

ax_linear_arm_8.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_linear_arm_8.savefig("linear_arm_8.png", bbox_inches='tight')

box_linear_arm_16 = ax_linear_arm_16.get_position()

ax_linear_arm_16.set_position(
    [box_linear_arm_16.x0,
     box_linear_arm_16.y0 + box_linear_arm_16.height * 0.3,
     box_linear_arm_16.width,
     box_linear_arm_16.height * 0.7])

ax_linear_arm_16.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_linear_arm_16.savefig("linear_arm_16.png", bbox_inches='tight')

box_linear_arm_46 = ax_linear_arm_46.get_position()

ax_linear_arm_46.set_position(
    [box_linear_arm_46.x0,
     box_linear_arm_46.y0 + box_linear_arm_46.height * 0.3,
     box_linear_arm_46.width,
     box_linear_arm_46.height * 0.7])

ax_linear_arm_46.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_linear_arm_46.savefig("linear_arm_46.png", bbox_inches='tight')

box_random_arm_8 = ax_random_data_8.get_position()

ax_random_data_8.set_position(
    [box_random_arm_8.x0,
     box_random_arm_8.y0 + box_random_arm_8.height * 0.3,
     box_random_arm_8.width,
     box_random_arm_8.height * 0.8])

ax_random_data_8.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_random_data_8.savefig("random_data_8.png", bbox_inches='tight')

box_random_arm_16 = ax_random_data_16.get_position()

ax_random_data_16.set_position(
    [box_random_arm_16.x0,
     box_random_arm_16.y0 + box_random_arm_16.height * 0.3,
     box_random_arm_16.width,
     box_random_arm_16.height * 0.7])

ax_random_data_16.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_random_data_16.savefig("random_data_16.png", bbox_inches='tight')

box_random_arm_46 = ax_random_data_46.get_position()

ax_random_data_46.set_position(
    [box_random_arm_46.x0,
     box_random_arm_46.y0 + box_random_arm_46.height * 0.3,
     box_random_arm_46.width,
     box_random_arm_46.height * 0.7])

ax_random_data_46.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_random_data_46.savefig("random_data_46.png", bbox_inches='tight')

box_real_arm_8 = ax_real_data_8.get_position()

ax_real_data_8.set_position(
    [box_real_arm_8.x0,
     box_real_arm_8.y0 + box_real_arm_8.height * 0.3,
     box_real_arm_8.width,
     box_real_arm_8.height * 0.7])

ax_real_data_8.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_real_data_8.savefig("real_data_8.png", bbox_inches='tight')

box_real_arm_16 = ax_real_data_16.get_position()

ax_real_data_16.set_position(
    [box_real_arm_16.x0,
     box_real_arm_16.y0 + box_real_arm_16.height * 0.3,
     box_real_arm_16.width,
     box_real_arm_16.height * 0.7])

ax_real_data_16.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_real_data_16.savefig("real_data_16.png", bbox_inches='tight')

box_real_arm_46 = ax_real_data_46.get_position()

ax_real_data_46.set_position(
    [box_real_arm_46.x0,
     box_real_arm_46.y0 + box_real_arm_46.height * 0.3,
     box_real_arm_46.width,
     box_real_arm_46.height * 0.7])

ax_real_data_46.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_real_data_46.savefig("real_data_46.png", bbox_inches='tight')

# plt.show()
