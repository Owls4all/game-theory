class matrix:
    def __init__(self,m11,m12,m13,m21,m22,m23,m31,m32,m33):
        self.m11 = m11; self.m12 = m12; self.m13 = m13
        self.m21 = m21; self.m22 = m22; self.m23 = m23
        self.m31 = m31; self.m32 = m32; self.m33 = m33
class vector:
    def __init__(self,coop,copy,cheat):
        self.coop = coop
        self.copy = copy
        self.cheat = cheat
    def multiplyMatrix(self,matrix:matrix):
        v1 = self.coop
        v2 = self.copy
        v3 = self.cheat

        coop = v1*matrix.m11 + v2*matrix.m12 + v3*matrix.m13
        copy = v1*matrix.m21 + v2*matrix.m22 + v3*matrix.m23
        cheat = v1*matrix.m31 + v2*matrix.m32 +v3*matrix.m33
        return vector(coop,copy,cheat)
    def print(self):
        str_self = f'''
 _  _
| {self.coop} |
| {self.copy} |
|_{self.cheat}_|
 
'''
        print(str_self)
players=vector(10,10,10)
players.print()

