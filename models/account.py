import json


class Account():

    properties = ["uid", "username", "password", "avatar", "join_date", "active"]
    model_type = "account"

    def __init__(self, data=None):

        for prop in self.properties:
            self.__dict__[prop] = None

        if data:
            self.__dict__.update(data)


    def to_dict(self):
        return self.__dict__


    def to_json(self):
        return json.dumps(self.__dict__)