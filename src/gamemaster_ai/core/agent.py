from abc import ABC, abstractmethod
from typing import Any

class Agent(ABC):
    """Base class for all agents"""

    @abstractmethod
    def choose_action(self, observation: Any) -> Any:
        """Choose an action based on the current observation"""
        pass