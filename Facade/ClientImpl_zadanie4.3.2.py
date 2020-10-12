from Facade.OperatingSystem import OperatingSystem


class ClientImpl(OperatingSystem):

    def create_file(self, user, name):
        permissions = 'admin'
        return self.fs.create_file(user, name, permissions)


def main():
    os = ClientImpl()
    os.start()
    os.create_file('new_user', 'new_file')
    os.create_process('bar', 'ls /tmp')


if __name__ == '__main__':
    main()
