import numpy as np

brands = 100
 # number of music brands
strength_of_info = np.random.uniform (0, 100, brands)
 # strength of information signal for each brand

listeners = 1000
# number of listeners
noise = np.random.normal(0,1,listeners)
# random preference shock (listeners choice may changed by personal tastes)

S =  strength_of_info[0]

utility = np.log(S + 1) + noise
# utility funciton of a single listener
choice = utility > 2
# the condition for branding attraction
plays = np.sum(choice)
# play count per brand

plays_list = []

i = 0

while i < brands:
    
    S = strength_of_info[i]

    utility = np.log(S + 1) + noise

    choice = utility > 2

    plays = np.sum(choice)

    plays_list.append(plays)

    i += 1

import matplotlib.pyplot as plt

plt.scatter(strength_of_info,plays_list)

plt.xlabel("Information signal Intensity")
plt.ylabel("Stimulated Choice")
plt.title("Relationship Between Information Signaling Intensity and Simulated Choice")

plt.show()



## ADDITIONAL ANALYZATION (Packaging vs. Utility) ##

#Figure 2

noise = np.random.normal(0,1,10000)

strength_of_info = np.random.uniform (0, 100, 10000)

U = np.log(strength_of_info + 1) + noise

plt.scatter(strength_of_info, U)

plt.xlabel("Information Signal Intensity")
plt.ylabel("Listener Utility")
plt.title("Relationship Between Information Signal Intensity and Listener Utility")

plt.show()

# Figure 3

noise = np.random.normal(0,0.1,10000)

strength_of_info = np.random.uniform (0, 100, 10000)

U = np.log(strength_of_info + 1) + noise

plt.scatter(strength_of_info, U)

plt.xlabel("Information Signal Intensity")
plt.ylabel("Listener Utility")
plt.title("Relationship Between Information Signal Intensity and Listener Utility")

plt.show()