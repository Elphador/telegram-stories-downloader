from config import *
from pyrogram import Client ,filters , enums
from pyroaddon import listen
from pyrogram.errors import *
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon import functions, types
import os
#os.mkdir("downloads")
bot = Client (  "cht",
                api_id = API_ID,
                api_hash = API_HASH ,
                bot_token = BOT_TOKEN 
                )



                
@bot.on_message(filters.private & filters.command(['start']))
async def start(_, m):
    await m.delete()
    usr_name = m.from_user.first_name
    await m.reply(f"**😊hello {usr_name} i am simple telegram stories downloader made by @neuralp\n\n\n1 i can download every protected stories😍 \n2 i can download private stories which is visible only for contacts🤩 \n3 the fun part you can view anyones story without being added or watched in viewers list ,which telegram called it stealth mode😅\n4 the last thing you can use all premium features of story via me🤗\n\nHow to use\n first send me the username of the stories owner , second send me telethon string session to access your account ,you can generate one from @strin9genbot \n\nan open source project https://t.me/Neuralp/248**",disable_web_page_preview=True)

    
@bot.on_message(filters.private & filters.text)
async def storyget(c,m): 
    await m.reply_chat_action(enums.ChatAction.TYPING)
    try :
        await c.get_chat_member(-1001776406696,m.from_user.id)
    except UserNotParticipant:
        await m.reply('**as this Bot provides free service for users you have to join the bot channel \n@neuralp**')
        return
    #session = await bot.ask(m.from_user.id ,"**please send your telethon session string , if you do not have any use @strin9genbot to generate one  **" )
    try :
        async with TelegramClient(StringSession("1BJWap1wBu3UtUKbZUUdxGsid2z35OBjATonOzsLwaswaCLK9JsUabEg60Y8VAwZLsf76hlc9-4ItIN10-OJcdbBXyVwAboyNXozyiSX9RfDd1jd_VvEd7C6c0wEjY8Mg55nf5aBbGelGhMEVbABxHp8xgvkBAvlUHUUqmFpqfaV6Bw-yXZHsUxl9QzOLWuNriphq8Ie6uyLRivycKVnFiwh_DADtZK32Lnsgm7ITiee2_2D_J5YONbxQMmaoaV2Fu46BblCKI63caAME_NVih1I5omg_iodDFMlKPzzoQFF07ymOF4VjQNfAFC6am-i4zgnRv6no1hVbaviGzzq0pQdhDOa9qBM="), API_ID, API_HASH) as client:
          result =await  client(functions.stories.GetPinnedStoriesRequest(
            user_id= m.text.replace('@',''),
            offset_id =42,
            limit=100  ))
          for story in result.stories:
            download = await client.download_media(story.media)
            await m.reply_document(download)
            os.remove(download)
    except Exception as e :
        await m.reply(f'this happened??\n{e}\nplease report @neuralp 🙃')
    await m.reply('Done')
        
        

         
                
print('everything is fine ')
bot.run()
