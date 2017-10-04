from os import path


class Repo():

    def __init__(self, folder):
        self.folder = folder

    def __save__(self, data, filename):
        with open(path.join(self.folder, filename), 'w') as file_object:
            file_object.write(data)
