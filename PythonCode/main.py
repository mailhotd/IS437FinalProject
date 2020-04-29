from flask import Flask
from flask import render_template
from flask import request,session, redirect, url_for, escape,send_from_directory,make_response 
from user import userList
from event import eventList
from equipment import equipmentList
import pymysql,json,time

from flask_session import Session  #serverside sessions

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
    '''
    -check login
    -set session
    -redirect to menu
    -check session on login pages
    '''
    print('-------------------------')
    if request.form.get('email') is not None and request.form.get('password') is not None:
        c = userList()
        if c.tryLogin(request.form.get('email'),request.form.get('password')):
            print('login ok')
            session['user'] = u.data[0]
            session['active'] = time.time()
            
            return redirect('main')
        else:
            print('login failed')
            return render_template('login.html', title='Login', msg='Incorrect login.')
    else:
        if 'msg' not in session.keys() or session['msg'] is None:
            m = 'Type your email and password to continue.'
        else:
            m = session['msg']
            session['msg'] = None
        return render_template('login.html', title='Login', msg=m)
        
@app.route('/logout',methods = ['GET','POST'])
def logout():
    del session['user'] 
    del session['active'] 
    return render_template('login.html', title='Login', msg='Logged out.')

@app.route('/basichttp')
def basichttp():
    if request.args.get('myvar') is not None:
        a = request.args.get('myvar')
        return 'your var:' + request.args.get('myvar')
    else:
        return 'myvar not set' 

@app.route('/index')
def index():
    user = {'username': 'Tyler'}
    
    
    items = [
        {'name':'Apple','price':2.34},
        {'name':'Orange','price':4.88},
        {'name':'Grape','price':2.44}
    ]
    return render_template('index.html', title='Home', user=user, items=items)
    
@app.route('/users')
def users():
    if checkSession() == False: 
        return redirect('login')
    c = userList()
    c.getAll()
    
    print(c.data)
    #return ''
    return render_template('users.html', title='user List',  users=u.data)
    
@app.route('/user')
def user():
    if checkSession() == False: 
        return redirect('login')
    c = userList()
    if request.args.get(c.pk) is None:
        return render_template('error.html', msg='No user id given.')  

    c.getById(request.args.get(c.pk))
    if len(c.data) <= 0:
        return render_template('error.html', msg='User not found.')  
    
    print(c.data)
    return render_template('user.html', title='user ',  user=u.data[0])
    
@app.route('/newuser',methods = ['GET', 'POST'])
def newuser():
    if checkSession() == False: 
        return redirect('login')
    if request.form.get('fname') is None:
        c = userList()
        c.set('fname','')
        c.set('lname','')
        c.set('email','')
        c.set('password','')
        c.set('type','')
        c.add()
        return render_template('newuser.html', title='New user',  user=u.data[0]) 
    else:
        c = userList()
        c.set('fname',request.form.get('fname'))
        c.set('lname',request.form.get('lname'))
        c.set('email',request.form.get('email'))
        c.set('password',request.form.get('password'))
        c.set('type',request.form.get('type'))
        c.add()
        if c.verifyNew():
            c.insert()
            print(c.data)
            return render_template('saveduser.html', title='User Saved',  user=u.data[0])
        else:
            return render_template('newuser.html', title='user Not Saved',  user=u.data[0],msg=u.errorList)
            
@app.route('/saveuser',methods = ['GET', 'POST'])
def saveuser():
    if checkSession() == False: 
        return redirect('login')
    c = userList()
    c.set('id',request.form.get('id'))
    c.set('fname',request.form.get('fname'))
    c.set('lname',request.form.get('lname'))
    c.set('email',request.form.get('email'))
    c.set('password',request.form.get('password'))
    c.set('type',request.form.get('type'))
    c.add()
    if c.verifyChange():
        c.update()
        #print(c.data)
        #return ''
        return render_template('saveduser.html', title='user Saved',  user=c.data[0])
    else:
        return render_template('user.html', title='user Not Saved',  user=c.data[0],msg=c.errorList)
        
'''
================================================================
START EVENT PAGES:
=================================================================
'''

