# import pandas as pd   #  pip install pandas
# import sqlite3

# conn = sqlite3.connect('database.db')
# a = pd.read_sql('SELECT * FROM `A-block`', conn)
# b = pd.read_sql('SELECT * FROM `Б-block`', conn)
# v = pd.read_sql('SELECT * FROM `В-block`', conn)
# g = pd.read_sql('SELECT * FROM `Г-block`', conn)
# # a.to_excel(f'result.xlsx', index=True)

# with pd.ExcelWriter('output.xlsx') as writer:  
#     a.to_excel(writer, sheet_name='Sheet_name_1')
#     b.to_excel(writer, sheet_name='Sheet_name_2')
# b.to_excel(f'result-b.xlsx', index=False)
# v.to_excel(f'result-v.xlsx', index=False)
# g.to_excel(f'result-g.xlsx', index=False)
# import sqlite3



# con = sqlite3.connect('database.db')
# cur= con.cursor()
# # block
# # pod
# # floor
# # n_house
# # quantity_r
# # kvm
# # price
# # status
# # cur.execute('INSERT INTO `houses`(block,pod,floor,n_house,quantity_r,kvm,price,status)VALUES(?,?,?,?,?,?,?',())

# for i in range(1,41):
#     if i <=20 :
#         if i >=1 and  i <=4:
#             if i == 3:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',1,1,i,1))
#             else:    
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',1,1,i,2))
#         elif i >=5 and  i <=8:
#             if i==7:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',1,2,i,1))
#             else:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',1,2,i,2))
#         elif i >=9 and  i <=12:
#             if i == 11:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',1,3,i,1))
#             else:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',1,3,i,2))
#         elif i >=13 and  i <=16:
#             if i==15:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',1,4,i,1))
#             else:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',1,4,i,2))
#         elif i >=17 and  i <=20:
#             if i==19:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',1,5,i,1))
#             else:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',1,5,i,2))
    
#     elif i>=20:
#         if i >=21 and  i <=24:
#             if i==23:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',2,1,i,3))
#             else:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',2,1,i,2))
#         elif i >=25 and  i <=28:
#             if i==27:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',2,2,i,3))
#             else:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',2,2,i,2))
#         elif i >=29 and  i <=32:
#             if i==31:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',2,3,i,3))    
#             else:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',2,3,i,2))
#         elif i >=33 and  i <=36:
#             if i==35:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',2,4,i,3))
#             else:
#                 cur.execute('INSERT INTO `Б-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',2,4,i,2))
#         elif i >=37 and  i <=40:
#             if i==39:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',2,5,i,3))    
#             else:
#                 cur.execute('INSERT INTO `В-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('В',2,5,i,2))

# fg = [27,30,33,36,39]

# a = [1,4,5,8,9,12,13,16,17,20,21,24,25,28,29,32,33,36,37,40]#62.2
# b= [2,6,10,14,18,23,27,31,35,39]#70.14
# c = [3,7,11,15,19]#43,93
# d = [1,5,9,13,17]#73,6
# e=  [2,6,10,14,18]#53.7
# f = [4,8,12,16,20]#65,41
# j = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# h= [1,5,9,13,17]
# # l = [16,17,18,19,20,21,22,23,24,25]
# for i in h:
#     cur.execute('UPDATE `В-block` SET quantity_r=? WHERE n_house=?',(3,i))
# con.commit()
# a = [1,2,3,4,5]
# for i in a:
#     if i ==1:
#         cur.execute('UPDATE `Г-block` SET price=? WHERE floor = ? ',(7200000,i))
#     elif i==2:       
#         cur.execute('UPDATE `Г-block` SET price=? WHERE floor = ? ',(7300000,i))
#     elif i==3:       
#         cur.execute('UPDATE `Г-block` SET price=? WHERE floor = ? ',(7200000,i))
#     elif i==4:       
#         cur.execute('UPDATE `Г-block` SET price=? WHERE floor = ? ',(6750000,i))
#     elif i==5:       
#         cur.execute('UPDATE `Г-block` SET price=? WHERE floor = ? ',(6650000,i))

# cur.execute('UPDATE `Г-block` SET status=? WHERE block=?',('✅','Г'))

# for i in range(1,41):
#     if i <=40 :
#         if i >=26 and  i <=28:  
#                 cur.execute('INSERT INTO `Г-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('Г',1,1,i,2))
#         elif i >=29 and  i <=31:
#                 cur.execute('INSERT INTO `Г-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('Г',1,2,i,2))
#         elif i >=32 and  i <=34:
#                 cur.execute('INSERT INTO `Г-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('Г',1,3,i,2))
#         elif i >=35 and  i <=37:
#                 cur.execute('INSERT INTO `Г-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('Г',1,4,i,2))
#         elif i >=38 and  i <=40:
#                 cur.execute('INSERT INTO `Г-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('Г',1,5,i,2))

# for i in range(1,41):
#     if i <=25 :
#         if i >=16 and  i <=17:  
#                 cur.execute('INSERT INTO `Г-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('Г',1,1,i,3))
#         elif i >=18 and  i <=19:
#                 cur.execute('INSERT INTO `Г-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('Г',1,2,i,3))
#         elif i >=20 and  i <=21:
#                 cur.execute('INSERT INTO `Г-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('Г',1,3,i,3))
#         elif i >=22 and  i <=23:
#                 cur.execute('INSERT INTO `Г-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('Г',1,4,i,3))
#         elif i >=24 and  i <=25:
#                 cur.execute('INSERT INTO `Г-block`(block,pod,floor,n_house,quantity_r) VALUES(?,?,?,?,?)',('Г',1,5,i,3))
# con.commit()