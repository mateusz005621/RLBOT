# Tutaj znajdzie się definicja modelu sieci neuronowej dla agenta AI.
# Może to być np. sieć konwolucyjna (CNN) do analizy obrazu z gry
# lub sieć rekurencyjna (RNN) do przetwarzania sekwencji stanów.

import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F


class AgentModel(nn.Module):
    """Prosty model sieci neuronowej sterujący agentem."""

    def __init__(self, observation_space, action_space):
        super().__init__()
        self.observation_space = observation_space
        self.action_space = action_space

        obs_size = observation_space.shape[0]
        action_size = action_space.n

        self.fc1 = nn.Linear(obs_size, 64)
        self.fc2 = nn.Linear(64, 64)
        self.fc3 = nn.Linear(64, action_size)

        print("Model agenta zainicjalizowany.")

    def forward(self, x: np.ndarray | torch.Tensor) -> torch.Tensor:
        if isinstance(x, np.ndarray):
            x = torch.from_numpy(x).float()
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        return self.fc3(x)

    def predict(self, state) -> int:
        """Zwraca najlepszą akcję dla danego stanu."""
        with torch.no_grad():
            q_values = self.forward(state)
        return int(torch.argmax(q_values).item())
