from .loginsession import loginsession

from sys import exit
from datetime import date,timedelta

import mysql.connector as eskuel
dbaseee = eskuel.connect(
        user="root",
        password="password_to_OP3N",
        host="localhost",
        database="prak_ppl",
        autocommit=True,
        auth_plugin='mysql_native_password'
    )
myc = dbaseee.cursor(dictionary=True)


"""LOGIN SESSION"""
newuser = loginsession()


def login(role, uname, pw):
    if role == 1:
        role = 'Murid'
    elif role == 2:
        role = 'Guru'
    else:
        role = 'Orang Tua'

    record = newuser.login(role, uname, pw)
    return record


def regist(role, nama, uname, pw, phone, addr, mail):
    #QUERY BUAT INSERT DATA
    i = newuser.register(role, nama, uname, phone, addr, mail, pw)
    if type(i) == str:
        return i

    sql = "INSERT INTO users (status,username,password,nama,notelp,email,alamat) Values(%s,%s,%s, %s,%s,%s,%s)"
    myc.execute(sql,i)
    dbaseee.commit()
    return False


def forgot(role, uname, mail, pw):
    done = newuser.forgotpassword(role, uname, mail, pw)

    if not done:
        return done

    return False
