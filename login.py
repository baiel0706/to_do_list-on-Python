import psycopg2
from models import User

def con_db(fun):
    def wrap(*args, **kwargs):
        with psycopg2.connect("dbname=to_do_list user=postgres password = 20072604sh host=localhost port=5432") as conn:
            cur = conn.cursor()
            answer = fun(cur, *args, **kwargs)
            conn.commit()
        return answer
    return wrap

@con_db
def register(cur):
    username = input('Username - ')
    email = input('Email - ')
    password = input('Password - ')
    password2 = input('Password2 - ')
    if password == password2:
        cur.execute('insert into users (username, email, password) values (%s,%s,%s)', (username, email, password))
    else:
        print('Passwords are not same')
        
@con_db
def login(cur):
    username = input('Username - ')
    password = input('Password - ')
    cur.execute('select * from users where username = %s and password = %s', (username,password))
    user = cur.fetchone()
    user = User(*user)
    return user
@con_db
def all_tasks(cur):
    u_id = input('users_id - ')
    cur.execute('select %s from users ',(u_id))