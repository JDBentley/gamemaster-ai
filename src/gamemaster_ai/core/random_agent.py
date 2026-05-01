import random
from typing import Any

from gamemaster_ai.core import Agent

class RandomAgent(Agent):
    """Agent that chooses randomly from a list of actions."""

    def __init__(self, actions: list[str]):
        if not actions:
            raise ValueError("RandomAgent requires at least one action.")
        
        self.actions = actions
    
    def choose_action(self, observation: Any) -> str:
        return random.choice(self.actions)