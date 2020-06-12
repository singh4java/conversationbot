from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import os
from termcolor import colored
import pyfiglet

colors = {'G': 'grey', 'R': 'red', 'GR': 'green', 'Y': 'yellow', 'B': 'blue', 'M': 'magenta', 'C': 'cyan', 'W': 'white'}


result = pyfiglet.figlet_format("Con-Bot-AI", font = "digital")
print(colored(result,color='green'))
print('------Color List-------')
print(colors)
x = input('Select bot response color from  color  list ')
color = colors.get(x)


def botreply(reply, color):
    text = f'ChatBot :{reply}'
    coloradan_art = colored(text, color=color)
    print(coloradan_art)


bot = ChatBot('God')
trainer = ListTrainer(bot)

pathurl = "/Users/manvendrasingh/PycharmProjects/conversationbotai/data/english/"

for files in os.listdir(pathurl):
    data = open(pathurl + files, 'r').readlines()

    trainer.train(data)

while True:
    msg = input('You : ')
    if msg.strip() != 'Bye':
        reply = bot.get_response(msg)
        botreply(reply, color)

    if msg.strip() == 'Bye':
        botreply('Bye', color)
        break