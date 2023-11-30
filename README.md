# QuantumStateAssessor
A Python package for assessing the quality of quantum states.

Пакет Python для оценки качества квантовых состояний.

## Installation
Project is written in Python 3.11.5. 
Before installing the package, make sure that you have installed Python 3.11.5 or higher. 
And you create a virtual environment.

To install the package, run the following command:

Проект написан на Python 3.11.5. Перед установкой пакета убедитесь, что у вас установлен Python 3.11.5 или выше. И вы создали виртуальную среду.

Чтобы установить пакет, выполните следующую команду:
```bash
pip install -r requirements.txt
```

## Run Docker
To run the project in Docker, run the following command:

Чтобы запустить проект в Docker, выполните следующую команду:
```bash
docker run -d -e BOT_TOKEN=<your_bot_token> --name <container_name> tgbot
```
or(или)
```bash
docker run -d --env-file .env --name <container_name> tgbot
```