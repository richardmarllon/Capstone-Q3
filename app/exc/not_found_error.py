class NotFound(Exception):

    def __init__(self):
        self.message = (
                        {"error":
                            {"Message": "Not found"}
                        }
                        )

        super().__init__(self.message)