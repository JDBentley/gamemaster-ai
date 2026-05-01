from typing import Any

from gamemaster_ai.core import Environment

class NumberLineEnv(Environment):
    """A simple tyo environment where the agent moves along a number line."""

    def __init__(self, target_position: int = 5, max_steps: int = 20):
        self.target_position = target_position
        self.max_steps = max_steps
        self.position = 0
        self.steps_taken = 0

    def reset(self) -> dict[str, Any]:
        self.position = 0
        self.steps_taken = 0
    
        return self._get_observation()
    
    def step(self, action: str) -> tuple[dict[str, Any], float, bool, dict]:
        if action not in ["move_left", "move_right"]:
            raise ValueError(f"Invalid action: {action}")
        
        if action == "move_left":
            self.position -= 1
        
        if action == "move_right":
            self.position += 1

        self.steps_taken += 1

        reached_goal = self.position >= self.target_position
        out_of_steps = self.steps_taken >= self.max_steps

        done = reached_goal or out_of_steps

        reward = 10 if reached_goal else -1.0

        observation = self._get_observation()

        info = {
            "reached_goal": reached_goal,
            "steps_taken": self.steps_taken,
        }

        return observation, reward, done, info
    
    def _get_observation(self) -> dict[str, Any]:
        return {
            "position": self.position,
            "target_position": self.target_position,
            "steps_taken": self.steps_taken,
        }