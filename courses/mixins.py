from rest_framework import permissions
from .permissions import IsStaffEditorPermission

class StaffEditorPermissionMixin():
    permission_classes = [
        permissions.IsAdminUser, IsStaffEditorPermission
    ]

class StudentMixin():
    permission_classes = [permissions.IsAuthenticated]