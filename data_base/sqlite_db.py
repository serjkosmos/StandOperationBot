import sqlite3 as sq
from create_bot import bot

def sql_start():
    global base, cur
    base = sq.connect('deviations')
    cur = base.cursor()
    if base:
        print('Data base connected OK')
    base.execute('CREATE TABLE IF NOT EXISTS deviations(img TEXT, name TEXT PRIMARY KEY, causes TEXT)')
    base.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO deviations VALUES(?,?,?)', tuple(data.values()))
        base.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM deviations').fetchall():
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\nПричины: {ret[2]}')

async def sql_read2():
    return cur.execute('SELECT * FROM deviations').fetchall()

async def sql_delete_command(data):
    cur.execute('DELETE FROM deviations WHERE name == ?', (data,))
    base.commit()