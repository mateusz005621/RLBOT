"""Simple injector that connects the RLBot framework with Rocket League.

This module uses RLBot's `SetupManager` to launch the game and inject
an agent for offline training. It expects an `rlbot.cfg` configuration
file describing the match and bot to run.
"""

from pathlib import Path

from rlbot.setup_manager import SetupManager


def launch_offline_match(config_path: str) -> None:
    """Launch Rocket League for offline training using RLBot.

    Parameters
    ----------
    config_path: str
        Path to the ``rlbot.cfg`` configuration file.
    """
    manager = SetupManager()
    manager.load_config(Path(config_path))
    manager.connect_to_game()
    manager.launch_ball_prediction()
    manager.launch_bot_processes()
    manager.start_match()
    manager.infinite_loop()


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python -m src.env.rlbot_injector <path_to_rlbot.cfg>")
        sys.exit(1)
    launch_offline_match(sys.argv[1])
