import telebot
import random
from telebot import types


access_token = "441033761:AAFZE9ZJxLf6oncWVstygwojL6TwDChZzYc"
# Создание бота с указанным токеном доступа
bot = telebot.TeleBot(access_token)

@bot.message_handler(commands=['start'])
def startBot(message):
    key = types.ReplyKeyboardMarkup()
    key.row('Симпсоны', 'Гриффины', 'Саус Парк', '2 страница')
    bot.send_message(message.chat.id,"Используете кнопки чтоб выбрать название мультика или напишите его вручную, выбрав из списка: Симпсоны, Гриффины, Саус Парк, Американский папаша, Рик и Морти, Время приключений, Мы обычные медведи, Шоу Кливленда, Футурама,Бургеры Боба, Царь горы ,Приграничный город, Бриклберри, Мультреалити.", reply_markup=key)

@bot.message_handler(content_types=['text'])
def sss(message):
    if message.text == '1 страница':
        startBot(message)  
    if message.text == '2 страница':
        page2(message)
    if message.text == '3 страница':
        page3(message)
    if message.text == '4 страница':
        page4(message)
    if message.text == '5 страница':
        page5(message)
    if message.text == '6 страница':
        page6(message)        
    if message.text == 'К началу':
        startBot(message)    
    if message.text == 'Симпсоны':
        simpsons(message)
    if 's' in message.text:
        simpsons2(message)
    if 'Рандомная серия Симпсонов' in message.text:
        simpsonsr(message)
    if message.text == 'Гриффины':
        familyguy(message)
    if 'g' in message.text:
        familyguy2(message)
    if 'Рандомная серия Гриффинов' in message.text:
        familyguyr(message)
    if message.text == 'Саус Парк':
        park(message)
    if 'p' in message.text:
        park2(message)
    if 'Рандомная серия Саус Парка' in message.text:
        parkr(message) 
    if message.text == 'Американский папаша':
        american(message)
    if 'a' in message.text:
        american2(message)
    if 'Рандомная серия Американского Папаши' in message.text:
        americanr(message)
    if message.text == 'Рик и Морти':
        rickandmorty(message)
    if 'rm' in message.text:
        rickandmorty2(message)
    if 'Рандомная серия Рика и Морти' in message.text:
        rickandmortyr(message) 
    if message.text == 'Время приключений':
        adventuretime(message)
    if 't' in message.text:
        adventuretime2(message)
    if  message.text == 'Рандомная серия Время приключений':    
        adventuretimer(message)
    if message.text == 'Мы обычные медведи':
            bears(message)
    if 'b' in message.text:
            bears2(message)
    if  message.text == 'Рандомная серия Мы обычные медведи':    
            bearsr(message)         
    if message.text == 'Шоу Кливленда':
            klivlend(message)
    if 'k' in message.text:
            klivlend2(message)
    if  message.text == 'Рандомная серия Шоу Кливленда':    
            klivlendr(message)
    if message.text == 'Футурама':
        futurama(message)
    if 'f' in message.text:
        futurama2(message)
    if  message.text == 'Рандомная серия Футурамы':    
        futuramar(message)
    if message.text == 'Бургеры Боба':
        burgers(message)
    if 'n' in message.text:
        burgers2(message)
    if  message.text == 'Рандомная серия Бургеры Боба':    
        burgersr(message)
    if message.text == 'Царь горы':
        king(message)
    if 'c' in message.text:
        king2(message)
    if  message.text == 'Рандомная серия Царь горы':    
        kingr(message)
    if message.text == 'Приграничный город':
        city(message)
    if 'u' in message.text:
        city2(message)
    if  message.text == 'Рандомная серия Приграничный город':    
        cityr(message)
    if message.text == 'Бриклберри':
        brik(message)
    if 'l' in message.text:
        brik2(message)
    if  message.text == 'Рандомная серия Бриклберри':    
        brikr(message)
    if message.text == 'Мультреалити':
        multi(message)
    if 'm' in message.text:
        multi2(message)
    if  message.text == 'Рандомная серия Мультреалити':    
        multir(message)

