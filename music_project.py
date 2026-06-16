import numpy as np

songs = 100
 # number of songs
packaging = np.random.uniform (0, 100, songs)
 # packaging intensity for each song

listeners = 1000
# number of listeners
noise = np.random.normal(0,1,listeners)
# random preference shock (listeners choice may changed by personal tastes)

P =  packaging[0]

utility = np.log(P + 1) + noise
# utility funciton of a single song with 1000 listeners
choice = utility > 2
# the condition for listeners to choose a song
plays = np.sum(choice)
# play count per song

plays_list = []

i = 0

while i < songs:
    
    P = packaging[i]

    utility = np.log(P + 1) + noise

    choice = utility > 2

    plays = np.sum(choice)

    plays_list.append(plays)

    i += 1

import matplotlib.pyplot as plt

plt.scatter(packaging,plays_list)

plt.xlabel("Packaging Intensity")
plt.ylabel("Stimulated PLays")
plt.title("Relationship Between Packaging Intensity and Simulated Plays")

plt.show()



## ADDITIONAL ANALYZATION (Packaging vs. Utility) ##

# Figure 2

noise = np.random.normal(0,1,10000)

packaging = np.random.uniform (0, 100, 10000)

U = np.log(packaging + 1) + noise

plt.scatter(packaging, U)

plt.xlabel("Packaging Intensity")
plt.ylabel("Listener Utility")
plt.title("Relationship Between Packaging Intensity and Listener Utility")

plt.show()

# Figure 3

noise = np.random.normal(0,0.1,10000)

packaging = np.random.uniform (0, 100, 10000)

U = np.log(packaging + 1) + noise

plt.scatter(packaging, U)

plt.xlabel("Packaging Intensity")
plt.ylabel("Listener Utility")
plt.title("Relationship Between Packaging Intensity and Listener Utility")

plt.show()
