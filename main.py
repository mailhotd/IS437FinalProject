from flask import Flask
from flask import render_template
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response 
from user import userList
from event import eventList
from equipment import equipmentList
#from issuedEquipment import issuedEquipmentList
#from attendance import attendanceList
import pymysql,json,time
from flask_session import Session  

app = Flask(__name__,static_url_path='')

SESSION_TYPE = 'filesystem'
app.config.from_object(__name__)
Session(app)

@app.route('/set')
def set():
    session['time'] = time.time()
    return 'set'
    
@app.route('/get')
def get():
    return str(session['time'])
 
@app.route('/login',methods = ['GET','POST'])
def login():

    if request.form.get('UserEmail') is not None and request.form.get('UserPassword') is not None:
        u = userList()
        if u.tryLogin(request.form.get('UserEmail'),request.form.get('UserPassword')):
            print('login ok')
            session['user'] = u.data[0]
            session['active'] = time.time()
            
            return redirect('main')
        else:
            print('login failed')
            return render_template('login.html', title='Login', msg='Incorrect login.')
    else:
        if 'msg' not in session.keys() or session['msg'] is None:
            m = 'Type your Email and Password to continue.'
        else:
            m = session['msg']
            session['msg'] = None
        return render_template('login.html', title='Login', msg=m)
        
@app.route('/logout',methods = ['GET','POST'])
def logout():
    del session['user'] 
    del session['active'] 
    return render_template('login.html', title='Login', msg='Logged out.')

@app.route('/users')
def users():
    if checkSession() == False: 
        return redirect('login')
    u = userList()
    u.getAll()
    
    print(u.data)
    return render_template('users.html', title='User List',  users=u.data)
    
@app.route('/user')
def user():
    if checkSession() == False: 
        return redirect('login')
    u = userList()
    if request.args.get(u.pk) is None:
        return render_template('error.html', msg='No user id given.')  

    u.getById(request.args.get(u.pk))
    if len(u.data) <= 0:
        return render_template('error.html', msg='User not found.')  
    
    print(u.data)
    return render_template('user.html', title='User',  user=u.data[0])
    
@app.route('/newuser',methods = ['GET', 'POST'])
def newuser():
    if checkSession() == False: 
        return redirect('login')
    if request.form.get('UserFName') is None:
        u = userList()
        u.set('UserFName','')
        u.set('UserLName','')
        u.set('UserEmail','')
        u.set('UserPassword','')
        u.set('UserType','')
        u.add()
        return render_template('newuser.html', title='New user',  user=u.data[0]) 
    else:
        u = userList()
        u.set('UserFName',request.form.get('UserFName'))
        u.set('UserLName',request.form.get('UserLName'))
        u.set('UserEmail',request.form.get('UserEmail'))
        u.set('UserPassword',request.form.get('UserPassword'))
        u.set('UserType',request.form.get('UserType'))
        u.add()
        if u.verifyNew():
            u.insert()
            print(u.data)
            return render_template('saveduser.html', title='User Saved',  user=u.data[0])
        else:
            return render_template('newuser.html', title='User Not Saved',  user=u.data[0],msg=u.errorList)
            
@app.route('/saveuser',methods = ['GET', 'POST'])
def saveuser():
    if checkSession() == False: 
        return redirect('login')
    u = userList()
    u.set('UserID',request.form.get('UserID'))
    u.set('UserFName',request.form.get('UserFName'))
    u.set('UserLName',request.form.get('UserLName'))
    u.set('UserEmail',request.form.get('UserEmail'))
    u.set('UserPassword',request.form.get('UserPassword'))
    u.set('UserType',request.form.get('UserType'))
    u.add()
    if u.verifyChange():
        u.update()
        return render_template('saveduser.html', title='User Saved',  user=u.data[0])
    else:
        return render_template('user.html', title='User Not Saved',  user=u.data[0],msg=u.errorList)
 
