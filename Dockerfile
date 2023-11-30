# Используйте официальный образ Python 3.11
FROM python:3.11.5

# Установите рабочую директорию в контейнере
WORKDIR /usr/src/app

# Копируйте файлы проекта в контейнер
COPY . .

# Установите зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Команда для запуска бота
CMD ["python", "./main.py"]
