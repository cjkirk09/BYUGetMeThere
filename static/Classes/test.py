from DB import *

if __name__ == "__main__":
    print DB.getPath("ASB", "TMCB")
    
    print DB.getCustomPath(200.02, 300.41, "TMCB")
    
    print DB.verifyLogin('romrell4','password')
    
    user = User()
    user.username = 'test_user'
    user.password = 'test_password'
    user.save()
    
    print DB.verifyLogin('test_user','test_password')
    
    SQL = "delete from BYU.USERS where username = 'test_user'"
    Query.execute(SQL)
