from abc import ABC

import numpy as np
from gymnasium.wrappers import StepAPICompatibility

try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol

import base64
import glob
import io
from typing import Any, Tuple

import gym
from gym.wrappers import Monitor
from IPython import display as ipythondisplay
from IPython.display import HTML
from pyvirtualdisplay import Display

_display = None


class ModelProtocol(Protocol):
    def predict(self, observation: np.ndarray, **kwargs) -> Tuple[np.ndarray, Any]:
        pass


def show_video():
    mp4list = glob.glob("video/*.mp4")
    if len(mp4list) != 1:
        raise Exception("Something went wrong")
    video = io.open(mp4list[0], "r+b").read()
    encoded = base64.b64encode(video)
    ipythondisplay.display(
        HTML(
            data="""<video alt="test" autoplay 
                loop controls style="height: 400px;">
                <source src="data:video/mp4;base64,{0}" type="video/mp4" />
              </video>""".format(
                encoded.decode("ascii")
            )
        )
    )


class SingleVideoMonitor(Monitor):
    # Overriding gym's monitor to not reset video recorder each time
    def _after_reset(self, observation):
        if not self.enabled:
            return

        # Reset the stat count
        self.stats_recorder.after_reset(observation)

        if not self.video_recorder:
            self.reset_video_recorder()

        # Bump *after* all reset activity has finished
        self.episode_id += 1

        self._flush()


def demo_model(
    env: gym.Env, model: ModelProtocol, num_steps=1000, in_notebook=True, **kwargs
):
    if in_notebook:
        global _display
        if _display is None:
            _display = Display(visible=0, size=(1400, 900))
            _display.start()
        env = SingleVideoMonitor(env, "./video", force=True)
    obs = env.reset()
    for _ in range(num_steps):
        action, _states = model.predict(obs, **kwargs)
        obs, reward, done, info = env.step(action)
        env.render()
        if done:
            obs = env.reset()
    env.close()
    if in_notebook:
        show_video()


try:
    from typing import Protocol
except ImportError:
    from typing_extensions import Protocol

import base64
import glob
import io
from typing import Any, Tuple

from gym.wrappers import Monitor
from IPython import display as ipythondisplay
from IPython.display import HTML
from pyvirtualdisplay import Display


def show_video():
    mp4list = glob.glob("video/*.mp4")
    if len(mp4list) != 1:
        raise Exception("Something went wrong")
    video = io.open(mp4list[0], "r+b").read()
    encoded = base64.b64encode(video)
    ipythondisplay.display(
        HTML(
            data="""<video alt="test" autoplay 
                loop controls style="height: 400px;">
                <source src="data:video/mp4;base64,{0}" type="video/mp4" />
              </video>""".format(
                encoded.decode("ascii")
            )
        )
    )


class SingleVideoMonitor(Monitor):
    # Overriding gym's monitor to not reset video recorder each time
    def _after_reset(self, observation):
        if not self.enabled:
            return

        # Reset the stat count
        self.stats_recorder.after_reset(observation)

        if not self.video_recorder:
            self.reset_video_recorder()

        # Bump *after* all reset activity has finished
        self.episode_id += 1

        self._flush()


def demo_model(
    env: gym.Env, model: ModelProtocol, num_steps=100, in_notebook=True, **kwargs
):
    if in_notebook:
        global _display
        if _display is None:
            _display = Display(visible=0, size=(1400, 900))
            _display.start()
        env = SingleVideoMonitor(env, "./video", force=True)
    obs = env.reset()
    for _ in range(num_steps):
        action, _states = model.predict(obs, **kwargs)
        obs, reward, done, info = env.step(action)
        env.render()
        if done:
            obs = env.reset()
    env.close()
    if in_notebook:
        show_video()

    a = StepAPICompatibility()
