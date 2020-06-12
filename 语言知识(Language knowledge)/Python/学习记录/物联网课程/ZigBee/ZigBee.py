# coding=gb18030

import serial  # 导入serial包
import time  # 导入time包
import pymysql  # 导入pymysql包

log = 0  # 设一个log变量用于记录单次接收次数
s = serial.Serial('com1', 9600, timeout=2)  # 打开串口，配置串口
db = pymysql.connect("localhost", "root", "jinhao", "zigbees")  # 打开数据库，配置数据库
cursor = db.cursor()  # 数据库操作
cursor.execute("DROP TABLE IF EXISTS Monitor_Data")  # 如果存在表则重新创建
creatTab = """CREATE TABLE Monitor_Data( # 创建表
    LOG_ID INT NOT NULL,
    D_ID CHAR(20) NOT NULL,
    TIME CHAR(50),
    T_DATA INT ,
    H_DATA INT ,
    L_DATA FLOAT )"""
cursor.execute(creatTab)  # 执行数据库语句

while True:  # 无限循环读取数据
    localtime = time.asctime(time.localtime(time.time()))  # time包操作，打印本地时间
    n = s.readline()  # 读取串口一行数据
    log += 1  # 传输次数记录+1
    data_pre = str(n)  # 强制用字符串格式
    data = data_pre[2:]  # 取部分数据
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 规整本地时间的格式
    did = data[0:4]  # 分类取有效数据
    print(data)
    td = int(data[4:6])
    hd = int(data[6:8])
    ld = float(data[8:len(data)-6])
    print(local_time, did, td, hd, ld)  # 打印结果在控制台

    sql = "INSERT INTO Monitor_Data(LOG_ID,D_ID,TIME,T_DATA,H_DATA,L_DATA)VALUES('%d','%s','%s','%d','%d','%f')" % (
        log, did, local_time, td, hd, ld)  # 存入数据库
    cursor.execute(sql)  # 执行数据库语句
    db.commit()  # 提交

cursor.close()
db.close()
