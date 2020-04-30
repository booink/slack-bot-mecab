import os
import traceback
from slackbot.bot import Bot

def main():
    print("running")
    try:
        bot = Bot()
        bot.run()
        print("run")
    except Exception as e:
        print(str(e))
        traceback.print_exc()
        exit(1)

if __name__ == '__main__':
    main()

