from aiogram import Router
from aiogram.filters import CommandStart, Command

base_router = Router()


@base_router.message(CommandStart())
async def cmd_start(message):
    await message.answer("""🌟 Добро пожаловать в QuantumStateAssessor! 🌟\n
Здесь вы можете оценить научно-техническое состояние для квантовой передачи. 
Мы предлагаем передовые решения и аналитические инструменты для изучения и оптимизации квантовых систем.\n 
Введите команду /evaluate, чтобы начать.
Если вам нужна помощь, просто напишите /help.\n
Готовы погрузиться в мир квантовых технологий? Давайте начнем!
""")


@base_router.message(Command("help"))
async def cmd_help(message):
    await message.answer("Help menu")
