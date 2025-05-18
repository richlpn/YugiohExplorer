import json

class State():

    __value: object

    def __init__(self, new_value=None):
        self.__value = new_value
        
    def set_value(self, new_value):
        self.__value = new_value
    
    def to_dict(self):
        return {'value': self.__value}

    @property
    def value(self):
        return self.__value
    @classmethod
    def from_dict(cls, data):
        return cls(new_value=data.get('value'))

    def to_json(self):
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls.from_dict(data)