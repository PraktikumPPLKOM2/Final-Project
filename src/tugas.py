import datetime

class tugas:
    """CLASS TUGAS"""
    def __init__(self, nama, desc='', dl= None):
        self.nama = nama
        self.desc = desc
        if dl[4] == dl[7] == '/' and dl[13] == ':':
            self.deadline = dl #'yyyy-mm-dd hh:mm'
        elif dl == None:
            self.deadline = dl
        else:
            print('Tanggal tidak terdeteksi, deadline dianggap tidak ada.')
            self.deadline = None
        self.score = {}

    def getSisaWaktu(self):
        curt = datetime.datetime.now
        # tahun
        a = int(self.deadline[:4]) - curt.year
        if a > 0:
            print(a, 'Tahun', end=' ')
        # bulan
        a = int(self.deadline[5:7]) - curt.month
        if a > 0:
            print(a, 'Bulan', end=' ')
        # hari
        a = int(self.deadline[8:10]) - curt.day
        if a > 0:
            print(a, 'Hari', end=' ')
        # jam
        a = int(self.deadline[11:13]) - curt.hour
        if a > 0:
            print(a, 'Jam', end=' ')
        # menit
        a = int(self.deadline[14:]) - curt.minute
        if a > 0:
            print(a, 'Menit', end=' ')
        print()

    def printDataTugas(self):
        print("""
        Nama tugas : %s
        Deskripsi  : %s
        Deadline   : %s
        """%(self.nama,self.desc,self.deadline))

    def setSubmitStatus(self, murid):
        self.score[murid.getID()] = 0

    def getSubmitStatus(self, murid):
        return murid.getID() in self.score.keys()

    def setNilai(self, murid, nilai):
        if not self.getSubmitStatus(murid):
            print (murid.getName(), "belum mengumpulkan tugas!")
        self.score[murid.getID()] = nilai

    def getNilai(self, murid):
        try:
            return self.score[murid.getID()]
        except:
            print (murid.getName(), "belum mengumpulkan tugas!")