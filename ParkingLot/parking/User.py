import json
from parking import DBoprate


class User:
    __name = ""
    __password = ""
    __tel = ""
    __email = ""

    def GetName(self):
       return self.__name

    def GetPswd(self):
       return self.__password

    def GetTel(self):
        return self.__tel

    def GetEmail(self):
        return self.__email

    def SetName(self,name):
        self.__name = name

    def SetPswd(self,password):
        self.__password = password

    def SetTel(self,tel):
        self.__tel = tel

    def SetEmail(self,email):
        self.__email = email

    def Register(self,data):
        TBName = "parking_info.user_info"
        exp1 = "username,password"
        exp2 = "where username = " + "'" + data['name'] + "'"
        rows = DBoprate.DBSelect(TBName, exp1, exp2)
        if len(rows) > 0:
            return 0

        self.SetName(data['name'])
        self.SetPswd(data['password'])
        self.SetTel(data['tel'])
        self.SetEmail(data['email'])

        val = "(" + "'" + self.GetName() + "'" + "," + "'" + self.GetPswd() + "'" + "," + "'" + self.GetTel() + "'" + "," + "'" + self.GetEmail() + "'" + ")"
        TBName = "parking_info.user_info"
        DBoprate.DBInsert(TBName, val)
        return 1

    def Login(self,data):
        TBName = "parking_info.user_info"
        exp1 = "username,password"
        exp2 = "where username = " + "'" + data['name'] + "'"
        rows = DBoprate.DBSelect(TBName, exp1, exp2)
        password = rows[0][1]
        if password == data['password']:
            print("login successed")
            return 1
        else:
            print(data['password'])
            print("login failed")
            return 0

    def Reset(self,jsobj):
        data = json.loads(jsobj)

        self.SetName(data['name'])
        self.SetPswd(data['password'])
        self.SetTel(data['tel'])
        self.SetEmail(data['email'])

        val = "(" + self.GetName() + "," + self.GetPswd() + "," + self.GetTel() + "," + self.GetEmail() + ")"
        TBName = "parking_info.user_info"
        DBoprate.DBInsert(TBName, val)

# data = {'name': 'zhangsan', 'password': '12345'}
# user = User()
# print(User.Login(user,data))



