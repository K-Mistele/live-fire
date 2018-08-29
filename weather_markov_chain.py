import numpy as np
import random as rm

states = ["wind", "rain", "snow"]

transition_name = [["WW", "WR", "WS"],  # transitions from wind state
                   ["RW", "RR", "RS"],  # transitions from rain state
                   ["SW", "SR", "SS"]] # transitions from snow state

transition_matrix = [[0.2, 0.7, 0.1],  # corresponding probabilities of transitions from wind to other states
                     [0.3, 0.2, 0.5],  # corresponding probabilities of transitions from rain to other states
                     [0.1, 0.3, 0.6]] # corresponding probabliities of transitions from snow to other states

# ensure all probabilities are forced to be a total of 1:
if sum(transition_matrix[0]) + sum(transition_matrix[1]) + sum(transition_matrix[2]) != 3:
    print("Your transition matrix is not valid! Please ensure each list of probabilities adds up to 1!")
    quit()

def weather_forecast(n):

    #choose the starting state:
    while True:
        start_state_input = input(f"Please enter a starting state from the following list: {states}\n>>> ")
        if start_state_input in states:
            start_state = start_state_input
            break

    print(f"Start state: {start_state}")
    activity_list =[start_state]

    number_of_days = n
    prob = 1
    for i in range(0, number_of_days):
        activity_today = activity_list[-1]
        if activity_today == "wind":

            # param no.1 is list of options, param no. 2 is sampling with replacement, param no. 3 is list of probabilities
            change = np.random.choice(transition_name[0], replace=True, p=transition_matrix[0])
            if change == "WW":
                prob = prob * 0.2
                activity_list.append("wind")
                pass
            elif change == "WR":
                prob = prob * 0.7
                activity_list.append("rain")

            else:
                prob = prob * 0.1
                activity_list.append("snow")

        elif activity_today == "rain":
            change = np.random.choice(transition_name[1], replace=True, p=transition_matrix[1])
            if change == "RW":
                prob = prob * 0.3
                activity_list.append("wind")
                pass
            elif change == "RR":
                prob = prob * 0.2
                activity_list.append("rain")
            else:
                prob = prob * 0.5
                activity_list.append("snow")

        elif activity_today == "snow":
            change = change = np.random.choice(transition_name[2], replace=True, p=transition_matrix[2])
            if change == "SW":
                prob = prob * 0.1
                activity_list.append("wind")
            elif change == "SR":
                prob = prob * 0.3
                activity_list.append("rain")
            else:
                prob = prob * 0.6
                activity_list.append("snow")
    print(f"Possible states: {str(states)}")
    print(f"End State after {number_of_days} days: {activity_today}")
    print(f"Probability of the possible sequence of states: {str(prob)}")
    print(f"All transitions: {activity_list}")

weather_forecast(40)
