from DB import *
from Course import Course

if __name__ == "__main__":

    #getPath
    print "Tesing getPath..."
    assert DB.getPath("ASB", "TMCB") == {'buildingInfo': {'phone_number': '801-422-5816', 'hours': '', 'in_DB': True, 'id': 'TMCB', 'name': 'James E Talmage Building'}, 'endCoord': {'latitude': '40.24917', 'in_DB': True, 'building_id': 'TMCB', 'id': 63L, 'longitude': '-111.65064'}, 'floorPlans': ['/static/FloorPlans/TMCB/tmcb-bd.pdf', '/static/FloorPlans/TMCB/tmcb-1d.pdf', '/static/FloorPlans/TMCB/tmcb-2d.pdf', '/static/FloorPlans/TMCB/tmcb-3d.pdf'], 'startCoord': {'latitude': '40.250796', 'in_DB': True, 'building_id': 'ASB', 'id': 1L, 'longitude': '-111.649268'}} 
    print "  Passed test 1"
    assert DB.getPath("TMCB", "JFSB") == {'buildingInfo': {'phone_number': '801-422-4265', 'hours': '', 'in_DB': True, 'id': 'JFSB', 'name': 'Joseph F Smith Building'}, 'endCoord': {'latitude': '40.248041', 'in_DB': True, 'building_id': 'JFSB', 'id': 29L, 'longitude': '-111.651718'}, 'floorPlans': ['/static/FloorPlans/JFSB/jfsb-bd.pdf', '/static/FloorPlans/JFSB/jfsb-1d.pdf', '/static/FloorPlans/JFSB/jfsb-2d.pdf', '/static/FloorPlans/JFSB/jfsb-3d.pdf', '/static/FloorPlans/JFSB/jfsb-4d.pdf'], 'startCoord': {'latitude': '40.249335', 'in_DB': True, 'building_id': 'TMCB', 'id': 62L, 'longitude': '-111.650431'}}
    print "  Passed test 2"
    assert DB.getPath("JFSB", "HBLL") == {'buildingInfo': {'phone_number': '801-422-4774', 'hours': '', 'in_DB': True, 'id': 'HBLL', 'name': 'Harold B Lee Library'}, 'endCoord': {'latitude': '40.249232', 'in_DB': True, 'building_id': 'HBLL', 'id': 14L, 'longitude': '-111.64909'}, 'floorPlans': ['/static/FloorPlans/HBLL/hbll-bnd.pdf', '/static/FloorPlans/HBLL/hbll-1d.pdf', '/static/FloorPlans/HBLL/hbll-1nd.pdf', '/static/FloorPlans/HBLL/hbll-2d.pdf', '/static/FloorPlans/HBLL/hbll-3d.pdf', '/static/FloorPlans/HBLL/hbll-3nd.pdf', '/static/FloorPlans/HBLL/hbll-4d.pdf', '/static/FloorPlans/HBLL/hbll-5d.pdf', '/static/FloorPlans/HBLL/hbll-6d.pdf', '/static/FloorPlans/HBLL/hbll-7d.pdf'], 'startCoord': {'latitude': '40.248153', 'in_DB': True, 'building_id': 'JFSB', 'id': 27L, 'longitude': '-111.65068'}}
    print "  Passed test 3"
    
    #getCustomPath
    print "Testing getCustomPath..."
    assert DB.getCustomPath(140.2, 136.5, "ESC") == {'buildingInfo': {'phone_number': '801-422-9276', 'hours': 'WD 6AM-11PM;WE 7AM-10PM', 'in_DB': True, 'id': 'ESC', 'name': 'Carl F Eyring Science Center'}, 'endCoord': {'latitude': '40.24751', 'in_DB': True, 'building_id': 'ESC', 'id': 8L, 'longitude': '-111.650149'}, 'floorPlans': ['/static/FloorPlans/ESC/esc-bd.pdf', '/static/FloorPlans/ESC/esc-1d.pdf', '/static/FloorPlans/ESC/esc-l1d.pdf', '/static/FloorPlans/ESC/esc-2d.pdf', '/static/FloorPlans/ESC/esc-l2d.pdf', '/static/FloorPlans/ESC/esc-3d.pdf', '/static/FloorPlans/ESC/esc-l3d.pdf', '/static/FloorPlans/ESC/esc-5d.pdf'], 'startCoord': {'latitude': 140.2, 'in_DB': False, 'building_id': '', 'id': '', 'longitude': 136.5}}
    print "  Passed test 1"
    assert DB.getCustomPath(250, 290, "JKB") == {'buildingInfo': {'phone_number': '801-422-3006', 'hours': '', 'in_DB': True, 'id': 'JKB', 'name': 'Jesse Knight Building'}, 'endCoord': {'latitude': '40.250354', 'in_DB': True, 'building_id': 'JKB', 'id': 33L, 'longitude': '-111.650187'}, 'floorPlans': ['/static/FloorPlans/JKB/jkb-1d.pdf', '/static/FloorPlans/JKB/jkb-2d.pdf', '/static/FloorPlans/JKB/jkb-3d.pdf', '/static/FloorPlans/JKB/jkb-4d.pdf'], 'startCoord': {'latitude': 250, 'in_DB': False, 'building_id': '', 'id': '', 'longitude': 290}}
    print "  Passed test 2"
    assert DB.getCustomPath(200.02, 300.41, "TMCB") == {'buildingInfo': {'phone_number': '801-422-5816', 'hours': '', 'in_DB': True, 'id': 'TMCB', 'name': 'James E Talmage Building'}, 'endCoord': {'latitude': '40.249856', 'in_DB': True, 'building_id': 'TMCB', 'id': 66L, 'longitude': '-111.650697'}, 'floorPlans': ['/static/FloorPlans/TMCB/tmcb-bd.pdf', '/static/FloorPlans/TMCB/tmcb-1d.pdf', '/static/FloorPlans/TMCB/tmcb-2d.pdf', '/static/FloorPlans/TMCB/tmcb-3d.pdf'], 'startCoord': {'latitude': 200.02, 'in_DB': False, 'building_id': '', 'id': '', 'longitude': 300.41}}
    print "  Passed test 3"
    
    #verifyUser/createUser
    print "Testing verifyUser and createUser"
    SQL = "delete from BYU.USERS where USERNAME = 'test_user'"
    Query.execute(SQL)
    assert DB.verifyUser('test_user','test_password') == False
    print "  Passed with non-existant user"
    assert DB.createUser('test_user','test_password')
    print "  Passed adding a user"
    assert DB.verifyUser('test_user','test_password')
    print "  Passed with existant user"
    assert DB.createUser('test_user', 'another_password') == False
    print "  Passed with duplicate user"
    SQL = "delete from BYU.USERS where username = 'test_user'"
    Query.execute(SQL)
    
    #getBuildingInfo
    print "Testing getBuidingInfo"
    assert DB.getBuildingInfo("ASB") == {'phone_number': '801-422-2741', 'hours': 'WD 6AM-7PM', 'in_DB': True, 'id': 'ASB', 'name': 'Abraham Smoot Building'}
    print "  Passed test 1"
    assert DB.getBuildingInfo("NICB") == {'phone_number': '801-422-5718', 'hours': '', 'in_DB': True, 'id': 'NICB', 'name': 'Joseph K Nicholes Building'}
    print "  Passed test 2"
    assert DB.getBuildingInfo("BLAH!")['in_DB'] == False
    print "  Passed test 3"
    
    #getSavedSchedules/saveSchedule
    print "Testing getSavedSchedules"
    SQL = "delete from BYU.SCHEDULES where USERNAME = 'test_user'"
    Query.execute(SQL)
    SQL = "delete from BYU.COURSES where NAME = 'test_class'"
    Query.execute(SQL)
    assert DB.getSavedSchedules('test_user') == []
    print "  Passed with non-existant user"
    course1 = Course()
    course1.loadFromAll('test_class', '1', '8:00 AM', 'MWF', 'JFSB', 'B102')
    course2 = Course()
    course2.loadFromAll('test_class', '2', '9:00 AM', 'MWF', 'TMCB', '111')
    assert DB.saveSchedule('test_user', 'test_schedule', [course1, course2])
    print "  Passed saving schedule"
    print DB.loadSchedule('test_user', 'another_schedule')
    assert DB.getSavedSchedules('test_user') != []
    print "  Passed with existant schedule"
    print DB.loadSchedule('test_user', 'test_schedule')
    SQL = "delete from BYU.SCHEDULES where USERNAME = 'test_user'"
    Query.execute(SQL)
    SQL = "delete from BYU.COURSES where NAME = 'test_class'"
    Query.execute(SQL)
    
    
    
    
    
    
    
    
