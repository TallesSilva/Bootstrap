from imports import *

class Delete:
    def __init__(self):
        self.data = []
        self.data_type = []
        self.collection = []
        
    def delete(self):
        response = None
        db = get_mongo_database()
        collection = db[self.collection]
        response = collection.delete_many({})
    
class Delete_Backlog(Delete):
    def __init__(self):
        super(Delete_Backlog, self).__init__()
        self.collection = 'backlog'

    def delete_collection(self, data_type, data):
        self.data = data_type
        self.data_type = data
        return True

class Exclude:
    def __init__(self):
        super(Exclude, self).__init__()
    
    def delete_all_backlog(self):
        ''' deleta todos os arquivos dentro do backlog do bd'''
        d = Delete_Backlog()
        d.delete_collection( None, None)
        return d.delete()

if __name__ == '__main__':
    d = Exclude()
    d.delete_all_backlog()

