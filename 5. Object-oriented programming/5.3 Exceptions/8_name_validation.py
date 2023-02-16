class CyrillicError(Exception):
    pass


class CapitalError(Exception):
    pass


def name_validation(string):
    rus_abc = ''
    if not isinstance(string, str):
        raise TypeError
    else:
        if any(map(lambda x: not (1040 <= ord(x) <= 1071 or 1072 <= ord(x) <= 1103), string)):
            raise CyrillicError
        elif string[0].islower() or (string[1:] != string[1:].lower()):
            raise CapitalError
        else:
            return string


print(name_validation("иванов"))