@app.route('/deleteuser',methods = ['GET', 'POST'])
def deleteuser():
    if checkSession() == False: 
        return redirect('login')
    print("ID:",request.form.get('UserID')) 

    u = userList()
    u.deleteById(request.form.get('UserID'))
    return render_template('confirmaction.html', title='Cadet Deleted',  msg='Cadet Deleted!')
        
'''
================================================================
START EVENT PAGES:
================================================================
'''

@app.route('/events')
def events():
    if checkSession() == False: 
        return redirect('login')
    e = eventList()
    e.getAll()
    return render_template('event/events.html', title='Event List',  events=e.data)
    
@app.route('/event')
def event():
    if checkSession() == False: 
        return redirect('login')
    e = eventList()
    if request.args.get(e.pk) is None:
        return render_template('error.html', msg='No Event ID given.')  

    e.getById(request.args.get(e.pk))
    if len(e.data) <= 0:
        return render_template('error.html', msg='Event not found.')  
    
    print(e.data)
    return render_template('event/event.html', title='Event ',  event=e.data[0])  
    
@app.route('/newevent',methods = ['GET', 'POST'])
def newevent():
    if checkSession() == False: 
        return redirect('login')
    if request.form.get('EventName') is None:
        e = eventList()
        e.set('EventName','')
        e.set('EventStartDT','')
        e.set('EventEndDT','')
        e.set('EventStatus','')
        e.set('EventSemester','')
        e.add()
        return render_template('event/newevent.html', title='New Event',  event=e.data[0]) 
    else:
        e = eventList()
        e.set('EventName',request.form.get('EventName'))
        e.set('EventStartDT',request.form.get('EventStartDT'))
        e.set('EventEndDT',request.form.get('EventEndDT'))
        e.set('EventStatus',request.form.get('EventStatus'))
        e.set('EventSemester',request.form.get('EventSemester'))
        e.add()
        if e.verifyNew():
            e.insert()
            print(e.data)
            return render_template('event/savedevent.html', title='Event Saved',  event=e.data[0])
        else:
            return render_template('event/newevent.html', title='Event Not Saved',  event=e.data[0],msg=e.errorList)
            
@app.route('/saveevent',methods = ['GET', 'POST'])
def saveevent():
    if checkSession() == False: 
        return redirect('login')
    e = eventList()
    e.set('EventID',request.form.get('EventID'))
    e.set('EventName',request.form.get('EventName'))
    e.set('EventStartDT',request.form.get('EventStartDT'))
    e.set('EventEndDT',request.form.get('EventEndDT'))
    e.set('EventStatus',request.form.get('EventStatus'))
    e.set('EventSemester',request.form.get('EventSemester'))
    e.add()
    print(e.data)
    if e.verifyChange():
        e.update()
        return render_template('event/savedevent.html', title='Event Saved',  event=e.data[0])
    else:
        return render_template('event/event.html', title='Event Not Saved',  event=e.data[0],msg=e.errorList)

@app.route('/deleteevent',methods = ['GET', 'POST'])
def deleteevent():
    if checkSession() == False: 
        return redirect('login')
    print("ID:",request.form.get('EventID')) 

    e = eventList()
    e.deleteById(request.form.get('EventID'))
    return render_template('event/deletedevent.html', title='Event Deleted',  msg='Event Deleted!')
        
'''
================================================================
END EVENT PAGES
================================================================
'''

'''
================================================================
START EQUIPMENT PAGES:
================================================================
'''

@app.route('/equipments')
def equipments():
    if checkSession() == False: 
        return redirect('login')
    eq = equipmentList()
    eq.getAll()
    return render_template('equipment/equipments.html', title='Equipment List',  equipments=eq.data)
    
