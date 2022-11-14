import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id


class Bot:
    def __init__(self, token):
        self.token = token
        self.session = vk_api.VkApi(token=self.token)
        self.accept_long = VkLongPoll(self.session)

    def send_message(self, user_id, text):
        self.session.method("messages.send", {'user_id': user_id,
                                              'message': text,
                                              'random_id': get_random_id()
                                              }
                            )

    def start(self):
        for event in self.accept_long.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                self.send_message(event.user_id, event.message)
