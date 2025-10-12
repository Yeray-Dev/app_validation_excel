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

def can_view_no_validation(user_rol):
    if user_rol == 1:
        return True
    else:
        return False

def can_close(user_rol):
    if user_rol == 2:
        return True
    else:
        return False

def can_view_all(user_rol):
    if user_rol == 2:
        return True
    else:
        return False


def can_change_roles(user_rol):
    if user_rol == 3:
        return True
    else:
        return False