@app.route('/equipment')
def equipment():
    if checkSession() == False: 
        return redirect('login')
    eq = equipmentList()
    if request.args.get(eq.pk) is None:
        return render_template('error.html', msg='No Equipment ID given.')  

    eq.getById(request.args.get(eq.pk))
    if len(eq.data) <= 0:
        return render_template('error.html', msg='Equipment not found.')  
    
    print(eq.data)
    return render_template('equipment/equipment.html', title='Equipment ',  equipment=eq.data[0])

@app.route('/newequipment',methods = ['GET', 'POST'])
def newequipment():
    if checkSession() == False: 
        return redirect('login')
    eq = equipmentList()
    eq.getAll()
    if request.form.get('EquipmentName') is None:
        eq = equipmentList()
        eq.set('EquipmentName','')
        eq.set('NatoStockNumber','')
        eq.set('DateAcquired','')
        eq.set('DateRetired','')
        eq.add()
        return render_template('equipment/newequipment.html', title='New Equipment',  equipment=eq.data[0]) 
    else:
        eq = equipmentList()
        eq.set('EquipmentID',request.form.get('EquipmentID'))
        eq.set('EquipmentName',request.form.get('EquipmentName'))
        eq.set('NatoStockNumber',request.form.get('NatoStockNumber'))
        eq.set('DateAcquired',request.form.get('DateAcquired'))
        eq.set('DateRetired',request.form.get('DateRetired'))
        eq.add()
        if eq.verifyNew():
            eq.insert()
            print(eq.data)
            return render_template('equipment/savedequipment.html', title='Equipment Saved',  equipment=eq.data[0])
        else:
            return render_template('equipment/newequipment.html', title='Equipment Not Saved',  equipment=eq.data[0],msg=eq.errorList)

@app.route('/saveequipment',methods = ['GET', 'POST'])
def saveequipment():
    if checkSession() == False: 
        return redirect('login')
    eq = equipmentList()
    eq.set('EquipmentID',request.form.get('EquipmentID'))
    eq.set('EquipmentName',request.form.get('EquipmentName'))
    eq.set('NatoStockNumber',request.form.get('NatoStockNumber'))
    eq.set('DateAcquired',request.form.get('DateAcquired'))
    eq.set('DateRetired',request.form.get('DateRetired'))
    eq.add()
    if eq.verifyChange():
        eq.update()
        return render_template('equipment/savedequipment.html', title='Equipment Saved', equipment=eq.data[0])
    else:
        return render_template('equipment/equipment.html', title='Equipment Not Saved',  equipment=eq.data[0],msg=eq.errorList)
 
@app.route('/deleteequipment',methods = ['GET', 'POST'])
def deleteequipment():
    if checkSession() == False: 
        return redirect('login')
    print("ID:",request.form.get('EquipmentID')) 

    eq = equipmentList()
    eq.deleteById(request.form.get('EquipmentID'))
    return render_template('equipment/deletedequipment.html', title='Equipment Deleted',  msg='Equipment Deleted!')
   
'''
================================================================
END EQUIPMENT PAGES
================================================================
'''

'''
================================================================
START ISSUED EQUIPMENT PAGES:
================================================================
'''

'''
================================================================
END ISSUED EQUIPMENT PAGES:
================================================================
'''

'''
================================================================
START ATTENDANCE PAGES:
================================================================
'''

'''
================================================================
END ATTENDANCE PAGES:
================================================================
'''



@app.route('/main')
def main():
    if checkSession() == False: 
        return redirect('login')
    userinfo = 'Hello, ' + session['user']['UserFName']
    return render_template('main.html', title='Main menu',msg = userinfo)  

def checkSession():
    if 'active' in session.keys():
        timeSinceAct = time.time() - session['active']
        print(timeSinceAct)
        if timeSinceAct > 1440:
            session['msg'] = 'Your session has timed out.'
            return False
        else:
            session['active'] = time.time()
            return True
    else:
        return False
    
    
@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
   app.secret_key = '1234'
   app.run(host='127.0.0.1',debug=True)   
   
   