ROL = {
    0: "user",
    1: "Evaluator",
    2: "Admin",
    3: "SuAdmin"
}

def can_upload_excel(user_rol):
    if user_rol == 0:
        return True
    else:
        return False

def can_view_own(user_rol):
    if user_rol == 0:
        return True
    else:
        return False


def can_validate(user_rol):
    return user_rol.nivel >= 0

def can_add_notes(user_rol):
    return user_rol.nivel >= 1

def can_view_all(user_rol):
    return user_rol.nivel >= 1

def can_close(user_rol):
    return user_rol.nivel >= 2

def can_change_roles(user_rol):
    return user_rol.nivel == 3
