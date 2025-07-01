import gymnasium as gym
import numpy as np
import time
import imageio

class Tester():
    def __init__(self, episodes=100, max_steps=100):
        self.episodes = episodes
        self.max_steps = max_steps
        self.env = gym.make('CliffWalking-v0')
        # test_env = gym.make('Taxi-v3')

    def reset_f(self):
        state, _ = self.env.reset()
        return state

    def step_f(self, action):
        next_state, reward, terminated, truncated, _ = self.env.step(action)
        done = terminated or truncated
        return next_state, reward, done

    def get_obs_size(self):
        return self.env.observation_space.n
    
    def get_act_size(self):
        return self.env.action_space.n

    def evaluate(self, q_table):
        total_rewards = []
        for _ in range(self.episodes):
            state, _ = self.env.reset()
            total_reward = 0
            for _ in range(self.max_steps):
                action = np.argmax(q_table[state])
                state, reward, done, truncated, _ = self.env.step(action)
                total_reward += reward
                if done or truncated:
                    break
            total_rewards.append(total_reward)
        return total_rewards
    
    def evaluate_random_agent(self):
        total_rewards = []
        for _ in range(self.episodes):
            state, _ = self.env.reset()
            total_reward = 0
            for _ in range(self.max_steps):
                action = self.env.action_space.sample()
                state, reward, done, truncated, _ = self.env.step(action)
                total_reward += reward
                if done or truncated:
                    break
            total_rewards.append(total_reward)
        return total_rewards

    def render(self, q_table):
        test_env = gym.make('CliffWalking-v0', render_mode="rgb_array")
        # test_env = gym.make('Taxi-v3', render_mode="rgb_array")
        frames = []
        
        for episode in range(5):
            state, _ = test_env.reset()
            done = False

            print('Episode', episode)

            for _ in range(self.max_steps):
                frame = test_env.render()
                frames.append(frame)

                action = np.argmax(q_table[state])
                next_state, reward, done, truncated, _ = test_env.step(action)
                state = next_state

                if done or truncated:
                    test_env.render()
                    print('finished episode', episode, 'with reward', reward)
                    break

                time.sleep(0.05) # short time delay when rendering to allow linux ctrl+c to work
                # otherwise i couldnt close the app
        self.close()
        imageio.mimsave("cliffwalking.gif", frames, fps=5)
    
    def close(self):
        self.env.close()