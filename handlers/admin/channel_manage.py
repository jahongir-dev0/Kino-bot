from aiogram import types
from aiogram.dispatcher import FSMContext
from loader import dp
from states.channel_manage import ManageChannels
from utils.db_api.channel import add_channel, remove_channel, get_channels
from data.config import ADMINS
from keyboards.inline.channel_settings import channel_settings_menu

ADMIN_CHANNEL_PATH = "data/admin_channel.txt"

def set_admin_channel_link(username: str):
    with open(ADMIN_CHANNEL_PATH, "w") as f:
        f.write(username)

def get_admin_channel_link():
    try:
        with open(ADMIN_CHANNEL_PATH, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return "@your_channel"

@dp.callback_query_handler(text="channel_settings")
async def show_channel_settings(call: types.CallbackQuery):
    if str(call.from_user.id) not in ADMINS:
        return await call.answer("Ruxsat yo‘q!", show_alert=True)
    await call.message.edit_text("🛠 Kanal sozlamalari:", reply_markup=channel_settings_menu())

@dp.callback_query_handler(text="add_channel")
async def ask_add_channel(call: types.CallbackQuery):
    await call.message.answer("➕ Qo‘shiladigan kanalni kiriting (masalan: @kino_uz):")
    await ManageChannels.add.set()

@dp.message_handler(state=ManageChannels.add)
async def add_channel_handler(message: types.Message, state: FSMContext):
    text = message.text.strip()
    if text.startswith("@"):
        add_channel(text)
        await message.answer(f"✅ {text} kanal qo‘shildi.")
    else:
        await message.answer("❌ Kanal `@` bilan boshlanishi kerak.")
    await state.finish()

@dp.callback_query_handler(text="remove_channel")
async def ask_remove_channel(call: types.CallbackQuery):
    await call.message.answer("➖ Olib tashlanadigan kanalni kiriting (masalan: @kino_uz):")
    await ManageChannels.remove.set()

@dp.message_handler(state=ManageChannels.remove)
async def remove_channel_handler(message: types.Message, state: FSMContext):
    text = message.text.strip()
    if text.startswith("@"):
        remove_channel(text)
        await message.answer(f"❎ {text} kanal olib tashlandi.")
    else:
        await message.answer("❌ Kanal `@` bilan boshlanishi kerak.")
    await state.finish()

@dp.callback_query_handler(text="list_channels")
async def list_channels_handler(call: types.CallbackQuery):
    channels = get_channels()
    if channels:
        await call.message.edit_text("📋 Obuna kanallari:\n" + "\n".join(channels))
    else:
        await call.message.edit_text("🚫 Kanallar ro‘yxati bo‘sh.")

@dp.callback_query_handler(text="set_admin_channel")
async def ask_admin_channel(call: types.CallbackQuery):
    await call.message.answer("🔗 Admin kanal username'ni yuboring (masalan: @kino_admin):")
    await ManageChannels.set_admin.set()

@dp.message_handler(state=ManageChannels.set_admin)
async def set_admin_channel_handler(message: types.Message, state: FSMContext):
    text = message.text.strip()
    if text.startswith("@"):
        set_admin_channel_link(text)
        await message.answer(f"✅ Admin kanal: {text} deb o‘rnatildi.")
    else:
        await message.answer("❌ Kanal `@` bilan boshlanishi kerak.")
    await state.finish()
