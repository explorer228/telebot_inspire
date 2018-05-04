import telebot
import constants
import os
import random

bot = telebot.TeleBot(constants.token)

print(bot.get_me())

def log(message, answer):
    print('\n -----')
    from datetime import datetime
    print(datetime.now())
    print('Message from {0} {1}. (id = {2}) \n Text - {3}'.format(message.from_user.first_name,
                                                                   message.from_user.last_name,
                                                                   str(message.from_user.id),
                                                                   message.text))
    print(answer)



#COMMANDS

#start
@bot.message_handler(commands=['start'])

def start(message):
    sent = bot.send_message(message.chat.id, 'what is your name?')
    bot.register_next_step_handler(sent, hello_keyboard)

#keyboard
def hello_keyboard(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/stop')
    user_markup.row('photo', 'audio', 'video')
    user_markup.row('impulse', 'somethin new', 'voice', 'location')
    answer = 'hello, {name}. nice to meet you :) how can i help you?'
    bot.send_message(message.from_user.id,  answer.format(name=message.text), reply_markup=user_markup)

#stop
@bot.message_handler(commands=['stop'])
def handle_start(message):
    remove_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id, '..', reply_markup=remove_markup)

#help
@bot.message_handler(commands=['help'])
def handle_text(message):
    answer = 'this bot sends you interesting finds of good quality ' \
             '- photos, audios, videos, locations and other treats - ' \
             'that will make you feel better ;)'
    bot.send_message(message.chat.id, answer)


#MAIN
@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'photo':
        directory = '/Users/polinakato/PycharmProjects/telebot/photos'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()
    elif message.text == 'audio':
        directory = '/Users/polinakato/PycharmProjects/telebot/audios'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        audio = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()

    elif message.text == 'video':
        directory = '/Users/polinakato/PycharmProjects/telebot/videos'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        video = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_video')
        bot.send_audio(message.from_user.id, video)
        video.close()
    elif message.text == 'voice':
        directory = '/Users/polinakato/PycharmProjects/telebot/voices'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        voice = open(directory + '/' + random_file, 'rb')
        bot.send_chat_action(message.from_user.id, 'upload_voice')
        bot.send_audio(message.from_user.id, voice)
        voice.close()
    elif message.text == 'location':
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, 51.5022, -0.0851)
    elif message.text == 'words':
        bot.send_message(message.from_user.id, constants.random_message())



bot.polling(none_stop=True, interval=0)

