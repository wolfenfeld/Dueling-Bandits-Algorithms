__author__ = 'wolfenfeld'
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

fontP = FontProperties()
fontP.set_size('small')

###############
# The figures #
###############

# Real Data - 46 arms
fig_real_data_46 = plt.figure()
ax_real_data_46 = plt.subplot(111)


####################
# Balanced Doubler #
####################

# # Real arms - 46 arms
# balanced_doubler_real_arm_46 = \
#     np.load('Balanced Doubler_Real_data_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = balanced_doubler_real_arm_46.shape
# avg_balanced_doubler_real_arm_46 = balanced_doubler_real_arm_46.sum(axis=1)/number_of_iteration
# ax_real_data_46.plot(range(horizon), avg_balanced_doubler_real_arm_46, 'b--',
#                      label="Balanced Doubler Real data Random Arms")

############
# Sparring #
############

# sparring_real_arm_46 = \
#     np.load('Sparring_Real_data_Random_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = sparring_real_arm_46.shape
# avg_sparring_real_arm_46 = sparring_real_arm_46.sum(axis=1)/number_of_iteration
# ax_real_data_46.plot(range(horizon), avg_sparring_real_arm_46, 'g--',
#                      label="Sparring")


###############
# Sparring TS #
###############

sparring_ts_real_arm_46 = \
    np.load('Sparring TS_Real_data_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_real_arm_46.shape

sample = np.linspace(1, horizon-1, num=10, dtype=int)

avg_sparring_ts_real_arm_46 = sparring_ts_real_arm_46.sum(axis=1)/number_of_iteration
std_sparring_ts_real_arm_46 = sparring_ts_real_arm_46.std(axis=1)

plt.errorbar(sample, avg_sparring_ts_real_arm_46[sample], std_sparring_ts_real_arm_46[sample], linestyle='None')
ax_real_data_46.plot(range(horizon), avg_sparring_ts_real_arm_46, 'r--',
                     label="Sparring Thompson Sampling")

#####################
# Sparring TS Turbo #
#####################

sparring_ts_turbo_real_arm_46 = \
    np.load('Sparring TS Turbo_Real_data_arms_46_horizon_131072.npy')
horizon, number_of_iteration = sparring_ts_turbo_real_arm_46.shape
sample = np.linspace(1, horizon-1, num=10, dtype=int)

avg_sparring_ts_turbo_real_arm_46 = sparring_ts_turbo_real_arm_46.sum(axis=1)/number_of_iteration
std_sparring_ts_turbo_real_arm_46 = sparring_ts_turbo_real_arm_46.std(axis=1)

plt.errorbar(sample, avg_sparring_ts_turbo_real_arm_46[sample], std_sparring_ts_turbo_real_arm_46[sample], linestyle='None')

ax_real_data_46.plot(range(horizon), avg_sparring_ts_turbo_real_arm_46, 'c--',
                     label="Sparring TS Turbo")

###########
# Doubler #
###########

doubler_real_arm_46 = \
    np.load('Doubler_Real_data_arms_46_horizon_131072.npy')
horizon, number_of_iteration = doubler_real_arm_46.shape
sample = np.linspace(1, horizon-1, num=10, dtype=int)
avg_doubler_real_arm_46 = doubler_real_arm_46.sum(axis=1)/number_of_iteration
std_doubler_real_arm_46 = doubler_real_arm_46.std(axis=1)

plt.errorbar(sample, avg_doubler_real_arm_46[sample], std_doubler_real_arm_46[sample], linestyle='None')

ax_real_data_46.plot(range(horizon), avg_doubler_real_arm_46, 'k--',
                     label="Doubler")

######################
# Forgetful Doubler #
######################

forgetful_doubler_real_arm_46 = \
    np.load('Forgetful Doubler_Real_data_arms_46_horizon_131072.npy')
horizon, number_of_iteration = forgetful_doubler_real_arm_46.shape
sample = np.linspace(1, horizon-1, num=10, dtype=int)

avg_forgetful_doubler_real_arm_46 = forgetful_doubler_real_arm_46.sum(axis=1)/number_of_iteration
std_forgetful_doubler_real_arm_46 = forgetful_doubler_real_arm_46.std(axis=1)

plt.errorbar(sample, avg_forgetful_doubler_real_arm_46[sample], std_forgetful_doubler_real_arm_46[sample], linestyle='None')
ax_real_data_46.plot(range(horizon), avg_forgetful_doubler_real_arm_46, 'b-',
                     label="Forgetful Doubler")

#######################
# Improved Doubler TS #
#######################

improved_doubler_ts_real_arm_46 = \
    np.load('Improved Doubler TS_Real_data_arms_46_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_ts_real_arm_46.shape
sample = np.linspace(1, horizon-1, num=10, dtype=int)

avg_improved_doubler_ts_real_arm_46 = improved_doubler_ts_real_arm_46.sum(axis=1)/number_of_iteration
std_improved_doubler_ts_real_arm_46 = improved_doubler_ts_real_arm_46.std(axis=1)

plt.errorbar(sample, avg_improved_doubler_ts_real_arm_46[sample], std_improved_doubler_ts_real_arm_46[sample], linestyle='None')
ax_real_data_46.plot(range(horizon), avg_improved_doubler_ts_real_arm_46, 'g-',
                     label="Improved Doubler TS")

####################
# Improved Doubler #
####################

improved_doubler_real_arm_46 = \
    np.load('Improved Doubler_Real_data_arms_46_horizon_131072.npy')
horizon, number_of_iteration = improved_doubler_real_arm_46.shape
sample = np.linspace(1, horizon-1, num=10, dtype=int)

avg_improved_doubler_real_arm_46 = improved_doubler_real_arm_46.sum(axis=1)/number_of_iteration
std_improved_doubler_real_arm_46 = improved_doubler_real_arm_46.std(axis=1)
plt.errorbar(sample, avg_improved_doubler_real_arm_46[sample], std_improved_doubler_real_arm_46[sample], linestyle='None')
ax_real_data_46.plot(range(horizon), avg_improved_doubler_real_arm_46, 'r-',
                     label="Improved Doubler")

# #######
# # RCS #
# #######
#
# rcs_real_arm_46 = \
#     np.load('RCS_Real_data_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = rcs_real_arm_46.shape
# avg_rcs_real_arm_46 = rcs_real_arm_46.sum(axis=1)/number_of_iteration
# ax_real_data_46.plot(range(horizon), avg_rcs_real_arm_46, 'c-',
#                      label="RCS")
#
#
# ########
# # RUCB #
# ########
#
# rucb_real_arm_46 = \
#     np.load('RUCB_Real_data_arms_46_horizon_131072.npy')
# horizon, number_of_iteration = rucb_real_arm_46.shape
# avg_rucb_real_arm_46 = rucb_real_arm_46.sum(axis=1)/number_of_iteration
# ax_real_data_46.plot(range(horizon), avg_rucb_real_arm_46, 'm-',
#                      label="RUCB")
#
# ##########
# # SAVAGE #
# ##########
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

box_real_arm_46 = ax_real_data_46.get_position()

ax_real_data_46.set_position(
    [box_real_arm_46.x0,
     box_real_arm_46.y0 + box_real_arm_46.height * 0.4,
     box_real_arm_46.width,
     box_real_arm_46.height * 0.7])

ax_real_data_46.legend(loc='center left', bbox_to_anchor=(0.2, -0.4), shadow=True, prop=fontP)

fig_real_data_46.savefig("preference_real_data_46.png", bbox_inches='tight')

plt.show()
