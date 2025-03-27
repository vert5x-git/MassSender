from hikka import loader

class AutoChat(loader.Module):
    """Модуль для автопоиска собеседников и отправки сообщений"""
    strings = {"name": "AutoChat"}

    async def client_ready(self, client, db):
        self.client = client
        self.target_chat = "@palata_6numberr"  # Чат для отправки сообщений
        self.message_text = (
            "🌟 Приглашаем вас на ламповые посиделки в нашем чате! 🌟\n\n"
            "Присоединяйтесь к дружной компании, где вас ждут:\n\n"
            "✨ Добрые администраторы, готовые помочь и поддержать!\n"
            "🎉 Увлекательные розыгрыши на звёзды!\n"
            "💬 Интересные обсуждения и весёлые беседы!\n\n"
            "Не упустите возможность стать частью нашей дружной семьи!\n\n"
            "👨‍👩‍👧 Требования к семье:\n\n"
            "🔞 Возраст: от 13\n"
            "👤 Пол: не важен!!!\n\n"
            "👉 Ссылка на чат: @palata_6numberr\n\n"
            "Ждем вас с нетерпением! 💖"
        )

    # Команда /start, которая просто сообщает, что бот запущен
    @loader.command()
    async def start(self, message):
        """Запуск бота"""
        await message.answer("Бот успешно запущен!")

    # Команда /set_chat, чтобы задать целевой чат для отправки сообщений
    @loader.command()
    async def set_chat(self, message, chat_name: str):
        """Устанавливает целевой чат для отправки сообщений"""
        self.target_chat = chat_name
        await message.answer(f"Целевой чат изменён на: {self.target_chat}")

    # Команда /set_message, чтобы задать новый текст для сообщения
    @loader.command()
    async def set_message(self, message, new_message: str):
        """Устанавливает новый текст сообщения"""
        self.message_text = new_message
        await message.answer("Сообщение обновлено!")

    # Команда /i для начала поиска собеседника
    @loader.command()
    async def i(self, message):
        """Запуск поиска собеседников"""
        await message.answer("Поиск собеседников начат!")
        await self.client.send_message(self.target_chat, "Искать собеседника 🌀")

    # Команда /stop для остановки текущего процесса
    @loader.command()
    async def stop(self, message):
        """Останавливает поиск собеседников"""
        await message.answer("Поиск собеседников остановлен!")
        # Если в поиске, останавливаем его
        self.is_running = False
        await self.client.send_message(self.target_chat, "Остановить 💔")