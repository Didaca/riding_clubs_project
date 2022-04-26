VALIDATE_PLUS = 'Phone number must start with "+" !'
VALIDATE_NUMBER = 'Phone number must be contains only numbers!'
VALIDATE_OWNER_NAME = 'Owner name must be contains only letters!'
VALIDATE_OWNER_NAME_SPACE = 'Owner name must be separated with space!'
VALIDATE_NAME = 'Name must be contains only letters!'


def phone_number_validator(value):
    new_value = value[1::]
    if not value.startswith('+'):
        raise ValueError(VALIDATE_PLUS)
    if not new_value.isdigit():
        raise ValueError(VALIDATE_NUMBER)


def owner_name_validator(value):
    index = ''
    is_space = False
    for ind in range(len(value)):
        if value[ind].isspace():
            index = ind
            is_space = True
    if not is_space:
        raise ValueError(VALIDATE_OWNER_NAME_SPACE)
    new_value = value[:index] + value[index+1:]
    if not new_value.isalpha():
        raise ValueError(VALIDATE_OWNER_NAME)


def name_validator(value):
    if not value.isalpha():
        raise ValueError(VALIDATE_NAME)
