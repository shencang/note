# coding=gb18030

import serial  # ����serial��
import time  # ����time��
import pymysql  # ����pymysql��

log = 0  # ��һ��log�������ڼ�¼���ν��մ���
s = serial.Serial('com1', 9600, timeout=2)  # �򿪴��ڣ����ô���
db = pymysql.connect("localhost", "root", "jinhao", "zigbees")  # �����ݿ⣬�������ݿ�
cursor = db.cursor()  # ���ݿ����


while True:  # ����ѭ����ȡ����
    localtime = time.asctime(time.localtime(time.time()))  # time����������ӡ����ʱ��
    n = s.readline()  # ��ȡ����һ������
    log += 1  # ���������¼+1
    data_pre = str(n)  # ǿ�����ַ�����ʽ
    data = data_pre[2:]  # ȡ��������
    local_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())  # ��������ʱ��ĸ�ʽ
    print(data)

    sql = "INSERT INTO building(BUILDING_ID)VALUES('%s')" % (
        data)  # �������ݿ�
    cursor.execute(sql)  # ִ�����ݿ����
    db.commit()  # �ύ

cursor.close()
db.close()
