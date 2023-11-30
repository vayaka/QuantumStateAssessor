from decouple import config


class Config:
    TOKEN = config('BOT_TOKEN')
    ADMINS = config('ADMINS', cast=lambda v: [int(item) for item in v.split(',')])


if __name__ == '__main__':
    config = Config()
    print(config.TOKEN)
    print(config.ADMINS)
