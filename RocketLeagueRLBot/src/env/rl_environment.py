# Ten plik będzie zawierał definicję środowiska Rocket League,
# zgodnego z interfejsem typowym dla bibliotek reinforcement learning (np. OpenAI Gym).

import gym
import numpy as np


class RocketLeagueEnv(gym.Env):
    """Proste środowisko testowe."""

    def __init__(self, config):
        super().__init__()
        self.config = config

        # To jedynie uproszczona przestrzeń stanów i akcji.
        # Integracja z prawdziwą grą wymaga rlgym oraz zainstalowanej gry.
        self.observation_space = gym.spaces.Box(
            low=-1.0, high=1.0, shape=(10,), dtype=np.float32
        )
        self.action_space = gym.spaces.Discrete(5)

        print("Środowisko Rocket League zainicjalizowane.")

    def reset(self):
        """Zwraca losowy stan początkowy."""
        print("Resetowanie środowiska.")
        return self.observation_space.sample()

    def step(self, action):
        """Symuluje przejście do kolejnego stanu."""
        print(f"Wykonywanie akcji: {action}")
        next_state = self.observation_space.sample()
        reward = float(np.random.rand())
        done = False
        info = {}
        return next_state, reward, done, info

    def render(self, mode='human'):
        pass

    def close(self):
        print("Zamykanie środowiska Rocket League.")
