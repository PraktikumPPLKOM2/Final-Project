from .kelas import kelas
from .tugas import tugas

import mysql.connector as eskuel
dbaseee = eskuel.connect(
        user="root",
        password="password_to_OP3N",
        host="localhost",
        database="prak_ppl",
        autocommit=True,
        auth_plugin='mysql_native_password'
    )

class guru:

    def __init__(self, USER):
        self.USER = USER

    def getName(self):
        return self.USER.getName()

    def getUname(self):
        return self.USER.getUname()

    def getID(self):
        return self.USER.getID()

    def getMurid(self, KLS):
        return self.kelas[KLS]

    def getUserData(self):
        return self.USER.getUserData()

    """
    GURU memberi tugas ke suatu kelas
    semua murid dalam kelas itu mendapat
    tugas yang sama
    """

    def getTugas(self):
        pass

    def getKelas(self):
        myc = dbaseee.cursor(dictionary=True)
        query = 'select * from kelas where idteacher = "'+str(self.getID())+'"'
        myc.execute(query)
        records = myc.fetchall()
        for i in range(len(records)):
            #convert idtugas dan idmember menjadi data
            tugastugas = records[i]['idtugas']
            print(tugastugas)
            if tugastugas == '' or tugastugas == None:
                tugastugas = []
            else:
                tugastugas= tugastugas.split(",")
            print('sampe sini')

            muridmurid = records[i]['idmember']
            if muridmurid == '' or muridmurid == None:
                muridmurid = []
            else:
                muridmurid = muridmurid.split(",")
            listtugas=[]
            listmurid = []
            j=0
            z=0

            while(j<len(tugastugas)):
                if(tugastugas[j]==''):
                    break
                #untuk tugas
                myc = dbaseee.cursor(dictionary=True)
                query = 'select * from tugas where id='+str(tugastugas[j])
                myc.execute(query)
                therecords = myc.fetchall()
                listtugas.append(therecords)
                j+=1
            print('while tugas')
            while(z<len(muridmurid)):
                if (muridmurid[z] == ''):
                    break
                #untuk murid
                myc = dbaseee.cursor(dictionary=True)
                query = 'select * from users where id=' + str(muridmurid[z])
                myc.execute(query)
                therecords = myc.fetchall()
                listmurid.append(therecords)
                z+=1
            print('while murid')

            records[i]['listtugas'] = listtugas
            records[i]['listmurid'] = listmurid
        return records

    def giveTugas(self, namakelas, namatugas, desctugas, dl):
        myc = dbaseee.cursor(dictionary=True)
        query = 'select * from kelas where namakelas="' + namakelas + '"'
        myc.execute(query)
        records = myc.fetchall()
        if (len(records) == 0):
            return False
        KELAS = kelas(records[0])
        tugass = tugas(namatugas, desctugas, dl)
        try:
            idkelas= str(KELAS.id)
        except:
            print ("Error")
        #masukkan tugas ke dbase kelas dan tugas
        myc = dbaseee.cursor()
        query = 'insert into tugas (nama, deskripsi, idkelas, deadline) values(%s,%s,%s,%s)'
        value = (tugass.nama, tugass.desc, idkelas, tugass.deadline)
        myc.execute(query,value)

        listidtugas = str(KELAS.getTugas())
        myc = dbaseee.cursor()
        query = 'select id from tugas where nama="'+tugass.nama+'" and idkelas='+idkelas
        myc.execute(query)
        records = myc.fetchall()

        idtugas = str(records[0][0])
        if(listidtugas == "" or listidtugas == "None"):
            listidtugas =idtugas
        else:
            listidtugas = listidtugas +',' +idtugas
        myc = dbaseee.cursor()
        query = 'update kelas set idtugas ="'+listidtugas+'" where namakelas ="'+KELAS.nama+'"'
        myc.execute(query)

        #ke database penilaian
        myc = dbaseee.cursor()
        query = 'select idmember from kelas where namakelas ="'+KELAS.nama+'"'
        myc.execute(query)
        records = myc.fetchall()
        listmurid = str(records[0][0])
        listmurid = listmurid.split(",")
        print(listmurid)
        #masukkan ke database nilai untuk tiap murid
        if(len(listmurid)!=0):
            for i in range (len(listmurid)):
                myc = dbaseee.cursor()
                query = 'insert into nilai(idmurid, idtugas, submission, file) values ('+str(listmurid[i])+','+idtugas+',false,'+'"No File"'+')'
                print(query)
                myc.execute(query)

    def makeKelas(self, nama, enrPresent, enr):

        myc = dbaseee.cursor(dictionary=True)

        if enrPresent == 1:
            query = 'insert into kelas (namakelas, enrollmentkey, idteacher) values (%s,%s,%s)'
            val = (nama,enr,self.getID()) #
            myc.execute(query,val)
            dbaseee.commit()

        else:
            query = 'insert into kelas (namakelas, idteacher) values (%s,%s)'
            val = (nama,self.getID())
            myc.execute(query,val)
            dbaseee.commit()

    def nilaiTugas(self, namakelas, nilai, namamurid):
        try:
            myc = dbaseee.cursor(dictionary=True)
            query = 'select * from kelas where namakelas = "' + namakelas + '"'
            myc.execute(query)
            records = myc.fetchall()
            if listmember == "" or listmember==None:
                listmember = []
            else:
                listmember = records[0]['idmember']
                listmember = listmember.split(",")
            for i in range(len(listmember)):
                listmember[i] = int(listmember[i])
        except:
            print("Nama kelas tidak terdaftar")
        myc = dbaseee.cursor()
        query = "select id from users where nama='{}'".format(namamurid)
        myc.execute(query)
        idmurid = myc.fetchall()

        query = "select idtugas from nilai where idmurid='{}'".format(idmurid)
        myc.execute(query)
        idtugas = myc.fetchall()

        if nilai == "":
            print("Pemberian nilai batal!")
            return False
        nilai = int(nilai)
        if nilai > 100:
            print("Pemberian nilai batal! Nilai tidak boleh lebih dari 100")
            return False
        elif nilai < 0:
            print("Pemberian nilai batal! Nilai tidak boleh negatif")
            return False
        else:
            query = "UPDATE nilai set nilai='{}' where idmurid='{}' and idtugas='{}'".format(nilai, idmurid, idtugas)
            myc.execute(query)
            

    def cekhasilpekerjaan(self,tugasnya,kelasnya):
        namatugas = tugasnya
        namakelas = kelasnya

        #cari id kelasnya
        myc = dbaseee.cursor()
        query = 'select id from kelas where namakelas="'+namakelas+'"'
        myc.execute(query)
        records = myc.fetchall()
        idkelas = str(records[0][0])
        #mencari idtugasnya
        myc = dbaseee.cursor()
        query = 'select id from tugas where nama="'+namatugas+'" and idkelas='+idkelas
        myc.execute(query)
        records = myc.fetchall()
        idtugas = str(records[0][0])
        #mendapatkan hasil dari semua anak yang diamanahi tugas tersebut
        myc = dbaseee.cursor(dictionary= True)
        query = 'select * from nilai where idtugas='+idtugas
        myc.execute(query)
        records = myc.fetchall()
        tugasnya = records

        la =[]

        for i in range(len(records)):
            dictt = {}
            # cari nama murid dari id yang ada
            myc = dbaseee.cursor()
            query = 'select nama from users where id='+str(tugasnya[i]['idmurid'])
            myc.execute(query)
            records = myc.fetchall()
            namamurid = str(records[0][0])
            if(tugasnya[i]['submission']==1):
                dictt['namamurid'] = namamurid
                dictt['submission'] = "Sudah Mengumpulkan"
                dictt['file'] = tugasnya[i]['file']
            else:
                dictt['namamurid'] = namamurid
                dictt['submission'] = "Belum Mengumpulkan"
                dictt['file'] = 'Tidak Ada'
            la.append(dictt)

        return la
