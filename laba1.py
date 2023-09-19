import telebot
from telebot import types
import random
import os
import re

user_token = "5832700201:AAGd1AXiVDXTi9hdUzdAhsUNTzPDHSekDnQ"
user_images_folder = r"C:\Users\nsrod\Pictures\images"
user_images_folder = re.sub(r'\\', '/', user_images_folder)
user_audio_folder = r"C:\Users\nsrod\Music\audio"
user_audio_folder = re.sub(r'\\', '/', user_audio_folder)


class Bot:
    def __init__(self, token, images_folder, audio_folder):
        self.bot = telebot.TeleBot(token)
        self.images_folder = images_folder
        self.audio_folder = audio_folder

    def start(self):
        @self.bot.message_handler(commands=['start'])
        def handle_start(message):
            keyboard = types.ReplyKeyboardMarkup(True)
            keyboard.add('Аудио')
            keyboard.add('GitHub Link')
            self.bot.send_message(
                text="Чем могу быть полезен?",
                chat_id=message.chat.id,
                reply_markup=keyboard
            )

        @self.bot.message_handler(func=lambda message: "изображение" in message.text.lower())
        def send_random_image(message):
            image_files = [f for f in os.listdir(self.images_folder)]

            if image_files:
                random_image = random.choice(image_files)
                image_path = os.path.join(self.images_folder, random_image)

                with open(image_path, 'rb') as image_file:
                    self.bot.send_photo(message.chat.id, image_file)

        @self.bot.message_handler(func=lambda message: "аудио" in message.text.lower())
        def send_random_sound(message):
            sound_files = [f for f in os.listdir(self.audio_folder)]
            if sound_files:
                random_sound = random.choice(sound_files)
                sound_path = os.path.join(self.audio_folder, random_sound)

                with open(sound_path, 'rb') as sound_file:
                    self.bot.send_voice(message.chat.id, sound_file)

        @self.bot.message_handler(func=lambda message: "link" in message.text.lower())
        def send_github_link(message):
            self.bot.send_message(text='github.com/delf1nder/OOP_laba_1', chat_id=message.chat.id)
        self.bot.polling(none_stop=True)


if __name__ == "__main__":
    my_bot = Bot(user_token, user_images_folder, user_audio_folder)
    my_bot.start()