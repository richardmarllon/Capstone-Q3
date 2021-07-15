from http import HTTPStatus


class MissingKeys(Exception):

    def __init__(self, missing_keys: dict, required_keys: list):
        self.message = (
                        {"error":
                             {"required keys": required_keys,
                              "missing keys": missing_keys}
                        }
                        )

        super().__init__(self.message)