
import sqlite3
from aiogram.dispatcher import FSMContext
class DataBase:
    def __init__(self,db_url):
        self.connect = sqlite3.connect(db_url)
        self.cur = self.connect

    async def check_house(self,block,n_house):
        with self.connect:
            res =self.cur.execute(f'SELECT n_house FROM `{block}-block` WHERE n_house=?',(n_house,)).fetchall()
            return bool(len(res))
            # g = []
            # for i in res:
            #     a= f'{i[0]}\n {i[1]}\n {i[2]}\n{i[3]}\n{i[4]}\n{i[5]}\n{i[6]}\n{i[7]}\n '
            #     g.append(a)
            # return ''.join(g)

    async def info_house(self,block,n_house):
        with self.connect:
            res =self.cur.execute(f'SELECT block,pod,floor,n_house,quantity_r,kvm,price,status FROM `{block}-block` WHERE n_house=?',(n_house,)).fetchall()
            g = []
            for i in res:
                a= f'{i[0]}-blok\n{i[1]}-podezd\n{i[2]}-qavat\n{i[3]}-honadon\n{i[4]} xonali\n{i[5]} kv.m\n{i[6]}-kv.m narxi\nstatus:{i[7]}\n '
                g.append(a)
            return ''.join(g)

    async def list_houses_a(self):
        with self.connect:
            res=self.cur.execute('SELECT block,n_house,status FROM `A-block`' ).fetchall()

            g = []
            for i in res:
                a= f'__________________________\n<b>{i[0]}</b>-block  |  <b>{i[1]}</b>-honadon  |  status:{i[2]}\n__________________________'
                g.append(a)
            return ''.join(g)        
    
    async def list_houses_b(self):
        with self.connect:
            res=self.cur.execute('SELECT block,n_house,status FROM `Б-block`' ).fetchall()

            g = []
            for i in res:
                a= f'__________________________\n<b>{i[0]}</b>-block  |  <b>{i[1]}</b>-honadon  |  status:{i[2]}\n__________________________'
                g.append(a)
            return ''.join(g)     

    async def list_houses_v(self):
        with self.connect:
            res=self.cur.execute('SELECT block,n_house,status FROM `В-block`' ).fetchall()

            g = []
            for i in res:
                a= f'__________________________\n<b>{i[0]}</b>-block  |  <b>{i[1]}</b>-honadon  |  status:{i[2]}\n__________________________'
                g.append(a)
            return ''.join(g)     

    async def list_houses_g(self):
        with self.connect:
            res=self.cur.execute('SELECT block,n_house,status FROM `Г-block`' ).fetchall()

            g = []
            for i in res:
                a= f'__________________________\n<b>{i[0]}</b>-block  |  <b>{i[1]}</b>-honadon  |  status:{i[2]}\n__________________________'
                g.append(a)
            return ''.join(g)     

    async def status_edit(self,block,msg,status):
        with self.connect:
            self.cur.execute(f'UPDATE `{block}-block` SET status=? WHERE n_house=?',(status,msg))
            return 'status uzgardi'
            self.connect.commit()