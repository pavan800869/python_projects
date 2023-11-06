class Attendance:
    def __init__(self, att) :
        self.att = att
    def __contains__(self, sub):
        if sub in self.att:
            return True
        else:
            return False
    def __getitem__(self):
        return self.att[sub]
    def __str__(self):
        return "Sequence contain subject & attendance "
a=Attendance({"PP":45,"JP":40,"DS":50,"CS-1":30})
print(str(a))
s=input("Enter subject name:")
if s in a:
    print("Your attendance in %s is %d"%(s,a.att[s]))
else:
    print("%s is not in sequence"%(s))                