#учимся делать переход из одной функции в другую, это нужно для правильной структуры бота
import telebot

client = telebot.TeleBot("5293054411:AAEklRb8T28_kmdPmbNbHXyp1UMLDilSzwc")

@client.message_handler(commands=["application"])
def application(message):
    rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True,resize_keyboard=True) #one_time_keyboard=True - делает клавиатуру как бы одноразовой, скрывая ееж
    rmk.add(types.KeyboardButton("Да"), types.KeyboardButton("Нет"))

    msg = client.send_message(message.chat.id,"Желаете подать заявку на модератора?",reply_markup = rmk)

    client.register_next_step_handler(msg, user_answer) #Прописваем переход из одной функции в другую. Пишем имя нашей главной переменной (client), дальше register_next_step_handler(msg,название функци в которую хотим перейти)


def user_answer(message):
    if message.text == "Да":
        msg = client.send_message(message.chat.id, "Впишите ваши данные:")
        client.register_next_step_handler(msg,user_reg)
    elif message.text == "Нет":
        client.send_message(message.chat.id, "Хорошо, смешнявка!")
    else:
        client.send_message(message.chat, "Ты что, смешнявка?!")

def user_reg(message):
    client.send_message(message.chat.id, f"Ваши данные: {message.text}")


client.polling()