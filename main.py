import telebot
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from telebot import types
import requests                                     #pip install bs4 lxml selenium
from bs4 import BeautifulSoup


bot = telebot.TeleBot(open("key.txt").readline())

murkup=types.ReplyKeyboardMarkup(resize_keyboard=True)

item1=types.KeyboardButton("AM_4")
item2=types.KeyboardButton("1151v2")
item3=types.KeyboardButton("LGA_1200")
item4=types.KeyboardButton("TR_4")

murkup.add(item1,item2,item3,item4)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Выберите сокет',reply_markup=murkup)


@bot.message_handler(content_types=['text'])
def bred(message):

    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, напиши сокет который тебе нужен.(AM_4;LGA_1200;1151v2;TR_4;),а бот выведет тебе самый популярный вариант.")
    
    
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши привет")


    if message.text == "AM_4":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1=types.KeyboardButton("AM4_CPU")
        item2=types.KeyboardButton("AM4_Mb")
        
        markup.add(item1,item2)
                
        bot.send_message(message.chat.id,'Привет, напиши что тебе нужна материнская плата(M_b), если процессор- (CPU),тоесть (AM4_Mb)',reply_markup=markup)
    
    if message.text == "1151v2":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1=types.KeyboardButton("1151v2_CPU")
        item2=types.KeyboardButton("1151v2_Mb")

        markup.add(item1,item2)
                
        bot.send_message(message.chat.id,'Привет, напиши что тебе нужна материнская плата(M_b), если процессор- (CPU),тоесть (AM4_Mb)',reply_markup=markup)
    
    if message.text == "LGA_1200":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1=types.KeyboardButton("LGA_1200_CPU")
        item2=types.KeyboardButton("LGA_1200_Mb")

        markup.add(item1,item2)

        bot.send_message(message.chat.id,'Привет, напиши что тебе нужна материнская плата(M_b), если процессор- (CPU),тоесть (AM_4M_b)',reply_markup=markup)
    
    if message.text == "TR4":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1=types.KeyboardButton("TR4_CPU")
        item2=types.KeyboardButton("TR4_Mb")
    
        markup.add(item1,item2)
                
        bot.send_message(message.chat.id,'Привет, напиши что тебе нужна материнская плата(M_b), если процессор- (CPU),тоесть (AM_4M_b)',reply_markup=markup)

    if message.text == "AM4_CPU":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1=types.KeyboardButton("AM4_8CORE")
        item2=types.KeyboardButton("AM4_6CORE")
        item3=types.KeyboardButton("AM4_4CORE")
        item4=types.KeyboardButton("AM4_16CORE")
        markup.add(item1,item2,item3,item4)
        bot.send_message(message.chat.id,'Теперь напиши сколько ядер нужно в твоем процессоре.',reply_markup=markup)

    if message.text == "AM4_8CORE":

        x=parse_dns("https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/?order=6&stock=now-today-tomorrow-later&f[ykgd]=1ii0zc&f[mo]=27m")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])

    if message.text == "AM4_6CORE":

        x=parse_dns("https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/?order=6&stock=now-today-tomorrow-later&f[ykgd]=1ii0zc&f[mo]=27k")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])
    if message.text == "AM4_4CORE":

        x=parse_dns("https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/?order=6&stock=now-today-tomorrow-later&f[ykgd]=1ii0zc&f[mo]=27j")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])  
    
    if message.text == "AM4_16CORE":

        x=parse_dns("https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/?order=6&stock=now-today-tomorrow-later&f[ykgd]=1ii0zc&f[mo]=27n")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])
    
    
    if message.text == "AM4_Mb":
        x=parse_dns("https://www.dns-shop.ru/catalog/17a89a0416404e77/materinskie-platy/?order=6&f[rv2z]=13iyb1")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])
    
    if message.text == "1151v2_CPU":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1=types.KeyboardButton("1151v2_6CORE")
        item2=types.KeyboardButton("1151v2_4CORE")
        markup.add(item1,item2)
    
        bot.send_message(message.chat.id,'Теперь напиши сколько ядер нужно в твоем процессоре.',reply_markup=markup)
    if message.text == "1151v2_6CORE":

        x=parse_dns("https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/?order=6&stock=now-today-tomorrow-later&f[ykgd]=1ii0zg&f[mo]=27k")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])
    
    if message.text == "1151v2_4CORE":

            x=parse_dns("https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/?order=6&stock=now-today-tomorrow-later&f[ykgd]=1ii0zg&f[mo]=27j")
            bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])

    if message.text == "1151v2_Mb":
        x=parse_dns("https://www.dns-shop.ru/catalog/17a89a0416404e77/materinskie-platy/?order=6&f[rv2z]=13j0rf")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])
    
    if message.text == "TR4_CPU":
        x=parse_dns("https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/?order=6&f[ykgd]=1ii0zp")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])
    
    if message.text == "TR4_Mb":
        x=parse_dns("https://www.dns-shop.ru/catalog/17a89a0416404e77/materinskie-platy/?order=6&f[rv2z]=13j0yi")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])
    
    if message.text == "LGA_1200_CPU":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)

        item1=types.KeyboardButton("LGA1200_8CORE")
        item2=types.KeyboardButton("LGA1200_6CORE")
        item3=types.KeyboardButton("LGA1200_4CORE")
        markup.add(item1,item2,item3)
        bot.send_message(message.chat.id,'Теперь напиши сколько ядер нужно в твоем процессоре.',reply_markup=markup)

    if message.text == "LGA1200_8CORE":

        x=parse_dns("https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/?order=6&stock=now-today-tomorrow-later&f[ykgd]=1ii0zi&f[mo]=27m")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])
    if message.text == "LGA1200_6CORE":

        x=parse_dns("https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/?order=6&stock=now-today-tomorrow-later&f[ykgd]=1ii0zi&f[mo]=27k")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])
    
    if message.text == "LGA1200_4CORE":

        x=parse_dns("https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/?order=6&stock=now-today-tomorrow-later&f[ykgd]=1ii0zi&f[mo]=27j")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])
    
    if message.text == "LGA_1200_Mb":
        x=parse_dns("https://www.dns-shop.ru/catalog/17a89a0416404e77/materinskie-platy/?order=6&f[rv2z]=13j0y6")
        bot.send_message(message.chat.id,x[0]["name"]+" "+ x[0]["price"]+" "+ x[0]["link"])




def parse_dns(url):
    driver = webdriver.Chrome('chromedriver.exe')  # Optional argument, if not specified will search path.
    chr_opt = Options().add_argument("--disable-extentions")
    print("Opening chrome")
    driver.get(url)

    time.sleep(3)
    page = driver.page_source
    driver.quit()

    soup = BeautifulSoup(page, "lxml")
    print('Parsing..')

    elems = soup.find_all('div', class_ = 'catalog-product ui-button-widget')
    items = list()

    for el in elems:
        tmp = el.find('a', class_ = 'catalog-product__name ui-link ui-link_black')
        items.append(dict(
                name = tmp.find('span').text, 
                price = el.find('div', class_ = 'product-buy__price').text.replace(' ₽', ''),
                link = 'https://www.dns-shop.ru' + tmp['href']
        ))

    return items
bot.polling(none_stop=True, interval=0)