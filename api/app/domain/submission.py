import abc


class SubmissionObject(object, metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def __validate__(self):
        raise NotImplementedError('must define __validate__ to use this base class,' +
                                  ' methods should raise a ValueError if validation' +
                                  ' fails, otherwise return self')


class Entry(SubmissionObject):

    expected_fields = {
        'category',
        'focus',
        'title',
        'description',
        'name',
        'email',
        'link'
    }

    def __init__(self, data):
        self.data = data

    def get_id(self):
        return (self.data['name'].replace(' ', '') + '_' +
                self.data['title'].replace(' ', ''))

    def get_notification(self):
        return ('New entry recieved!\n' +
                self.data['name'] + ' submitted a project titled: ' +
                self.data['title'] + '. The description reads: ' +
                self.data['description'] + '. The project is for ' +
                self.data['category'] + ', with a focus on ' +
                self.data['focus'] + '. Here is a link to their project: ' +
                self.data['link']
                )


    def __validate__(self):
        if len(self.expected_fields - set(self.data.keys())) > 0:
            raise ValueError('Missing required fields: ' +
                             str(self.expected_fields -
                                 set(self.data.keys())))
        return self

