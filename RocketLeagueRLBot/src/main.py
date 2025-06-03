from utils.helpers import load_config
from env.rl_environment import RocketLeagueEnv
from agent.model import AgentModel
from agent.trainer import AgentTrainer


def main(num_episodes: int = 5) -> None:
    """Uruchamia trening przykładowego agenta."""

    print("Witaj w RocketLeagueRLBot!")

    config = load_config()
    env = RocketLeagueEnv(config)
    model = AgentModel(env.observation_space, env.action_space)
    trainer = AgentTrainer(model, env, config)

    trainer.train(num_episodes)

if __name__ == "__main__":
    main()
