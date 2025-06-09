import numpy as np
import random
import time
import gymnasium as gym

env = gym.make('Taxi-v3')

alpha = 0.9 # learning rate     - how important new info is
gamma = 0.95 # discount factor  - how important future rewards are
epsilon = 1 # exploration rate  - randomness 1 - completly random
epsilon_decay = 0.9995
min_epsilon = 0.01
num_episodes = 10000
max_steps = 100

# Taxi game - 25 pos x 5 x 4
q_table = np.zeros((env.observation_space.n, env.action_space.n))
# print(np.shape(q_table))

def choose_action(state):
    if random.uniform(0, 1) < epsilon:
        return env.action_space.sample()
    else:
        return np.argmax(q_table[state, :])
    

for episode in range(num_episodes):
    state, _ = env.reset()

    done = False

    for step in range(max_steps):
        action = choose_action(state)

        next_state, reward, done, truncated, _ = env.step(action)

        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])

        q_table[state, action] = (1 - alpha) * old_value + alpha * (reward + gamma *next_max)

        state = next_state

        if done or truncated:
            break

    epsilon = max(min_epsilon, epsilon * epsilon_decay)
env.close()


test_env = gym.make('Taxi-v3', render_mode='human')

for episode in range(5):
    state, _ = test_env.reset()
    done = False

    print('Episode', episode)

    for step in range(max_steps):
        test_env.render()
        action = np.argmax(q_table[state])
        next_state, reward, done, truncated, _ = test_env.step(action)
        state = next_state

        if done or truncated:
            test_env.render()
            print('finished episode', episode, 'with reward', reward)
            break

        time.sleep(0.05) # short time delay when rendering to allow linux ctrl+c to work
        # otherwise i couldnt close the app

test_env.close()
