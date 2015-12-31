from flask_login import current_user, login_required


class RestrictedMixin:
    @login_required
    def get_roles(self):
        user_roles = current_user.get_roles()
        roles = super().get_roles()
        return {
            key: list(set(values) & set(user_roles[key]))
            for key, values in roles.items()
        }
