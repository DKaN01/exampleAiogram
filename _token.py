def getToken() -> str:
    try:
        with open("./token", "r") as file:
            return file.read()
    except:
        raise Exception("Please create file 'token' and write him token telegram bot")