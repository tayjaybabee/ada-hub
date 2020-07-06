class AdaSenseError(Exception):
    def __init__(self):
        pass


class InvalidTempScaleError(AdaSenseError):
    def __init__(self, message: str = None):
        """

        An exception to be raised when AdaSense finds or is provided an invalid temperature scale.

        Args:
            message (str): The message to pass to the user upon throwing this error
        """

        if message is None:
            self.message = 'An invalid temperature scale was provided.'

        else:
            self.message = message
