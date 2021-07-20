
class BadCredentials(Exception):

    def __init__(self):
        self.message = (
                        {"error":
                             {"message": "Bad credentials"}
                        }
                        )

        super().__init__(self.message)