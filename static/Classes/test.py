from DB import *

if __name__ == "__main__":

    #getPath
    print DB.getPath("ASB", "TMCB")
    print DB.getPath("TMCB", "JFSB")
    print DB.getPath("JFSB", "HBLL")
    
    #getCustomPath
    print DB.getCustomPath(140.2, 136.5, "ESC")
    print DB.getCustomPath(250, 290, "JKB")    
    print DB.getCustomPath(200.02, 300.41, "TMCB")
    
    #verifyUser/createUser
    SQL = "delete from BYU.USERS where username = 'test_user'"
    Query.execute(SQL)
    assert DB.verifyUser('test_user','test_password') == False
    print "Passed with non-existant user"
    assert DB.createUser('test_user','test_password')
    print "Passed adding a user"
    assert DB.verifyUser('test_user','test_password')
    print "Passed with existant user"
    assert DB.createUser('test_user', 'another_password') == False
    print "Passed with duplicate user"
    SQL = "delete from BYU.USERS where username = 'test_user'"
    Query.execute(SQL)
    
    
