# Ten plik będzie zawierał logikę odpowiedzialną za trenowanie modelu agenta.
# Będzie tu implementacja algorytmu uczenia przez wzmacnianie, np. Q-learning, DQN, PPO itp.

import numpy as np
import torch
import torch.nn as nn


class AgentTrainer:
    """Bardzo uproszczona pętla treningowa."""

    def __init__(self, agent_model, environment, config):
        self.agent_model = agent_model
        self.environment = environment
        self.config = config

        lr = config.get("agent_params", {}).get("learning_rate", 0.001)
        self.gamma = config.get("agent_params", {}).get("discount_factor", 0.99)

        self.optimizer = torch.optim.Adam(self.agent_model.parameters(), lr=lr)
        self.criterion = nn.MSELoss()

        print("Trener agenta zainicjalizowany.")

    def train(self, num_episodes: int):
        print(f"Rozpoczynam trening na {num_episodes} epizodów.")

        for episode in range(num_episodes):
            state = self.environment.reset()
            done = False
            total_reward = 0.0

            while not done:
                action = self.agent_model.predict(state)
                next_state, reward, done, _ = self.environment.step(action)

                target = reward + self.gamma * torch.max(
                    self.agent_model(next_state)
                ).item()

                predicted = self.agent_model(state)[action]
                loss = self.criterion(predicted, torch.tensor(target))

                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

                state = next_state
                total_reward += reward

            print(f"Epizod {episode + 1}/{num_episodes} - nagroda: {total_reward:.2f}")

        print("Trening zakończony.")
        self.environment.close()
