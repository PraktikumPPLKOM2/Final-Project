from .user import user
from .murid import murid
from .guru import guru
from .ortu import ortu

import mysql.connector as eskuel
dbaseee = eskuel.connect(
        user="root",
        password="password_to_OP3N",
        host="localhost",
        database="prak_ppl",
        autocommit=True,
        auth_plugin='mysql_native_password'
    )


class loginsession:

    def __init__(self):

        self._nama = ""
        self._uname = ""
        self._notelp = ""
        self._alamat = ""
        self._email = ""
        self._password = ""

    def login(self, status, username, password):
        index = 0

        #SELECT BUAT LIST SEMUA UNAME TERGANTUNG DIA MURID/GURU/ORTU
        myc = dbaseee.cursor(dictionary=True)
        query = 'SELECT * FROM users where status like '+'"'+status+'"'
        myc.execute(query)
        records = myc.fetchall()
        dbaseee.commit()

        if len(records) == 0:
            return 'role'

        for i in range(len(records)):
            if (username == records[i]['username']):
                index = i
                break
            elif (i == len(records) - 1):
                return 'uname'

        userPass = records[index]["password"]
        if userPass != password:
            # LOGIN FAILED
            return 'pw'

        # LOGIN SUCCESS
        if status == 'Murid':
            return murid(user(records[index]))
        elif status == 'Guru':
            return guru(user(records[index]))
        else:
            return ortu(user(records[index]))


    def register(self, azn, nama, uname, notelp, alamat, email, password):
        self._nama = nama
        self._uname = uname
        self._notelp = notelp
        self._alamat = alamat
        self._email = email
        self._password = password

        # verification
        """
        ADD VERIFICATION IF EMAIL
        HAS BEEN USED OR NO
        """

        #SELECT BUAT SEMUA
        myc = dbaseee.cursor(dictionary=True)
        query = "SELECT * FROM users"
        myc.execute(query)
        records = myc.fetchall()
        dbaseee.commit()
        myc.close()

        listEmail = [records[i]['email'] for i in range (len(records))]
        if self._email in listEmail:
            return 'email exist'

        if "@" not in self._email:
            return 'email'

        if azn == 1:
            azn = "Murid"
        elif azn == 2:
            azn = "Guru"
        else:
            azn = "Orang Tua"

        return (
                azn,
                self._uname,
                self._password,
                self._nama,
                self._notelp,
                self._email,
                self._alamat
            )


    def forgotpassword(self, status, theuser, themail, newpassword):
        if (status == 1):
            status = "Murid"
        elif (status == 2):
            status = "Guru"
        else:
            status = "Ortu"

        #SELECT BUAT LIST SEMUA EMAIL
        myc = dbaseee.cursor(dictionary=True)
        query = "SELECT * FROM users"
        myc.execute(query)
        records = myc.fetchall()

        listEmail = [records[i]['email'] for i in range (len(records))]
        if (themail not in listEmail):
            return 'email'

        #QUERY CHANGE DATA PASSWORD
        query = "update users set password = %s where username = %s "
        value = (newpassword, theuser)
        myc.execute(query,value)
        dbaseee.commit()
        myc.close()

        return False