def multi(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Мультреалити')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате m101 для 1 сезона 1 серии или m111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def multi2(message):
    global mssg
    mssg = message.text
    url = "http://drawntogether.cc-fan.tv/series.php?id=" + mssg[1:]
    bot.send_message(message.chat.id, url)

def multir(message):
    season = random.randint(1, 3)
    episod ='0' + str(random.randint(1, 9))
    url = "http://drawntogether.cc-fan.tv/series.php?id=" + str(season) + str(episod)
    bot.send_message(message.chat.id, url)

def brik(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Бриклберри')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате l101 для 1 сезона 1 серии или l111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def brik2(message):
    global mssg
    mssg = message.text
    url = "http://brickleberry.cc-fan.tv/series.php?id=" + mssg[1:]
    bot.send_message(message.chat.id, url)

def brikr(message):
    season = random.randint(1, 3)
    episod ='0' + str(random.randint(1, 9))
    url = "http://brickleberry.cc-fan.tv/series.php?id=" + str(season) + str(episod)
    bot.send_message(message.chat.id, url)

def page6(message):
    key = types.ReplyKeyboardMarkup()
    key.row('5 страница','Приграничный город', 'Бриклберри', 'Мультреалити')
    bot.send_message(message.chat.id,"Используете кнопки чтоб выбрать название мультика или напишите его вручную, выбрав из списка: Симпсоны, Гриффины, Саус Парк, Американский папаша, Рик и Морти, Время приключений, Мы обычные медведи, Шоу Кливленда, Футурама,Бургеры Боба, Царь горы ,Приграничный город, Бриклберри, Мультреалити.", reply_markup=key)
    
def city(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Приграничный город')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате u101 для 1 сезона 1 серии или u111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def city2(message):
    global mssg
    mssg = message.text
    url = "http://bordertown.fox-fan.ru/series.php?id=" + mssg[1:]
    bot.send_message(message.chat.id, url)

def cityr(message):
    episod ='0' + str(random.randint(1, 9))
    url = "http://bordertown.fox-fan.ru/series.php?id=" + "1" + str(episod)
    bot.send_message(message.chat.id, url)


def king(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Царь горы')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате c101 для 1 сезона 1 серии или c111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def king2(message):
    global mssg
    mssg = message.text
    url = "http://kingofthehill.fox-fan.ru/series.php?id=" + mssg[1:]
    bot.send_message(message.chat.id, url)

def kingr(message):
    season = random.randint(1, 13)
    episod ='0' + str(random.randint(1, 9))
    url = "http://kingofthehill.fox-fan.ru/series.php?id=" + str(season) + str(episod)
    bot.send_message(message.chat.id, url)


def burgers(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Бургеры Боба')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате n101 для 1 сезона 1 серии или n111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def burgers2(message):
    global mssg
    mssg = message.text
    url = "http://bobsburgers.fox-fan.ru/series.php?id=" + mssg[1:]
    bot.send_message(message.chat.id, url)

def burgersr(message):
    season = random.randint(1, 8)
    episod ='0' + str(random.randint(1, 9))
    url = "http://bobsburgers.fox-fan.ru/series.php?id=" + str(season) + str(episod)
    bot.send_message(message.chat.id, url)
        
def page5(message):
    key = types.ReplyKeyboardMarkup()
    key.row('4 страница','Бургеры Боба', 'Царь горы', '6 страница')
    bot.send_message(message.chat.id,"Используете кнопки чтоб выбрать название мультика или напишите его вручную, выбрав из списка: Симпсоны, Гриффины, Саус Парк, Американский папаша, Рик и Морти, Время приключений, Мы обычные медведи, Шоу Кливленда, Футурама,Бургеры Боба, Царь горы ,Приграничный город, Бриклберри, Мультреалити.", reply_markup=key)
    
def futurama(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Футурамы')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате f101 для 1 сезона 1 серии или f111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def futurama2(message):
    global mssg
    mssg = message.text
    url = "http://futurama.fox-fan.ru/series.php?id=" + mssg[1:]
    bot.send_message(message.chat.id, url)

def futuramar(message):
    season = random.randint(1, 4)
    episod ='0' + str(random.randint(1, 9))
    url = "http://futurama.fox-fan.ru/series.php?id=" + str(season) + str(episod)
    bot.send_message(message.chat.id, url)
    
def klivlend(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Шоу Кливленда')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате k101 для 1 сезона 1 серии или k111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def klivlend2(message):
    global mssg
    mssg = message.text
    url = "http://clevelandshow.fox-fan.ru/series.php?id=" + mssg[1:]
    bot.send_message(message.chat.id, url)

def klivlendr(message):
    season = random.randint(1, 3)
    episod ='0' + str(random.randint(1, 9))
    url = "http://clevelandshow.fox-fan.ru/series.php?id=" + str(season) + str(episod)
    bot.send_message(message.chat.id, url)
    
def page4(message):
    key = types.ReplyKeyboardMarkup()
    key.row('3 страница','Шоу Кливленда', 'Футурама', '5 страница')
    bot.send_message(message.chat.id,"Используете кнопки чтоб выбрать название мультика или напишите его вручную, выбрав из списка: Симпсоны, Гриффины, Саус Парк, Американский папаша, Рик и Морти, Время приключений, Мы обычные медведи, Шоу Кливленда, Футурама,Бургеры Боба, Царь горы ,Приграничный город, Бриклберри, Мультреалити.", reply_markup=key)  
    

def bears(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Мы обычные медведи')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате b101 для 1 сезона 1 серии или b111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def bears2(message):
    global mssg
    mssg = message.text
    url = "http://webarebears.cn-fan.ru/series.php?id=" + mssg[1:]
    bot.send_message(message.chat.id, url)

def bearsr(message):
    season = random.randint(1, 3)
    episod ='0' + str(random.randint(1, 9))
    url = "http://webarebears.cn-fan.ru/series.php?id=" + str(season) + str(episod)
    bot.send_message(message.chat.id, url)
    
def page2(message):
    key = types.ReplyKeyboardMarkup()
    key.row('1 страница','Американский папаша', 'Рик и Морти', '3 страница')
    bot.send_message(message.chat.id,"Используете кнопки чтоб выбрать название мультика или напишите его вручную, выбрав из списка: Симпсоны, Гриффины, Саус Парк, Американский папаша, Рик и Морти, Время приключений, Мы обычные медведи, Шоу Кливленда, Футурама,Бургеры Боба, Царь горы ,Приграничный город, Бриклберри, Мультреалити.", reply_markup=key) 

def page3(message):
    key = types.ReplyKeyboardMarkup()
    key.row('2 страница','Время приключений', 'Мы обычные медведи', '4 страница')
    bot.send_message(message.chat.id,"Используете кнопки чтоб выбрать название мультика или напишите его вручную, выбрав из списка: Симпсоны, Гриффины, Саус Парк, Американский папаша, Рик и Морти, Время приключений, Мы обычные медведи, Шоу Кливленда, Футурама,Бургеры Боба, Царь горы ,Приграничный город, Бриклберри, Мультреалити.", reply_markup=key)     
     
def simpsons(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Симпсонов')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате s101 для 1 сезона 1 серии или s111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def simpsons2(message):
    global mssg
    mssg = message.text
    url = "http://www.simp-fan.ru/episode/" + mssg[1:]
    bot.send_message(message.chat.id, url)

def simpsonsr(message):
    season = random.randint(1, 29)
    episod ='0' + str(random.randint(1, 9))
    url = "http://www.simp-fan.ru/episode/" + str(season) + str(episod)
    bot.send_message(message.chat.id, url)
    
def familyguy(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Гриффинов')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате g101 для 1 сезона 1 серии или g111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def familyguy2(message):
    global mssg
    mssg = message.text
    url = "http://www.grif-fan.ru/episode/" + mssg[1:]
    bot.send_message(message.chat.id, url)

def familyguyr(message):
    season = random.randint(1, 16)
    episod ='0' + str(random.randint(1, 9))
    url = "http://www.grif-fan.ru/episode/" + str(season) + str(episod)
    bot.send_message(message.chat.id, url)  

def park(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Саус Парка')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате p101 для 1 сезона 1 серии или p111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def park2(message):
    global mssg
    mssg = message.text
    url = "http://sp.freehat.cc/episode/" + mssg[1:]
    bot.send_message(message.chat.id, url)

def parkr(message):
    season = random.randint(1, 21)
    episod ='0' + str(random.randint(1, 9))
    url = "http://sp.freehat.cc/episode/" + str(season) + str(episod)
    bot.send_message(message.chat.id, url)

def american(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Американского Папаши')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате a101 для 1 сезона 1 серии или a111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def american2(message):
    global mssg
    mssg = message.text
    url = "http://www.dad-fan.ru/episode/" + mssg[1:]
    bot.send_message(message.chat.id, url)

def americanr(message):
    season = random.randint(1, 14)
    episod ='0' + str(random.randint(1, 7))
    url = "http://www.dad-fan.ru/episode/" + str(season) + str(episod)
    bot.send_message(message.chat.id, url)
    
def rickandmorty(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Рика и Морти')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате rm101 для 1 сезона 1 серии или rm110 для 1 сезона 10 серии, либо выберите кнопками другой вариант", reply_markup=key)    

def rickandmorty2(message):
    global mssg
    mssg = message.text
    url = "http://rickandmorty.cn-fan.ru/series.php?id=" + mssg[2:]
    bot.send_message(message.chat.id, url)

def rickandmortyr(message):
    season = random.randint(1, 3)
    episod ='0' + str(random.randint(1, 9))
    url = "http://rickandmorty.cn-fan.ru/series.php?id=" + str(season) + str(episod)
    bot.send_message(message.chat.id, url)   

def adventuretime(message):
    key = types.ReplyKeyboardMarkup()
    key.row('К началу', 'Рандомная серия Время приключений')
    bot.send_message(message.chat.id, "Напишите номер сезона и серии в формате t101 для 1 сезона 1 серии или t111 для 1 сезона 11 серии, либо выберите кнопками другой вариант", reply_markup=key)

def adventuretime2(message):
    global mssg
    mssg = message.text
    url = "http://adventuretime.cn-fan.ru/series.php?id=" + mssg[1:]+ "a"
    bot.send_message(message.chat.id, url)

def adventuretimer(message):
    season = random.randint(1, 3)
    episod ='0' + str(random.randint(1, 9))
    url = "http://adventuretime.cn-fan.ru/series.php?id=" + str(season) + str(episod)+"a"
    bot.send_message(message.chat.id, url)


    
if __name__ == '__main__':
    bot.polling(none_stop=True)