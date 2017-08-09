import pymongo
import secrets
from models.account import Account as m_Account


class DBModel():

    def __init__(self, m_db):
        self.collection = getattr(m_db, self.c_name)

    def add(self, data):
        if isinstance(data, self.c_model):
            return self.collection.insert_one(data.to_dict())
        else:
            raise Exception("Data passed is not a {self.c_model} model.")

    def add_many(self, data):
        try:
            compiled = [x.to_dict for x in data]
            return self.collection.insert_many(compiled)
        except AttributeError:
            raise Exception("Data passed is not a {self.c_model} model.")


    def get_id(self, uid):
        return self.c_model(self.collection.find_one({"uid": uid}))


    def get_one(self, **kwarg):
        return self.c_model(self.collection.find_one(kwarg))


    def get_many(self, **kwarg):
        return [self.c_model(x) for x in self.collection.find(kwarg)]


    @property
    def size(self):
        return self.collection.count()




class DBAccount(DBModel):

    def __init__(self, m_db):
        self.c_name = "account"
        self.c_model = m_Account

        super().__init__(client, event)

