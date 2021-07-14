from http import HTTPStatus


class IncorrectKeysError(Exception):

    def __init__(self, wrong_fields: dict, required_fields: dict):
        self.message = {"error":
                             {"required keys": required_fields,
                              "wrong keys": wrong_fields}
                         }

        super().__init__(self.message)
