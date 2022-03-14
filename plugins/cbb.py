from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>🪄 Creator : KiruthiVarma \n\n🎓 Language : <code>Python3</code>\n\n✅️ Source Code : <a href='https://github.com/kiruthikvarma55/MOV-UNIVERSE'>Click here</a>\n\nHosting: Heroku (Free)\n\n<b>🔥 Powered by, \n@OYETC.</b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("CLOSE", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
