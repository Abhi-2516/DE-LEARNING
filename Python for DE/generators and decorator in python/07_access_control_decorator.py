"""Use a decorator to protect a function from unauthorized roles."""

from functools import wraps


def require_admin(func):
    @wraps(func)
    def wrapper(user_role):
        if user_role != "admin":
            print("Access denied: admins only")
            return None
        return func(user_role)

    return wrapper


@require_admin
def access_tea_inventory(role):
    print(f"Access granted to tea inventory for {role}")


if __name__ == "__main__":
    access_tea_inventory("user")
    access_tea_inventory("admin")