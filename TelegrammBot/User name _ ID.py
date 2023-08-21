import telebot #библиотека с которой будем работать
import configure #импортируем файл с данными о боте
from telebot import types  #для работы с кнопками

client = telebot.TeleBot(configure.config['token']) #создаем главнуб переменную (client), дальше обязетнльно пишем telebot.Telebot, в скобках обращаемся к файлу configure, потом к переменной config и к тоекну



#ккомонады создаем выше обработчика сообещний, выше content_types

@client.message_handler(commands = ['get_info', 'info']) #то же самое что и в 10 строке, только с разным напсианием
def get_user_ifo(message): #есть два вида кнопок, inline и reply, одни видын на в месте где мы вводим сообщения, а дургие под сообщение, соотвтетствено
    #будем создавать inline кнопки
    markup_inline = types.InlineKeyboardMarkup() #мы сейчас создали inline клавиатуру, которая крепится под сообщения, дальше мы должын добваить кнопки для клавиатрау. В параметрах "()" ничего не задаем, markup_inline - обычная переменная
    #создаем кнопки
    item_yes = types.InlineKeyboardButton(text = 'ДА', callback_data = 'yes') #в text помещеам наш текст. С помощью callback_data мы сможем ставить условие: если пользователь нажал на кнопку "ДА", то срабатвает действие
    item_no = types.InlineKeyboardButton(text = 'НЕТ', callback_data = 'no') #то же самое что и в предыдущей строке только наооборот

    #занесем наши кнопки в клавиатуру
    markup_inline.add(item_yes, item_no) #доабваляем в нашу нашу переменную, которая отвечает за клаивиатуру (markup_inline) две наши кнопки. add(имя переменноцнажей кнопки, имя переменноцнажей кнопки)

    #теперь выведем наше сообщение к которому будут крепится кнопки
    client.send_message(message.chat.id, 'Не хотите узнать небольшую информацию о вас?',
        reply_markup = markup_inline #в reply_markup помещаем название нашей главной переменной markup_inline, чтобы прикрепить наши нкопки к сообещнию в пердыдущй строчки. reply_markup - всегда пишем когад хотим добавить кнопки к сообщению
    )



#создадим обработчик обратной связи
@client.callback_query_handler(func = lambda call: True) #(func = lambda call: True) - это фнукция которая обрабадывает какое-то сообытие при нажатие на кнопку, но это не точно
def answer(call): #создали фуекцию answer с параметром call
    #в item_yes и item_no мы поместили параметр callback_data, у этих праметрах значения yes и no соответсенно, если юзер нажал на кнопку ДА то его перекидывает в эту функцию и начинается обработка функции. Eсли call.data уловил параметр yes то выполняется дейтсвие, для параметар no все то же самое
    if call.data == 'yes':
        #создадим кнопки, но уже reply
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True) #все то же самое что мы и делали для inline клавиватуры (строка 10), resize_keyboard = True - нужно для того чтобы клавиатуру сделать меньше и чтобы выглядела красивше, но это длеать НЕ обязательно
        #создадим кнопки
        item_id = types.KeyboardButton('МОЙ ID') #создали кнопку но пишем прсото ! types.KeyboardButton !
        item_username = types.KeyboardButton('МОЙ НИК')

        #присоединим кнопки к нашей клавиатуре
        markup_reply.add(item_id, item_username) #занесли кнопки в клавиатуру, как мы уже делали
        client.send_message(call.message.chat.id, 'Нажмите на одну кнопок', #мы здесь в функции answer (25 строка) не предавали параметр message, поэтому сначала обращаемся к параметру call, который объявляли в функции, а потом message
        #подвязываем наши кнопки
            reply_markup = markup_reply #то же самое что и в 20 строке
        )
    elif call.data == 'no':
        client.send_message(call.message.chat.id, 'Эх, жаль, если передумаешь пиши /info снова')



@client.message_handler(content_types = ['text']) #обращаемся к client, нашему боту. messege_handler - обработчик сообещний. content_types - тип контента, так же есть  такой тип контента: 'audio', 'document' content_types = ['text', 'audio', 'document']
def get_text(message): #создаем функцию, передаем параметр message с которым потом рабоатем
    if message.text == 'МОЙ ID':
        client.send_message(message.chat.id, f'Your ID: {message.from_user.id}') #бот отпарляет сообещние, f - форматирование, {message.from_user.id} - метод который узнает ID пользователя

    elif message.text == 'МОЙ НИК':
        client.send_message(message.chat.id, f'Your NIK: {message.from_user.first_name} {message.from_user.first_name}') #то же самое что в 47 стрчоке только метода отправки имени и фамилии пользователя



client.polling(none_stop = True, interval = 0) #polling - цикл нашего общения, бот все время будет спрашивать у сервера написали ли ли ему сообещение, и когда мы ему напишем он нам ответит. none_stop = True - значи что наш бот не будет устанавливаться. interval - интервал




#@client.message_handler(content_types = ['text']) #обращаемся к client, нашему боту. messege_handler - обработчик сообещний. content_types - тип контента, так же есть  такой тип контента: 'audio', 'document' content_types = ['text', 'audio', 'document']
#def get_text(message): #создаем функцию, передаем параметр message с которым потом рабоатем
#if message.text.lower() == 'привет': #если message.text == 'привет', то: (lower() - для того чтобы ПРИВЕТ = привет)
       # client.send_message(message.chat.id, 'Привет неизвестный юзер! Можешь почитать описание обо мне и узнать меня получше :)' ) #мы от именни нашего бота отправляем сообщения. имя нашего бота,у нас это client.-send_message(message.chat.id-, "сообщение". То что между '- -' пишется обязательно. message.chat.id - уникальынй код переписки, его так всегда и пишем
    #elif message.text.lower() == 'как дела'
       # client.send_message(message.chat.id, 'Все хорошшо, у тебя как ?')