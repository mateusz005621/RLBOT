# Tutaj znajdzie się definicja modelu sieci neuronowej dla agenta AI.
# Może to być np. sieć konwolucyjna (CNN) do analizy obrazu z gry
# lub sieć rekurencyjna (RNN) do przetwarzania sekwencji stanów.

import torch
import torch.nn as nn
import torch.nn.functional as F


class AgentModel(nn.Module):
    """Prosty model sieci neuronowej używany przez agenta."""

    def __init__(self, observation_space, action_space):
        super().__init__()
        self.observation_space = observation_space
        self.action_space = action_space
        # Minimalna sieć w pełni połączona
        self.fc1 = nn.Linear(observation_space, 128)
        self.fc2 = nn.Linear(128, action_space)
        print("Model agenta zainicjalizowany.")

    def forward(self, x):
        x = F.relu(self.fc1(x))
        return self.fc2(x)

    def predict(self, state):
        """Zwraca akcję na podstawie aktualnego stanu."""
        if not isinstance(state, torch.Tensor):
            state = torch.tensor(state, dtype=torch.float32)
        with torch.no_grad():
            logits = self.forward(state)
            action = torch.argmax(logits).item()
        return action
