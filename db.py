import pandas as pd
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine

from config import *


class DataBase:
    def __init__(self):
        self.engine = create_async_engine(f'postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}/{DATABASE}')

    async def check_house(self, block, n_house):
        async with self.engine.begin() as cur:
            res = (await cur.execute(text(f'SELECT n_house FROM "{block}-block" WHERE n_house={n_house}'))).fetchall()
            return bool(len(res))
            # g = []
            # for i in res:
            #     a= f'{i[0]}\n {i[1]}\n {i[2]}\n{i[3]}\n{i[4]}\n{i[5]}\n{i[6]}\n{i[7]}\n '
            #     g.append(a)
            # return ''.join(g)

    async def info_house(self, block, n_house):
        async with self.engine.begin() as cur:
            res = (await cur.execute(
                text(
                    f'SELECT block,pod,floor,n_house,quantity_r,kvm,price,status FROM "{block}-block" WHERE n_house={n_house}'))).fetchall()
            # g = []
            # for i in res:
            #     a= f'{i[0]}-blok\n{i[1]}-podezd\n{i[2]}-qavat\n{i[3]}-honadon\n{i[4]} xonali\n{i[5]} kv.m\n{i[6]}-kv.m narxi\nstatus:{i[7]}\n '
            #     g.append(a)
            # return ''.join(g)
            print(res)
            return res

    async def list_houses_a(self):
        async with self.engine.begin() as cur:
            res = (await cur.execute(text('SELECT block,n_house,status FROM "A-block" ORDER BY n_house ASC'))).fetchall()

            g = []
            for i in res:
                a = f'__________________________\n<b>{i[0]}</b>-block  |  <b>{i[1]}</b>-honadon  |  status:{i[2]}\n__________________________'
                g.append(a)
            return ''.join(g)

    async def list_houses_b(self):
        async with self.engine.begin() as cur:
            res = (await cur.execute(text('SELECT block,n_house,status FROM "Б-block" ORDER BY n_house ASC'))).fetchall()

            g = []
            for i in res:
                a = f'__________________________\n<b>{i[0]}</b>-block  |  <b>{i[1]}</b>-honadon  |  status:{i[2]}\n__________________________'
                g.append(a)
            return ''.join(g)

    async def list_houses_v(self):
        async with self.engine.begin() as cur:
            res = (await cur.execute(text('SELECT block,n_house,status FROM "В-block" ORDER BY n_house ASC'))).fetchall()

            g = []
            for i in res:
                a = f'__________________________\n<b>{i[0]}</b>-block  |  <b>{i[1]}</b>-honadon  |  status:{i[2]}\n__________________________'
                g.append(a)
            return ''.join(g)

    async def list_houses_g(self):
        async with self.engine.begin() as cur:
            res = (await cur.execute(text('SELECT block,n_house,status FROM "Г-block" ORDER BY n_house ASC'))).fetchall()

            g = []
            for i in res:
                a = f'__________________________\n<b>{i[0]}</b>-block  |  <b>{i[1]}</b>-honadon  |  status: {i[2]}\n__________________________'
                g.append(a)
            return ''.join(g)

    async def status_edit(self, block, msg, status):
        async with self.engine.begin() as cur
            await cur.execute(text(f'UPDATE "{block}-block" SET status=\'{status}\' WHERE n_house=\'{msg}\''))
            return 'status uzgardi'

    async def excel_file(self, block):
        async with self.engine.begin() as cur:
            a = pd.read_sql(text(f'SELECT * FROM "{block}-block"'), self.engine)
            a.to_excel(f'result.xlsx', index=True)
