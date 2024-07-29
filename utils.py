import psycopg2
from models import User

def con_db(fun):
    def wrap(*args, **kwargs):
        with psycopg2.connect("dbname=to_do_list user=postgres password = 0507209369kg host=localhost port=5432") as conn:
            cur = conn.cursor()
            answer = fun(cur, *args, **kwargs)
            conn.commit()
            cur.fetchall()
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
def add_tasks(cur, user):
    title = input('Title - ')
    description = input('Description - ')
    date = input('Date - ')
    cur.execute('insert into tasks (title, description, date_at, user_id) values (%s, %s, %s, %s)', (title, description,date, user.id))
@con_db
def delete_tasks(cur, user):
    id = input('tasks, id - ')
    cur.execute('select u.id from tasks as t join users as u on u.id = t.user_id where t.id = %s', (id))
    user_id = cur.fetchone()
    if user_id[0] == user.id:
        cur.execute('delete from tasks where id = %s and user_id = %s', (id,user.id))
        cur.execute('update users set faal_task = faal_task + 1 where id = %s', (user.id,))
        print('suggest operation')
    else:
        print('This task is not  your own')    

@con_db
def done_tasks(cur, user):
    id = input('tasks, id - ')
    cur.execute('select u.id from tasks as t join users as u on u.id = t.user_id where t.id = %s', (id) )
    user_id = cur.fetchone()
    if user_id[0] == user.id:
        cur.execute('delete from tasks where id = %s and user_id = %s', (id,user.id))
        cur.execute('update users set done_task = done_task + 1 where id = %s', (user.id,))
    else :
        print('Вы не можете удалять чужие задания')


@con_db
def all_tasks(cur,user):
    cur.execute('select * from tasks where user_id = %s',(user.id))
    all_tasks=cur.fetchall()
    for i in all_tasks:
        print(i)










