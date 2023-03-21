from combojsonapi.permission.permission_system import (
    PermissionMixin,
    PermissionUser,
    PermissionForPatch,
)

from flask_combo_jsonapi.exceptions import AccessDenied
from flask_login import current_user

from blog.models import User, Article


class ArticlePermission(PermissionMixin):
    PATCH_AVAILABLE_FIELDS = [
        "title",
        "text",
        "author",
        "tags,"
    ]

    def patch_permission(self, *args, user_permission: PermissionUser = None, **kwargs) -> PermissionForPatch:
        self.permission_for_patch.allow_columns = (self.PATCH_AVAILABLE_FIELDS, 10)

        return self.permission_for_patch

    def patch_data(self, *args, data: dict = None, obj: Article = None, user_permission: PermissionUser = None,
                   **kwargs) -> dict:
        permission_for_patch = user_permission.permission_for_patch_permission(model=Article)

        if not current_user.is_staff and not current_user.id == obj.author.user.id:
            raise AccessDenied("only Author and Admin has permission for update")

        return {
            i_key: i_val
            for i_key, i_val in data.items()
            if i_key in permission_for_patch.columns
        }
