from slackbot.bot import Bot
from slackbot.bot import respond_to
from slackbot.bot import listen_to
import re
import sqlite3
from sql import OriginalSQLLite3


def main():
    slack = Bot()
    slack.run()


@listen_to('show (.*) (.*)')
def show(message, society, name):
    con = sqlite3.connect('./DB/SQL.db')
    cur = con.cursor()
    cur.execute(
        "SELECT * FROM {} where name like '%{}%'".format(society, name))
    array = [[i[1], i[2], i[3], i[4], i[5]] for i in cur]
    con.close()
    print(array)
    message.send("開催日:" + str(array[0][0])+"\n"+"学会名:" + str(array[0][1])+"\n"+"提出締め切り:"
                 + str(array[0][2])+"\n"+"参加締め切り:" + str(array[0][3])+"\n"+"開催地:" + str(array[0][4]))


@listen_to('update (.*)')
def update_data(message, date):
    message.reply('Here is {}'.format(date))


if __name__ == "__main__":
    main()
