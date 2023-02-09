state -> action -> reward -> next state


if(action == forward and current_state.distance<theshold) negative reward
else positive reward


state = self._preprocess(state)
state = state[np.newaxis, ...].repeat(4, axis=0)



for i in range(400):
    env.reset()
    episode_reward = 0
    step = 0
    while True:
        state = get_state()
        action = reply[step-1]["action"]
        reward = get_progerss()-reward[step-1]["progress"]
        episode_reward += reward
        reply[step][action] = choose_action(state)
        reply[step][progerss] = get_progress()
        
        if memory_counter > memory_capacity:
            dqn.learn()
        if done: break

