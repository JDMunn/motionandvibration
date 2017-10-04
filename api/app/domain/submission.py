import abc


class SubmissionObject(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __validate__(self):
        raise NotImplementedError('must define __validate__ to use this base class,' +
                                  ' methods should raise a ValueError if validation' +
                                  ' fails, otherwise return self')


    @abc.abstractmethod
    def __save__(self):
        raise NotImplementedError('must define __save__ to use this base class')


    @abc.abstractmethod
    def __notify__(self):
        raise NotImplementedError('must define __notify__ to use this base class')


class Entry(SubmissionObject):

    expected_fields = {
        'category',
        'focus',
        'title',
        'description',
        'name',
        'email',
        'type'
    }

    def __init__(self, data, repo):
        self.data = data
        self.repo = repo


    def __validate__(self):
        if (set(self.data.keys()) <= self.expected_fields):
            raise ValueError('Missing required fields: ' +
                             str(self.expected_fields -
                                 set(self.data.keys())))
        return self


    def __save__(self):
        self.repo.save(self.data)