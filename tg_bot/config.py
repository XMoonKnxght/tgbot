class Development(Config):
    OWNER_ID = 6447082026  # my telegram ID
    OWNER_USERNAME = "TheHamkerGuy"  # my telegram username
    API_KEY = "8177523077:AAHcf1_-Oxpl_xI3kbCzW9yJtaDkdUOTY8Y"  # my api key, as provided by the botfather
    SQLALCHEMY_DATABASE_URI = 'postgresql://dray:dray@localhost:5432/dray'  # sample db credentials
    MESSAGE_DUMP = '-1002283917072' # some group chat that your bot is a member of
    USE_MESSAGE_DUMP = True
    SUDO_USERS = [7389923621]  # List of id's for users which have sudo access to the bot.
    LOAD = []
    NO_LOAD = ['translation']
