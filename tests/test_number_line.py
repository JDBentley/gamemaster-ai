import pytest

from gamemaster_ai.games.toy.number_line_env import NumberLineEnv

def test_number_line_env_resets_to_start():
    env = NumberLineEnv()

    observation = env.reset()

    assert observation["position"] == 0
    assert observation["target_position"] == 5
    assert observation["steps_taken"] == 0

def test_number_line_env_moves_right():
    env = NumberLineEnv()
    env.reset()

    observation, reward, done, info = env.step("move_right")

    assert observation["position"] == 1
    assert reward == -1.0
    assert done is False
    assert info["reached_goal"] is False

def test_number_line_env_reaches_goal():
    env = NumberLineEnv(target_position=1)
    env.reset()

    observation, reward, done, info = env.step("move_right")

    assert observation["position"] == 1
    assert reward == 10
    assert done is True
    assert info["reached_goal"] is True

def test_number_line_env_rejects_invalid_action():
    env = NumberLineEnv()
    env.reset()

    with pytest.raises(ValueError):
        env.step("jump")

def test_number_line_env_moves_left():
    env = NumberLineEnv()
    env.reset()

    observation, reward, done, info = env.step("move_left")

    assert observation["position"] == -1
    assert reward == -1.0
    assert done is False
    assert info["reached_goal"] is False