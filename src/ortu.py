from .murid import murid
from .user import user

import datetime
import time
from datetime import date, timedelta

import mysql.connector as eskuel
dbaseee = eskuel.connect(
        user="root",
        password="password_to_OP3N",
        host="localhost",
        database="prak_ppl",
        autocommit=True,
        auth_plugin='mysql_native_password'
    )

class ortu:

    def __init__(self, USER):
        self.USER = USER
        self.anak = {}

    def getName(self):
        return self.USER.getName()

    def getID(self):
        return self.USER.getID()

    def setAnak(self, murid):
        myc = dbaseee.cursor()
        query = "select id from users where nama = '{}'".format(murid)
        myc.execute(query)
        records = myc.fetchall()
        idmuridnyaortu = str(self.getAnak())
        if (idmuridnyaortu == ""):
            ididmuridnyaortu = str(records[0][0])
        else:
            ididmuridnyaortu = idmuridnyaortu + "," + str(records[0][0])
        qK = 'update users set idmuridnyaortu ="'+ididmuridnyaortu+'" where nama ="'+self.getName()+'"'
        myc.execute(qK)

    def getAnak(self):
        myc = dbaseee.cursor()
        query = "select idmuridnyaortu from users where id = '{}'".format(self.getID())
        myc.execute((query))
        records = myc.fetchall()
        list_child = records[0][0].split(',')
        list_name = ''

        for i in range(len(list_child)):
            myc = dbaseee.cursor()
            query = 'select nama from users where id='+list_child[i]
            myc.execute(query)
            records = myc.fetchall()
            list_name += (str(records[0][0]) + '\n')

        return list_name

    def banyakAnak(self):
        return len(self.anak.keys())

    def getUserData(self):
        return self.USER.getUserData()

    def giveAlert(self, text, murid):
        murid.getAlert(text)

    def getTugasAnak(self, namaanak):
        listanak = self.getAnak()
        listanak = listanak.split("\n")
        for j in range(len(listanak)):
            if namaanak == listanak[j]:
                # get nama anak
                myc = dbaseee.cursor(dictionary=True)
                query = 'select * from users where nama="' + listanak[j] + '"'
                myc.execute(query)
                records = myc.fetchall()
                anaknya = records[0]

                anaknya = user(anaknya)
                anaknya = murid(anaknya)

                return anaknya.getTUGAS()


    def getUname(self):
        return self.USER.getUname()


    def nilai(self, tugas):
        return tugas.getNilai()

    def getDeadlineAlert(self):
        listanak = self.getAnak()
        listanak = listanak.split("\n")
        list_child = []
        for j in range(len(listanak)):
            #get nama anak
            myc = dbaseee.cursor(dictionary=True)
            query = 'select * from users where nama="' + listanak[j] + '"'
            myc.execute(query)
            records = myc.fetchall()
            for anaknya in records:
                anaknya = user(anaknya)
                anaknya = murid(anaknya)
                list_child.append(anaknya.getName())
                anaknya.getDeadlineAlert()
        return list_child

    def giveAlert(self,murid,pesan):
        #cari id murid
        myc = dbaseee.cursor()
        query = 'select id from users where nama="'+murid+'"'
        myc.execute(query)
        records = myc.fetchall()
        idmurid = records[0][0]

        #giving alert
        myc = dbaseee.cursor()
        query = 'insert into alert(idmurid, idortu, pesan) values('+str(idmurid)+','+str(self.getID())+',"'+pesan+'")'
        myc.execute(query)
        print("GIVING ALERT SUKSES")



