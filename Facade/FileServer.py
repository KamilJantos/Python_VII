from Facade.FacadeClass import State, Server


class FileServer(Server):
    def __init__(self):
        self.name = 'FileServer'
        self.state = State.new

    def boot(self):
        print(f'booting the {self}')
        self.state = State.running

    def kill(self, restart=True):
        print(f'Killing {self}')
        self.state = State.restart if restart else State.zombie

    def create_file(self, user, name, permissions):
        print(f"trying to create the file '{name}' for user '{user}' "
              f"with permissions {permissions}")
