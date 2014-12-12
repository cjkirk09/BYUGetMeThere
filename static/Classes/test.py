from DB import *
from Course import Course

if __name__ == "__main__":

    '''#getPath
    print "Tesing getPath..."
    assert DB.getPath("ASB", "TMCB") == {'buildingInfo': {'phone_number': '801-422-5816', 'hours': '', 'in_DB': True, 'id': 'TMCB', 'name': 'James E Talmage Building'}, 'endCoord': {'latitude': '40.249856', 'in_DB': True, 'building_id': 'TMCB', 'id': 66L, 'longitude': '-111.650697'}, 'floorPlans': ['/static/FloorPlans/TMCB/tmcb-bd.pdf', '/static/FloorPlans/TMCB/tmcb-1d.pdf', '/static/FloorPlans/TMCB/tmcb-2d.pdf', '/static/FloorPlans/TMCB/tmcb-3d.pdf'], 'startCoord': {'latitude': '40.250796', 'in_DB': True, 'building_id': 'ASB', 'id': 1L, 'longitude': '-111.649268'}}
    print "  Passed test 1"
    assert DB.getPath("TMCB", "JFSB") == {'buildingInfo': {'phone_number': '801-422-4265', 'hours': '', 'in_DB': True, 'id': 'JFSB', 'name': 'Joseph F Smith Building'}, 'endCoord': {'latitude': '40.248841', 'in_DB': True, 'building_id': 'JFSB', 'id': 30L, 'longitude': '-111.651694'}, 'floorPlans': ['/static/FloorPlans/JFSB/jfsb-bd.pdf', '/static/FloorPlans/JFSB/jfsb-1d.pdf', '/static/FloorPlans/JFSB/jfsb-2d.pdf', '/static/FloorPlans/JFSB/jfsb-3d.pdf', '/static/FloorPlans/JFSB/jfsb-4d.pdf'], 'startCoord': {'latitude': '40.249242', 'in_DB': True, 'building_id': 'TMCB', 'id': 64L, 'longitude': '-111.651499'}}
    print "  Passed test 2"
    assert DB.getPath("JFSB", "HBLL") == {'buildingInfo': {'phone_number': '801-422-4774', 'hours': '', 'in_DB': True, 'id': 'HBLL', 'name': 'Harold B Lee Library'}, 'endCoord': {'latitude': '40.249259', 'in_DB': True, 'building_id': 'HBLL', 'id': 13L, 'longitude': '-111.649482'}, 'floorPlans': ['/static/FloorPlans/HBLL/hbll-bnd.pdf', '/static/FloorPlans/HBLL/hbll-1d.pdf', '/static/FloorPlans/HBLL/hbll-1nd.pdf', '/static/FloorPlans/HBLL/hbll-2d.pdf', '/static/FloorPlans/HBLL/hbll-3d.pdf', '/static/FloorPlans/HBLL/hbll-3nd.pdf', '/static/FloorPlans/HBLL/hbll-4d.pdf', '/static/FloorPlans/HBLL/hbll-5d.pdf', '/static/FloorPlans/HBLL/hbll-6d.pdf', '/static/FloorPlans/HBLL/hbll-7d.pdf'], 'startCoord': {'latitude': '40.2487', 'in_DB': True, 'building_id': 'JFSB', 'id': 28L, 'longitude': '-111.65072'}}
    print "  Passed test 3"
    
    #getCustomPath
    print "Testing getCustomPath..."
    assert DB.getCustomPath(140.2, 136.5, "ESC") == {'buildingInfo': {'phone_number': '801-422-9276', 'hours': 'WD 6AM-11PM;WE 7AM-10PM', 'in_DB': True, 'id': 'ESC', 'name': 'Carl F Eyring Science Center'}, 'endCoord': {'latitude': '40.247099', 'in_DB': True, 'building_id': 'ESC', 'id': 9L, 'longitude': '-111.649862'}, 'floorPlans': ['/static/FloorPlans/ESC/esc-bd.pdf', '/static/FloorPlans/ESC/esc-1d.pdf', '/static/FloorPlans/ESC/esc-l1d.pdf', '/static/FloorPlans/ESC/esc-2d.pdf', '/static/FloorPlans/ESC/esc-l2d.pdf', '/static/FloorPlans/ESC/esc-3d.pdf', '/static/FloorPlans/ESC/esc-l3d.pdf', '/static/FloorPlans/ESC/esc-5d.pdf'], 'startCoord': {'latitude': 140.2, 'in_DB': False, 'building_id': '', 'id': 0, 'longitude': 136.5}}
    print "  Passed test 1"
    assert DB.getCustomPath(250, 290, "JKB") == {'buildingInfo': {'phone_number': '801-422-3006', 'hours': '', 'in_DB': True, 'id': 'JKB', 'name': 'Jesse Knight Building'}, 'endCoord': {'latitude': '40.250354', 'in_DB': True, 'building_id': 'JKB', 'id': 33L, 'longitude': '-111.650187'}, 'floorPlans': ['/static/FloorPlans/JKB/jkb-1d.pdf', '/static/FloorPlans/JKB/jkb-2d.pdf', '/static/FloorPlans/JKB/jkb-3d.pdf', '/static/FloorPlans/JKB/jkb-4d.pdf'], 'startCoord': {'latitude': 250, 'in_DB': False, 'building_id': '', 'id': 0, 'longitude': 290}}
    print "  Passed test 2"
    assert DB.getCustomPath(200.02, 300.41, "TMCB") == {'buildingInfo': {'phone_number': '801-422-5816', 'hours': '', 'in_DB': True, 'id': 'TMCB', 'name': 'James E Talmage Building'}, 'endCoord': {'latitude': '40.249335', 'in_DB': True, 'building_id': 'TMCB', 'id': 62L, 'longitude': '-111.650431'}, 'floorPlans': ['/static/FloorPlans/TMCB/tmcb-bd.pdf', '/static/FloorPlans/TMCB/tmcb-1d.pdf', '/static/FloorPlans/TMCB/tmcb-2d.pdf', '/static/FloorPlans/TMCB/tmcb-3d.pdf'], 'startCoord': {'latitude': 200.02, 'in_DB': False, 'building_id': '', 'id': 0, 'longitude': 300.41}}
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
    
    #getAllBuildings
    print "Testing getAllBuildings"
    assert DB.getAllBuildings() ==  [{'phone_number': '801-422-2741', 'hours': 'WD 6AM-7PM', 'in_DB': True, 'id': 'ASB', 'name': 'Abraham Smoot Building'}, {'phone_number': '801-422-5718', 'hours': 'WD 5:30AM-11PM', 'in_DB': True, 'id': 'BNSN', 'name': 'Ezra Taft Benson Building'}, {'phone_number': '801-422-3625', 'hours': 'WD 6AM-11PM;WE 8AM-6PM', 'in_DB': True, 'id': 'BRMB', 'name': 'George H Brimhall Building'}, {'phone_number': '801-422-4731', 'hours': 'WD 6AM-11PM;WE 6AM-11PM', 'in_DB': True, 'id': 'CB', 'name': 'W W Clyde Building'}, {'phone_number': '801-422-3673', 'hours': 'WD 6AM-11PM;WE 6AM-11PM', 'in_DB': True, 'id': 'CTB', 'name': 'Roland A Crabtree Building'}, {'phone_number': '801-422-3672', 'hours': '', 'in_DB': True, 'id': 'ELLB', 'name': 'Leo Ellsworth Building'}, {'phone_number': '801-422-9276', 'hours': 'WD 6AM-11PM;WE 7AM-10PM', 'in_DB': True, 'id': 'ESC', 'name': 'Carl F Eyring Science Center'}, {'phone_number': '801-422-5753', 'hours': '', 'in_DB': True, 'id': 'FB', 'name': 'Harvey L Fletcher Building'}, {'phone_number': '801-422-4774', 'hours': '', 'in_DB': True, 'id': 'HBLL', 'name': 'Harold B Lee Library'}, {'phone_number': '801-422-5546', 'hours': '', 'in_DB': True, 'id': 'HCEB', 'name': 'Caroline Hemenway Harman Building'}, {'phone_number': '801-422-3651', 'hours': 'WD 6AM-11PM;WE 6AM-6PM', 'in_DB': True, 'id': 'HFAC', 'name': 'Franklin S Harris Fine Arts Center'}, {'phone_number': '801-422-9138', 'hours': '', 'in_DB': True, 'id': 'HGB', 'name': 'Heber J Grant Building'}, {'phone_number': '801-422-5518', 'hours': '', 'in_DB': True, 'id': 'HRCB', 'name': 'Herald R Clark Building'}, {'phone_number': '801-422-3828', 'hours': '', 'in_DB': True, 'id': 'IPF', 'name': 'Indoor Practice Facility'}, {'phone_number': '801-422-4265', 'hours': '', 'in_DB': True, 'id': 'JFSB', 'name': 'Joseph F Smith Building'}, {'phone_number': '801-422-3006', 'hours': '', 'in_DB': True, 'id': 'JKB', 'name': 'Jesse Knight Building'}, {'phone_number': '801-422-2816', 'hours': 'WD 6AM-12AM', 'in_DB': True, 'id': 'JRCB', 'name': 'J Reuben Clark Building'}, {'phone_number': '801-422-2745', 'hours': '', 'in_DB': True, 'id': 'JSB', 'name': 'Joseph Smith Building'}, {'phone_number': '801-422-4880', 'hours': '', 'in_DB': True, 'id': 'LSB', 'name':'Life Sciences Building'}, {'phone_number': '801-422-5781', 'hours': 'WD 6AM-11PM', 'in_DB': True, 'id': 'MARB', 'name': 'Thomas L Martin Building'}, {'phone_number': '801-422-5448', 'hours': 'WD 7AM-11PM', 'in_DB': True, 'id': 'MCKB', 'name': 'David O McKay Building'}, {'phone_number': '801-422-9136', 'hours': '', 'in_DB': True, 'id': 'MSRB', 'name': 'Karl G Maeser Building'}, {'phone_number': '801-422-5718', 'hours': '', 'in_DB': True, 'id': 'NICB', 'name': 'Joseph K Nicholes Building'}, {'phone_number': '801-422-2899', 'hours': '', 'in_DB': True, 'id': 'RB', 'name': 'Stephen L Richards Building'}, {'phone_number': '801-422-2877', 'hours': '', 'in_DB': True, 'id': 'SFH', 'name': 'George Albert Smith Fieldhouse'}, {'phone_number': '801-422-2816', 'hours': '', 'in_DB': True, 'id': 'SNLB', 'name': 'William H Snell Building'}, {'phone_number': '801-422-7703', 'hours': 'WD 6AM-11PM;WE 6AM-11:30PM', 'in_DB': True, 'id': 'SWKT', 'name': 'Spencer W Kimball Tower'}, {'phone_number': '801-422-2877', 'hours': '', 'in_DB': True, 'id': 'TCB', 'name': 'Tennis Courts Building'}, {'phone_number': '801-422-5816', 'hours': '', 'in_DB': True, 'id': 'TMCB', 'name': 'James E Talmage Building'}, {'phone_number': '801-422-7053', 'hours': 'WD 6AM-11PM;WE 6AM-11:30PM', 'in_DB': True, 'id': 'TNRB', 'name': 'N Eldon Tanner Building'}, {'phone_number': '801-422-5672', 'hours': '', 'in_DB': True, 'id': 'WSC', 'name': 'Wilkinson Student Center'}]
    print "  Passed getting all buildings"'''
    
    #getSavedSchedules/saveSchedule
    '''print "Testing getSavedSchedules"
    SQL = "delete from BYU.SCHEDULES where USERNAME = 'test_user'"
    Query.execute(SQL)
    SQL = "delete from BYU.COURSES where NAME like 'test_course%'"
    Query.execute(SQL)
    assert DB.getSavedSchedules('test_user') == []
    print "  Passed with non-existant user"
    courses = [{"name":"test_course1","time": "12:00 PM", "days": "MW", "building_id": "TMCB", "room": "123"}, {"name":"test_course2","time": "3:00 PM", "days": "TTh", "building_id": "JSB", "room": "122"}]
    assert DB.saveSchedule('test_user', 'Monday', courses)
    print "  Passed saving schedule"
    assert DB.loadSchedule('test_user', 'Monday')['in_DB'] == True
    print "  Passed loading existing schedule"
    courses = [{"name":"test_course2","time": "11:00 AM", "days": "M", "building_id": "TMCB", "room": "123"}]
    assert DB.saveSchedule('test_user', 'Monday', courses)
    #assert DB.loadSchedule('test_user', 'another schedule')['in_DB'] == False
    #print "  Passed with unknown schedule"
    #assert DB.getSavedSchedules('test_user') != []
    #print "  Passed with saved schedule"
    SQL = "delete from BYU.SCHEDULES where USERNAME = 'test_user'"
    Query.execute(SQL)
    SQL = "delete from BYU.COURSES where NAME like 'test_course%'"
    Query.execute(SQL)
    '''
    
    SQL = "delete from BYU.SCHEDULES where USERNAME = 'test_user'"
    Query.execute(SQL)
    SQL = "delete from BYU.COURSES where NAME like 'test_course%'"
    Query.execute(SQL)
    courses = [{"name":"test_course1","time": "12:00 PM", "days": "MW", "building_id": "TMCB", "room": "123"}, {"name":"test_course2","time": "3:00 PM", "days": "TTh", "building_id": "JSB", "room": "122"}]
    DB.saveSchedule('test_user', 'Monday', courses)
    courses = [{"name":"test_course3","time": "11:00 AM", "days": "M", "building_id": "TMCB", "room": "123"}]
    DB.saveSchedule('test_user', 'Monday', courses)
    
    
    
    
    
    
    
    
