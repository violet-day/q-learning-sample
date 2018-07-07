# -*- coding: utf-8 -*-

import numpy as np

reward_matrix = np.array([
    [-1, -1, -1, -1, 0, -1],
    [-1, -1, -1, 0, -1, 100],
    [-1, -1, -1, 0, -1, -1],
    [-1, 0, 0, -1, 0, -1],
    [0, -1, -1, 0, -1, 100],
    [-1, 0, -1, -1, 0, 100]
])


def random_initial_state():
    return np.random.randint(low=0, high=reward_matrix.shape[0])


def choice_action(q_target_matrix, current_state, epsilon=0.5):
    next_available_state = np.argwhere(reward_matrix[current_state] != -1).flatten()
    if np.random.sample() > epsilon:
        action = np.random.choice(next_available_state)
    else:
        q_max_idx = q_target_matrix[current_state][next_available_state].argmax()
        action = next_available_state[q_max_idx]

    return action


def step(action):
    if action == 5:
        return action, 100, True
    else:
        return action, 0, False


def run_loop(gamma=0.8, epsilon=0.5):
    q_matrix = np.zeros_like(reward_matrix, dtype=reward_matrix.dtype)

    for i_episode in range(1000):
        current_state = random_initial_state()

        while True:
            action = choice_action(q_matrix, current_state, epsilon)

            next_state, reward, done = step(action)

            q_matrix[current_state, action] = \
                reward + gamma * np.max(q_matrix[next_state])

            current_state = next_state
            if done:
                print('Episode %d finished' % i_episode)
                print(q_matrix)
                break


if __name__ == '__main__':
    run_loop()
