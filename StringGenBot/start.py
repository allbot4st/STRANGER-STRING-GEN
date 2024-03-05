from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""» ʜᴇʏ⚡️{msg.from_user.mention} ⚡,

» 𝐇𝐄𝐘💓{me2}💞💞💞💞,

➳ 𝐈 𝐀𝐦 𝐒ᴛʀɪɴɢ 𝐆ᴇɴ 𝐁ᴏᴛ❣❣,
❥𝗛𝗢𝗪 𝗧𝗢 𝗨𝗦𝗘:- 

☞︎ /start bot
☞︎ seletect pv1 (payrogram v1)
☞︎ tap on /skip
☞︎ share ur id mobile num (eg:- +916969696969)
☞︎ enter otp with space ( eg:- 1 2 3 4 5)
☞︎ done 💆‍♀️...see ur save mesg...✅

𝐌𝐚𝐝𝐞 𝐁𝐲  : 👻4sᴛ 𝐎ᴡɴᴇʀ !
» ɪғ ʏᴏᴜ ɴᴇᴇᴅ ᴀɴʏ ʜᴇʟᴘ, ᴛʜᴇɴ ᴅᴍ ᴛᴏ ᴍʏ ᴏᴡɴᴇʀ: [🌐ㅤ 4ˢᵗ➳𝐌ɪɴᴅ 𝐆ᴀᴍᴇʀ🍃❄](tg://user?id={OWNER_ID}) !""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="⚡𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐒𝐓𝐑𝐈𝐍𝐆⚡", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("⚡️𝗦𝗨𝗣𝗣𝗢𝗥𝗧⚡️", url="https://t.me/CODEX_KA_BAAP_4ST"),
                    InlineKeyboardButton("🕸‌🇻‌‌🇮‌‌🇸‌‌🇮‌‌🇹‌🌸", url="https://t.me/I_m_fighter")
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
