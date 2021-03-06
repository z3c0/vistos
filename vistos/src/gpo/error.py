"""Custom errors for all things bioguide-related"""


class InvalidRangeError(Exception):
    """The given Congress range can be perceived as both years or congresses"""

    def __init__(self):
        msg = 'Ranges that begin before 1785 but end afterwards are invalid'
        super().__init__(msg)


class InvalidPositionError(Exception):
    """nvalid position used"""

    def __init__(self, option: str = None):
        if option:
            msg = f'{option} is not a valid position'
        else:
            msg = 'Invalid position given'
        super().__init__(msg)


class InvalidPartyError(Exception):
    """Invalid party used"""

    def __init__(self, option: str = None):
        if option:
            msg = f'{option} is not a valid party'
        else:
            msg = 'Invalid party given'
        super().__init__(msg)


class InvalidStateError(Exception):
    """Invalid state used"""

    def __init__(self, option: str = None):
        if option:
            msg = f'{option} is not a valid state'
        else:
            msg = 'Invalid state given'
        super().__init__(msg)


class InvalidCongressError(Exception):
    """Invalid Congress number used"""

    def __init__(self, option: int = None):
        if option:
            msg = f'{str(option)} is not a valid Congress number'
        else:
            msg = 'Invalid Congress number given'
        super().__init__(msg)


class InvalidBioguideError(Exception):
    """Attepting to overwrite existing bioguide data with an invalid object"""

    def __init__(self):
        super().__init__('Invalid Bioguide object')


class InvalidGovInfoError(Exception):
    """Attepting to overwrite existing govinfo data with an invalid object"""

    def __init__(self):
        super().__init__('Invalid GovInfo object')


class InvalidGovInfoBillsError(Exception):
    """Attepting to overwrite existing govinfo data with an invalid object"""

    def __init__(self):
        super().__init__('Invalid GovInfo bills object')


class BioguideConnectionError(Exception):
    """Connection to bioguideretro.congress.gov failed"""


class GovinfoConnectionError(Exception):
    """Connection to api.govinfo.gov failed"""


class GovinfoInternalServerError(Exception):
    """The Govinfo API encountered an internal server error"""

    def __init__(self, endpoint):
        super().__init__(f'Internal Server Error encountered at {endpoint}')
