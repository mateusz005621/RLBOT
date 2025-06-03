from src.utils.helpers import load_config
from src.agent.model import AgentModel
from src.agent.trainer import AgentTrainer
from src.env.rl_environment import RocketLeagueEnv


def main():
    print("Witaj w RocketLeagueRLBot!")
    config = load_config()
    env = RocketLeagueEnv(config)
    obs_space = env.observation_space
    act_space = env.action_space
    agent = AgentModel(obs_space, act_space)
    trainer = AgentTrainer(agent, env, config)
    num_episodes = config.get("training_params", {}).get("num_episodes", 10)
    trainer.train(num_episodes)

if __name__ == "__main__":
    main()

