from aiogram.dispatcher.filters import Command, Text
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.default import menu
from loader import dp, bot
from bs4 import BeautifulSoup
import requests as req

@dp.message_handler(Command("start"))
async def show_menu(message: Message):
    await message.answer("Привет! Я гид Геленджика, выбери то что тебя интересует", reply_markup=menu)


@dp.message_handler(Text(equals=["Погода", "Web камеры", "Еда", "Куда сходить?"]))
async def get_food(message: Message):
    chat_id = message.from_user.id

    if message.text == 'Погода':
        weatherUrl = req.get("https://www.glavmore.ru/")
        weather = 'Сегодня в Геленджике '+get_weather(weatherUrl)
        await bot.send_message(chat_id=chat_id, text=weather)

    if message.text == 'Web камеры':
        cam1 = req.get("https://www.glavmore.ru/webcam/gelendzhik-center.html")
        webCamImg1 = get_cam_img(cam1)
        text = 'Полюбуйся красивым видом:'
        await bot.send_message(chat_id=chat_id, text=text)
        await bot.send_photo(chat_id=chat_id, photo=webCamImg1, caption="https://www.glavmore.ru/")

    if message.text == 'Еда':
        text = 'В нашем городе есть:\n'
        text += 'McDonald’s\n'
        text += 'KFC\n'
        text += 'Burger King\n'
        text += 'Додо Пицца\n'
        await bot.send_message(chat_id=chat_id, text=text)

    if message.text == 'Куда сходить?':
        text = 'Я рекомендую:\n'
        text += '1. Прогуляйтесь по наберкжной\n'
        text += '2. Сходите в горы\n'
        text += '3. Посетите "Сафари Парк"\n'
        text += '4. Прокатитесь на канатной дороге "Олимп"\n'
        await bot.send_message(chat_id=chat_id, text=text)

def get_cam_img(resp):
    soup = BeautifulSoup(resp.text, 'lxml')
    webCamImg = soup.find("img", id="webcam01")['src']
    return webCamImg

def get_weather(resp):
    soup = BeautifulSoup(resp.text, 'lxml')
    weather = soup.find("div", {"class": "weather-report"}).text.replace('геленджик', '')
    return weather