@app.route('/events')
def events():
    if checkSession() == False: 
        return redirect('login')
    e = eventList()
    e.getAll()
    
    #print(e.data)
    #return ''
    return render_template('event/events.html', title='Event List',  events=e.data)
    
@app.route('/event')
def event():
    if checkSession() == False: 
        return redirect('login')
    e = eventList()
    if request.args.get(e.pk) is None:
        return render_template('error.html', msg='No event id given.')  

    e.getById(request.args.get(e.pk))
    if len(e.data) <= 0:
        return render_template('error.html', msg='Event not found.')  
    
    print(e.data)
    return render_template('event/event.html', title='Event ',  event=e.data[0])  
@app.route('/newevent',methods = ['GET', 'POST'])
def newevent():
    if checkSession() == False: 
        return redirect('login')
    if request.form.get('name') is None:
        e = eventList()
        e.set('name','')
        e.set('start','')
        e.set('end','')
        e.add()
        return render_template('event/newevent.html', title='New Event',  event=e.data[0]) 
    else:
        e = eventList()
        e.set('name',request.form.get('name'))
        e.set('start',request.form.get('start'))
        e.set('end',request.form.get('end'))
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
    e.set('eid',request.form.get('eid'))
    e.set('name',request.form.get('name'))
    e.set('start',request.form.get('start'))
    e.set('end',request.form.get('end'))
    e.add()
    if e.verifyChange():
        e.update()
        #print(e.data)
        #return ''
        return render_template('event/savedevent.html', title='Event Saved',  event=e.data[0])
    else:
        return render_template('event/event.html', title='Event Not Saved',  event=e.data[0],msg=e.errorList)
        
'''
================================================================
END EVENT PAGES
=================================================================
'''
'''
================================================================
START EQUIPMENT PAGES:
=================================================================
'''

@app.route('/newequipment',methods = ['GET', 'POST'])
def newequipment():
    if checkSession() == False: 
        return redirect('login')
    allEvents = eventList()
    allEvents.getAll()
    if request.form.get('equipment') is None:
        r = equipmentList()
        r.set('event_id','')
        r.set('user_id','')
        r.set('equipment','')
        r.add()
        return render_template('equipment/newequipment.html', title='New equipment',  equipment=r.data[0],el=allEvents.data) 
    else:
        r = equipmentList()
        r.set('event_id',request.form.get('event_id'))
        r.set('user_id',session['user']['id'])
        r.set('equipment',request.form.get('equipment'))
        r.add()
        if r.verifyNew():
            r.insert()
            print(r.data)
            return render_template('equipment/savedequipment.html', title='Equipment Saved',  equipment=r.data[0])
        else:
            return render_template('equipment/newequipment.html', title='Equipment Not Saved',  equipment=r.data[0],msg=r.errorList,el=allEvents.data)
@app.route('/saveequipment',methods = ['GET', 'POST'])

def saveequipment():
    if checkSession() == False: 
        return redirect('login')
    r = equipmentList()
    r.set('aid',request.form.get('aid'))
    r.set('event_id',request.form.get('event_id'))
    r.set('user_id',request.form.get('user_id'))
    r.set('equipment',request.form.get('equipment'))
    r.add()
    r.update()
    #print(e.data)
    #return ''
    return render_template('equipment/savedequipment.html', title='equipment Saved',  equipment=r.data[0])

@app.route('/myequipments')
def myequipments():
    if checkSession() == False: 
        return redirect('login')
    r = equipmentList()
    r.getByuser(session['user']['id'])
    #print(r.data)
    #return ''
    return render_template('myequipments.html', title='My equipments',  equipments=r.data)
   
'''
================================================================
END EQUIPMENT PAGES
=================================================================
'''

@app.route('/main')
def main():
    if checkSession() == False: 
        return redirect('login')
    userinfo = 'Hello, ' + session['user']['fname']
    return render_template('main.html', title='Main menu',msg = userinfo)  

def checkSession():
    if 'active' in session.keys():
        timeSinceAct = time.time() - session['active']
        print(timeSinceAct)
        if timeSinceAct > 1000:
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
   
   
   
   