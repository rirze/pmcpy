from dataclasses import dataclass, fields, asdict
import json as json_lib


@dataclass
class data_structure:

    @classmethod
    def from_dict(cls, dict=None, json=None):
        if json:
            info = json_lib.loads(json)
        elif dict:
            info = dict
        else:
            raise ValueError("Either json or dict must be given!")

        fields_dict = {field.name: field.type(info[field.name])
                       for field in fields(cls)}

        return cls(**fields_dict)


    def to_dict(self):
        return asdict(self)
