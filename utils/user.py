from aiogram import Bot
from utils.db_api.channel import get_channels

async def check_user_subscriptions(bot: Bot, user_id: int) -> bool:
    result = []
    for ch in get_channels():
        try:
            member = await bot.get_chat_member(ch, user_id)
            result.append(member.status in ("member", "creator", "administrator"))
        except:
            result.append(False)
    return all(result)
