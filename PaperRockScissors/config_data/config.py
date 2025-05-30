from dataclasses import dataclass
from environs import Env
from pathlib import Path


@dataclass
class TgBot:
    token: str  # bot token


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str | None = None) -> Config:
    if path is None:
        path = Path(__file__).resolve().parent / '.env'

    env: Env = Env()  # instance of Env class
    env.read_env(path)  # add env variables

    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN")
        )
    )
