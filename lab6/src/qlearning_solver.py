import numpy as np
import random

class QLearningSolver:
    def __init__(self, observation_space_size, action_space_size,
                 alpha=0.1, gamma=0.99, epsilon=1.0, 
                 epsilon_decay=0.995, min_epsilon=0.01):
        
        # hyperparameter initialisation
        self.alpha = alpha      # learning rate - how important new info is
        self.gamma = gamma      # discount factor - how important future rewards are
        self.epsilon = epsilon  # exploration rate  - randomness 1 - completly random
        self.epsilon_decay = epsilon_decay
        self.min_epsilon = min_epsilon

        self.observation_space_size = observation_space_size
        self.action_space_size = action_space_size
    
    def choose_action(self, q_table, state):
        if random.uniform(0, 1) < self.epsilon:
            return random.randint(0, self.action_space_size-1)
        else:
            return np.argmax(q_table[state, :])
        

    def train(self, step_f, reset_f, num_episodes=1000, max_steps=100):
        q_table = np.zeros((self.observation_space_size, self.action_space_size))
        eps = self.epsilon

        for episode in range(num_episodes):
            state = reset_f()

            done = False

            for step in range(max_steps):
                action = self.choose_action(q_table, state)

                next_state, reward, done = step_f(action)

                old_value = q_table[state, action]
                next_max = np.max(q_table[next_state])

                q_table[state, action] = (1 - self.alpha) * old_value + self.alpha * (reward + self.gamma *next_max)

                state = next_state

                if done:
                    break

            eps = max(self.min_epsilon, eps * self.epsilon_decay)
        
        return q_table


    