from aiogram import types
from loader import dp
from data.config import ADMINS
from keyboards.inline.admin_panel import admin_panel

@dp.callback_query_handler(text="admin_panel")
async def show_admin_panel(call: types.CallbackQuery):
    if str(call.from_user.id) not in ADMINS:
        return await call.answer("Ruxsat yo‘q!", show_alert=True)
    await call.message.edit_text("⚙️ Admin paneliga xush kelibsiz", reply_markup=admin_panel())
