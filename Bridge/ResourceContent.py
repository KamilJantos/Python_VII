from Bridge.LocalFileFetcher import LocalFileFetcher
from Bridge.URLFetcher import URLFetcher


class ResourceContent:
    """
    Define the abstraction's interface.
    Maintain a reference to an object which represents the Implementor.
    """

    def __init__(self, imp):
        self._imp = imp

    def show_content(self, path): #Obsługa braku pliku
        try:
            self._imp.fetch(path)
        except FileNotFoundError as e:
            print("Nie znaleziono pliku: "+e.filename)


def main():
    url_fetcher = URLFetcher()
    iface = ResourceContent(url_fetcher)
    iface.show_content('http://python.org')
    print('===================')
    localfs_fetcher = LocalFileFetcher()
    iface = ResourceContent(localfs_fetcher)
    iface.show_content('file1.txt')


if __name__ == "__main__":
    main()
