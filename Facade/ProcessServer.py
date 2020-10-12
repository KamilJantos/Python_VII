from Facade.FacadeClass import Server, State


class ProcessServer(Server):
    def __init__(self):
        self.name = 'ProcessServer'
        self.state = State.new

    def boot(self):
        print(f'booting the {self}')
        self.state = State.running

    def kill(self, restart=True):
        print(f'Killing {self}')
        self.state = State.restart if restart else State.zombie

    def create_process(self, user, name):
        print(f"trying to create the process '{name}' for user '{user}'")
