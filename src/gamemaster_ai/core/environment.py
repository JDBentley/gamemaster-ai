from abc import ABC, abstractmethod
from typing import Any

class Environment(ABC):
    """Base class for all game environments."""

    @abstractmethod
    def reset(self) -> Any:
        """Reset the environment to its starting state"""
        pass

    @abstractmethod
    def step(self, action: Any) -> tuple[Any, float, bool, dict]:
        """Apply an action to the environment"""
        pass
