"""
An example OpenAI offers to test environment.
"""

import gym
env = gym.make('CartPole-v1')
env.reset()
for _ in range(100):
    env.render()
    env.step(env.action_space.sample()) # take a random action
env.close()