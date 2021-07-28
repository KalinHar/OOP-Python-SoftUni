def admin_access(ref_func):    # ref_func -> reference to function: read_book, get_product
    def wrapper(user_obj):     # user_obj -> reference to function argument : user
        if user_obj["is_admin"]:
            return ref_func(user_obj)
        raise PermissionError("Only for admins.")
    return wrapper


user_admin = {"name": "Pesho", "is_admin": True}
user_not_admin = {"name": "Tosho", "is_admin": False}


@admin_access
def read_book(user):
    print(f"{user['name']}, get this book")


@admin_access
def get_product(user):
    print(f"{user['name']}, get this product")


read_book(user_admin)
get_product(user_not_admin)
