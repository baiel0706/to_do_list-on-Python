from utils import register, login, add_tasks,delete_tasks,done_tasks,all_tasks
class App():
    
    def __init__(self) -> None:
        self.run_app = True
        self.is_auth = False
    
    def run(self):
        while self.run_app:
            if self.is_auth:
                print('Add tasks - 1, Delete tasks - 2, Done tasks - 3,all_tasks -4')
                com = input('Input command - ')
                if com == '1':
                    add_tasks(self.user)
                elif com == '2':
                    delete_tasks(self.user)
                    print('You deleted tasks')
                elif com == '3':
                    done_tasks(self.user)
                    print('You done tasks')
                elif com == '4':
                    all.tasks(self.users)
            else:
                print('Register - 1, Login - 2, Exit - 3,')
                com = input('Input command - ')
                if com == '1':
                    register()
                    print('Вы зарегистрированы')
                    
                elif com == '2':
                    self.user = login()
                    self.is_auth = True
                elif com == '3':
                    self.run_app = False
                


if __name__ == '__main__':
    app = App()
    app.run()
        
    
    
