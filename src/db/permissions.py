ROL = {
    0: "user",
    1: "Evaluator",
    2: "Admin",
    3: "SuAdmin"
}

def is_user(user_rol):
    if user_rol == 0:
        return True
    else:
        return False

# def can_view_own(user_rol):
#     if user_rol == 0:
#         return True
#     else:
#         return False 

def is_evaluator(user_rol):
    if user_rol == 1:
        return True
    else:
        return False

def is_admin(user_rol):
    if user_rol == 2:
        return True
    else:
        return False

# def can_view_all(user_rol):
#     if user_rol == 2:
#         return True
#     else:
#         return False


def is_suadmin(user_rol):
    if user_rol == 3:
        return True
    else:
        return False
