from .tugas import tugas

class kelas:
    """CLASS KELAS"""
    def __init__(self, dict):
        self.id = dict['id']
        self.nama = dict['namakelas']
        self.teachers = dict['idteacher']
        #self.teachers[guru.getName()] = guru
        self.members = dict['idmember']
        self.tugass = dict['idtugas']
        self.enrollment = dict['enrollmentkey']

    def getNama(self):
        return self.nama

    def addMember(self, murid, enr):
        if self.enrollment == None or enr == self.enrollment:
            self.members[murid.getName()] = murid
            murid.kelas = self
        else:
            print('Enrollment salah.')

    def getMembers(self):

        return self.members

    def addTeacher(self, guru):
        self.teachers[guru.getName()] = guru

    def getTeachers(self):
        return self.teachers


    def getTugas(self):
        return self.tugass
