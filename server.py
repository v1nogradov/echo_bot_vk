import configparser
from vkbot import Bot


class Setting:
    @staticmethod
    def start():
        config = configparser.ConfigParser()

        config.read("setting.ini")

        bot = Bot(config["VK"]["TOKEN"])
        bot.start()


Setting.start()
