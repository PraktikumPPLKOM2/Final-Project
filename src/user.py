class user:

    def __init__(self,dict):
        self.id = dict['id']
        self.uname = dict['username']
        self.pw = dict['password']
        self.name = dict['nama']
        self.noTelp = dict['notelp']
        self.email = dict['email']
        self.alamat = dict['alamat']
        self.idkelas = dict['idkelas']

    def getID(self):
        return self.id

    def getidkelas(self):
        return self.idkelas

    def getUname(self):
        return self.uname

    def getPw(self):
        return self.pw

    def getName(self):
        return self.name

    def getNoTelp(self):
        return self.noTelp

    def getEmail(self):
        return self.email

    def getAddress(self):
        return self.alamat
