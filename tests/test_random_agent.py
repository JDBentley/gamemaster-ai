from gamemaster_ai.core import RandomAgent

def test_random_agent_returns_valid_action():
    actions = ["move_left", "move_right"]
    agent = RandomAgent(actions)

    action = agent.choose_action(observation={})

    assert action in actions

