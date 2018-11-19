import logging
from gym.envs.registration import register

logger = logging.getLogger(__name__)

register(
    id='speak-v0',
    entry_point='gym_speak.envs:speakEnv',
    timestep_limit=1000,
    reward_threshold=1.0,
    nondeterministic = True,
)

register(
    id='speakWordClose-v0',
    entry_point='gym_speak.envs:speakWordClose',
    timestep_limit=1000,
    reward_threshold=10.0,
    nondeterministic = True,
)

register(
    id='speakSentClose-v0',
    entry_point='gym.envs:speakSentClose',
    timestep_limit=1000,
    reward_threshold=8.0,
    nondeterministic = True,
)
