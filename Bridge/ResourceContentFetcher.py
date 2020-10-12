import abc


class ResourceContentFetcher(metaclass=abc.ABCMeta):
    """
 Define the interface (Implementor) for implementation classes
 that help fetch content.
 """


@abc.abstractmethod
def fetch(path):
    pass
