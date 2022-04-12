import telebot
bot = telebot.TeleBot(open("key.txt").readline())

from telebot import types


import requests


from bs4 import BeautifulSoup

murkup=types.ReplyKeyboardMarkup(resize_keyboard=True)
item1=types.KeyboardButton("AM_4")

item2=types.KeyboardButton("1151v2")

item3=types.KeyboardButton("LGA_1200")

item4=types.KeyboardButton("TR_4")

        
murkup.add(item1,item2,item3,item4)


from bs4 import BeautifulSoup     #pip install bs4 lxml selenium

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options





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


        item1=types.KeyboardButton("AM_4CPU")

        item2=types.KeyboardButton("AM_4M_b")
        
        markup.add(item1,item2)
        
        
        bot.send_message(message.chat.id,'Привет, апиши что тебе нужна материнская плата(M_b), если процессор- (CPU),тоесть (AM_4M_b)',reply_markup=markup)
    
    if message.text == "1151v2":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)


        item1=types.KeyboardButton("1151v2CPU")

        item2=types.KeyboardButton("1151v2M_b")

        
        markup.add(item1,item2)
        
        
        bot.send_message(message.chat.id,'Привет, напиши что тебе нужна материнская плата(M_b), если процессор- (CPU),тоесть (AM_4M_b)',reply_markup=markup)
    
    if message.text == "LGA_1200":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)


        item1=types.KeyboardButton("LGA_1200CPU")

        item2=types.KeyboardButton("LGA_1200M_b")

        
        
        markup.add(item1,item2)
        
        
        bot.send_message(message.chat.id,'Привет, напиши что тебе нужна материнская плата(M_b), если процессор- (CPU),тоесть (AM_4M_b)',reply_markup=markup)
    
    if message.text == "TR_4":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)


        item1=types.KeyboardButton("TR_4CPU")

        item2=types.KeyboardButton("TR4M_b")

    
        markup.add(item1,item2)
        
        
        bot.send_message(message.chat.id,'Привет, напиши что тебе нужна материнская плата(M_b), если процессор- (CPU),тоесть (AM_4M_b)',reply_markup=markup)







driver = webdriver.Chrome('./chromedriver')  # Optional argument, if not specified will search path.
chr_opt = Options().add_argument("--disable-extentions")

def parse_dns(url):
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

#def test_dns():
    #x = parse_dns("https://www.dns-shop.ru/catalog/17a899cd16404e77/processory/?order=6&f[70m]=emb2")
    #for xx in x:
        #print(xx['name'], xx['price'], xx['link'])

#test_dns()