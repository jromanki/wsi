from qlearning_solver import QLearningSolver
from tester import Tester
import numpy as np

tester = Tester()

solver = QLearningSolver(tester.get_obs_size(), tester.get_act_size())
# Train the agent
q_table = solver.train(tester.step_f, tester.reset_f, num_episodes=1000, max_steps=100)
tester.render(q_table)