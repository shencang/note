# coding=gb18030

import serial  # ����serial��
import time  # ����time��
import pymysql  # ����pymysql��

log = 0  # ��һ��log�������ڼ�¼���ν��մ���
s = serial.Serial('com1', 9600, timeout=2)  # �򿪴��ڣ����ô���
db = pymysql.connect("localhost", "root", "jinhao", "zigbees")  # �����ݿ⣬�������ݿ�
cursor = db.cursor()  # ���ݿ����
cursor.execute("DROP TABLE IF EXISTS Monitor_Data")  # ������ڱ������´���
creatTab = """CREATE TABLE Monitor_Data( # ������
    LOG_ID INT NOT NULL,
    D_ID CHAR(20) NOT NULL,
    TIME CHAR(50),
    T_DATA INT ,
    H_DATA INT ,
    L_DATA FLOAT )"""
cursor.execute(creatTab)  # ִ�����ݿ����

while True:  # ����ѭ����ȡ����
    localtime = time.asctime(time.localtime(time.time()))  # time����������ӡ����ʱ��
    n = s.readline()  # ��ȡ����һ������
    log += 1  # ���������¼+1
    data_pre = str(n)  # ǿ�����ַ�����ʽ
    data = data_pre[2:]  # ȡ��������
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # ��������ʱ��ĸ�ʽ
    did = data[0:4]  # ����ȡ��Ч����
    print(data)
    td = int(data[4:6])
    hd = int(data[6:8])
    ld = float(data[8:len(data)-6])
    print(local_time, did, td, hd, ld)  # ��ӡ����ڿ���̨

    sql = "INSERT INTO Monitor_Data(LOG_ID,D_ID,TIME,T_DATA,H_DATA,L_DATA)VALUES('%d','%s','%s','%d','%d','%f')" % (
        log, did, local_time, td, hd, ld)  # �������ݿ�
    cursor.execute(sql)  # ִ�����ݿ����
    db.commit()  # �ύ

cursor.close()
db.close()
