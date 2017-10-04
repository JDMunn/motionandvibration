import abc


class RepoObject(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __save__(self, data, id):
        raise NotImplementedError('must define __save__ to use this base class')

