import telegram

chat_id = 1162346320

token = "6243318407:AAEMbNyi5srikgf_mMAe87Dh9sfj86QW73"
bot = telegram.Bot(token)
updates = bot.getUpdates()
print(updates[0].mesage.chat_id)
