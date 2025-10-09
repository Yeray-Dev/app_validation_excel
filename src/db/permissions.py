ROL = {
    0: "User",
    1: "Evaluator",
    2: "Admin",
    3: "SuAdmin"
}

def can_upload_excel(User):
    return User.nivel == 0

def can_view_own(User):
    return User.nivel == 0

def can_validate(User):
    return User.nivel >= 0

def can_add_notes(User):
    return User.nivel >= 1

def can_view_all(User):
    return User.nivel >= 1

def can_close(User):
    return User.nivel >= 2

def can_change_roles(User):
    return User.nivel == 3
