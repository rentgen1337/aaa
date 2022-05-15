import telebot;
from telebot import types
bot = telebot.Telebot('%5106859078%')
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    @bot.message_handler(content_types=['text'])
    if message.text == "Hi":
        bot.send_message(message.from_user.id, "Здравствуйте, что хотите заказать?")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши Hi")
            else:
                bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
                bot.polling(none_stop=True, interval=0)
                if message.text == "Меню":
                    bot.send_message(message.from_user.id, "Суши,Запеченые овощи,Бургер с рыбой,Картофель фри")
                    if message.text == "Сделать заказ":
                        bot.send_message(message.from_user.id, "Назовите свое имя,номер телефона и адрес доставки")
                        name = '';
                        phonenumber = '';
                        address = '0';
                        @bot.message_handler(content_types=['text'])
                        def start(message):
                            if message.text == '/reg':
                                bot.send_message(message.from_user.id, "Как тебя зовут?");
                                bot.register_next_step_handler(message, get_name);
                                     else:
                                     bot.send_message(message.from_user.id, 'Напиши /reg');
                                     def get_name(message):
                                         global name;
                                         name = message.text;
                                          bot.send_message(message.from_user.id, 'Какой у тебя номер телефона?');
                                          bot.register_next_step_handler(message, get_phonenumber);
                                          def get_phonenumber(message):
                                               global phonenumber;
                                               phonenumber = message.text;
                                               bot.send_message('Твой адресс?');
                                               bot.register_next_step_handler(message, get_address);
                                               def get_address(message):
                                                   global address;
                                                    while address == 0:
                                                        try:
                                                            age = int(message.text)
                                                            except Exception:
                                                                bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');

                                                   bot.send_message(message.from_user.id, 'Твой '+str(address)+'адрес , тебя зовут '+name+' 'Твой '+str(phonenumber)+' телефон' ?')
                                                   keyboard = types.InlineKeyboardMarkup();
                                                   key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes');
                                                   keyboard.add(key_yes);
                                                   key_no= types.InlineKeyboardButton(text='Нет', callback_data='no');
                                                   keyboard.add(key_no);
                                                   question = 'Твой '+str(address)+'адрес , тебя зовут '+name+' 'Твой '+str(phonenumber)+'телефон' ?';
                                                   bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
                                                   @bot.callback_query_handler(func=lambda call: True)
                                                   def callback_worker(call):
                                                        if call.data == "yes": 
                                                            bot.send_message(call.message.chat.id, 'Ваш заказ сформирован');
                                                            elif call.data == "no":






                