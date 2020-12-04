from .kelas import kelas
from .tugas import tugas

import datetime
import time
from datetime import date, timedelta
import string

import mysql.connector as eskuel
dbaseee = eskuel.connect(
        user="root",
        password="password_to_OP3N",
        host="localhost",
        database="prak_ppl",
        autocommit=True,
        auth_plugin='mysql_native_password'
    )
myc = dbaseee.cursor()

class murid:

    def __init__(self, USER):

        self.USER = USER
        self.idMurid = USER.getID()
        self.idKelas = USER.getidkelas()

    def getName(self):
        return self.USER.getName()

    def getUname(self):
        return self.USER.getUname()

    def getID(self):
        return self.USER.getID()

    def getKelas(self):
        qK = "select idkelas from users where id = '{}'".format(self.idMurid)
        myc.execute(qK)
        records = myc.fetchall()
        self.kelas = records[0][0]
        return self.kelas

    def getKELAS(self):
        myc = dbaseee.cursor()
        query = 'select idkelas from users where id='+str(self.getID())
        myc.execute(query)
        records = myc.fetchall()
        listidkelas = records[0][0]
        print(listidkelas)
        if listidkelas == None:
            print('kata2')
            return []
        print('duar')
        listidkelas = listidkelas.split(",")
        listkelas = []
        #mencari nama kelas dari list id
        for i in range(len(listidkelas)):
            dict={}
            myc = dbaseee.cursor(dictionary=True)
            query = 'select * from kelas where id='+str(listidkelas[i])
            myc.execute(query)
            recordkelas = myc.fetchall()
            namakelas = recordkelas[0]['namakelas']
            dict['name'] = namakelas
            #cari nama guru
            idteacher = recordkelas[0]['idteacher']
            myc = dbaseee.cursor()
            query = 'select nama from users where id='+str(idteacher)
            myc.execute(query)
            recordsguru = myc.fetchall()
            teacher = recordsguru[0][0]
            dict['teacher'] = teacher
            member = recordkelas[0]['idmember']
            member = member.split(",")
            if (member[0]==''):
                totalmember = 0
            else:
                totalmember = len(member)
            dict['totalmember'] = totalmember
            assignment = recordkelas[0]['idtugas']
            print(assignment)
            if assignment == '' or assignment == None:
                totalassignment = 0
                dict['totalassignments'] = 0
                listkelas.append(dict)
                continue
            assignment = assignment.split(",")
            if(assignment[0]==''):
                totalassignment = 0
            else:
                totalassignment = len(assignment)
            dict['totalassignments'] = totalassignment
            listkelas.append(dict)
        return listkelas

    def getUserData(self):
        return self.USER.getUserData()

    def getTUGAS(self):
        myc = dbaseee.cursor(dictionary=True)
        query = 'select * from nilai where idmurid='+str(self.USER.getID())
        myc.execute(query)
        records = myc.fetchall()
        listtugas = records
        tugastugas = []
        for i in range(len(listtugas)):
            idtugas = listtugas[i]['idtugas']
            #mencari nama tugas dari idtugas yang ada
            myc = dbaseee.cursor(dictionary= True)
            query = 'select * from tugas where id ='+str(idtugas)
            myc.execute(query)
            records = myc.fetchall()

            # penentuan submisi dari objek listtugas
            submission = str(listtugas[i]['submission'])
            if (submission == "0"):
                submission = "Belum Dikerjakan"
            else:
                submission = "Sudah Dikerjakan"
            records[0]['submission'] = submission
            tugastugas.append(records[0])
        return tugastugas

    def kumpulTugas(self, nama,link):
        namatugas = nama
        linktugas = link
        #cari id kelasnya dulu
        myc = dbaseee.cursor(dictionary=True)
        query = 'select * from tugas where nama="'+namatugas+'"'
        myc.execute(query)
        records = myc.fetchall()
        idtugas = str(records[0]['id'])
        deadline = records[0]['deadline']
        if(datetime.datetime.now()>deadline):
            return False

        #update database nilai
        myc = dbaseee.cursor()
        query = 'update nilai set submission=1, file="'+linktugas+'" where idtugas='+idtugas+' and idmurid='+str(self.USER.getID())
        myc.execute(query)

        return True


    def getDeadlineAlert(self):
        myc = dbaseee.cursor(dictionary=True)
        query = 'select * from nilai where idmurid=' + str(self.USER.getID())
        myc.execute(query)
        records = myc.fetchall()
        listtugas = records
        tugasbelumdikerjakan = 0
        listdeadline = []
        for i in range(len(listtugas)):
            idtugas = listtugas[i]['idtugas']
            # mencari nama tugas dari idtugas yang ada
            myc = dbaseee.cursor(dictionary=True)
            query = 'select * from tugas where id =' + str(idtugas)
            myc.execute(query)
            records = myc.fetchall()
            tugasnya = records

            if(listtugas[i]['submission']==0):
                #potential giving alert
                #percobaan = datetime.datetime(2020,12,15)
                thedeadline = tugasnya[0]['deadline']-datetime.datetime.now()
                waktu = time.strftime("%H jam : %M menit",time.gmtime(thedeadline.seconds))

                if(int(thedeadline.days)<0): #sudah melewati deadline
                    continue
                elif(int(thedeadline.days)<=3):
                    listdeadline.append(str(tugasnya[0]['nama'])+" Waktu tersisa, "+str(thedeadline.days)+"Hari"+str(waktu))
                    tugasbelumdikerjakan+=1

        if tugasbelumdikerjakan == 0:
            return None

    def masuk_kelas(self,KELAS):
        #update di database kelas
        myc = dbaseee.cursor()
        idmurid = str(self.USER.getID())
        namakelas = str(KELAS.getNama())
        memberkelas = str(KELAS.getMembers())
        if(memberkelas == "None"or memberkelas==""):
            memberkelas = idmurid
        else:
            memberkelas = memberkelas+","+idmurid
        query = 'update kelas set idmember="'+memberkelas+'" where namakelas = "'+namakelas+'"'
        myc.execute(query)

        #update di database user
        myc = dbaseee.cursor()
        ididkelas = str(self.getKelas())
        if(ididkelas == ""):
            ididkelas = str(KELAS.id)
        else:
            ididkelas = ididkelas+","+str(KELAS.id)
        query = 'update users set idkelas="'+ididkelas+'" where nama="'+self.USER.name+'"'
        myc.execute(query)

    def sign_class(self, namakelasnya, enrollkey):
        myc = dbaseee.cursor(dictionary=True)
        query = 'select * from kelas where namakelas ="' + namakelasnya + '"'
        myc.execute(query)
        records = myc.fetchall()

        print(records)
        if (records[0]['namakelas'] != namakelasnya):
            return False

        kelasnya = kelas(records[0])
        self.masuk_kelas(kelasnya)
        return True

    def getAlert(self):
        myc = dbaseee.cursor(dictionary=True)
        query = 'select pesan from alert where idmurid='+str(self.getID())
        myc.execute(query)
        records = myc.fetchall()
        return records

    def getNilai(self,tugasnya):
        #cari id tugas

        myc = dbaseee.cursor()
        query = 'select id from tugas where nama="'+str(tugasnya)+'"'
        myc.execute(query)
        records = myc.fetchall()
        idtugas = records[0][0]

        #cari nilai tugas
        myc = dbaseee.cursor()
        query = 'select nilai from nilai where idtugas='+str(idtugas)+' and idmurid='+str(self.getID())
        myc.execute(query)
        records = myc.fetchall()

        return records[0][0]
