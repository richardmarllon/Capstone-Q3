class Not_Permission(Exception):

    def __init__(self):
        self.message = {"message": "You do not have permission to use that command!"}
                                                 

        super().__init__(self.message)

    