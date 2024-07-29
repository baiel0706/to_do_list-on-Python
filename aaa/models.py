class User():
    def __init__(self, id,username, email,  done_task,falled_task,password) -> None:
        self.id = id
        self.username = username
        self.email = email
        self.done_task = done_task
        self.falled_task = falled_task
        self.password = password
    
    def str(self):
        return self.username