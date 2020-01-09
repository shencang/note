# coding=gb18030

import serial  # 导入serial包
import time  # 导入time包
import pymysql  # 导入pymysql包

log = 0  # 设一个log变量用于记录单次接收次数
s = serial.Serial('com1', 9600, timeout=2)  # 打开串口，配置串口
db = pymysql.connect("localhost", "root", "jinhao", "zigbees")  # 打开数据库，配置数据库
cursor = db.cursor()  # 数据库操作


while True:  # 无限循环读取数据
    localtime = time.asctime(time.localtime(time.time()))  # time包操作，打印本地时间
    n = s.readline()  # 读取串口一行数据
    log += 1  # 传输次数记录+1
    data_pre = str(n)  # 强制用字符串格式
    data = data_pre[2:]  # 取部分数据
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # 规整本地时间的格式
    print(data)

    sql = "INSERT INTO building(BUILDING_ID)VALUES('%s')" % (
        data)  # 存入数据库
    cursor.execute(sql)  # 执行数据库语句
    db.commit()  # 提交

cursor.close()
db.close()
