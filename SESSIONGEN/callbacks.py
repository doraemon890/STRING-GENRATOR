import traceback
from pyrogram import Client, filters
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup
from SESSIONGEN.generate import generate_session, ask_ques, buttons_ques

ERROR_MESSAGE = """ɪғ ʏᴏᴜ ᴀʀᴇ ɢᴇᴛᴛɪɴɢ ᴇʀʀᴏʀ!
ʏᴏᴜ ʜᴀᴠᴇ ᴅᴏɴᴇ sᴏᴍᴇ ᴍɪsᴛᴀᴋᴇ ᴡʜɪʟᴇ ɢᴇɴᴇʀᴀᴛɪɴɢ.
ɢɪᴠᴇɴ ᴡʀᴏɴɢ ᴅᴀᴛᴀ ᴏʀ ᴇʟsᴇ.
ᴛʀʏ ᴀɢᴀɪɴ ɪғ ʏᴏᴜ ᴄᴀɴ.
ᴏʀ ɪғ ʏᴏᴜ ʜᴀᴠᴇ ғɪʟʟᴇᴅ ᴛʜɪɴɢs ᴄᴏʀʀᴇᴄᴛʟʏ ʙᴜᴛ ɢᴇᴛᴛɪɴɢ ᴇʀʀᴏʀ,
ᴛʜᴇɴ ғᴏʀᴡᴀʀᴅ ᴇʀʀᴏʀ ᴍsɢ ᴛᴏ [𝙹𝙰𝚁𝚅𝙸𝚂](https://t.me/JARVIS_V2) !"""

@Client.on_callback_query(filters.regex(pattern=r"^(generate|pyrogram|pyrogram_bot|telethon_bot|telethon)$"))
async def _callbacks(bot: Client, callback_query: CallbackQuery):
    query = callback_query.matches[0].group(1)
    try:
        if query == "generate":
            await callback_query.answer()
            await callback_query.message.reply(ask_ques, reply_markup=InlineKeyboardMarkup(buttons_ques))
        elif query == "pyrogram":
            await callback_query.answer()
            await generate_session(bot, callback_query.message)
        elif query == "pyrogram_bot":
            await callback_query.answer("» ᴛʜᴇ sᴇssɪᴏɴ ɢᴇɴᴇʀᴀᴛᴇᴅ ᴡɪʟʟ ʙᴇ ᴏғ ᴩʏʀᴏɢʀᴀᴍ ᴠ2.", show_alert=True)
            await generate_session(bot, callback_query.message, is_bot=True)
        elif query == "telethon_bot":
            await callback_query.answer()
            await generate_session(bot, callback_query.message, telethon=True, is_bot=True)
        elif query == "telethon":
            await callback_query.answer()
            await generate_session(bot, callback_query.message, telethon=True)
    except Exception as e:
        print(traceback.format_exc())
        print(e)
        await callback_query.message.reply(ERROR_MESSAGE.format(str(e)))
