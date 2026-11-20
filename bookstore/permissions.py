from datetime import timedelta
from django.utils import timezone
from rest_framework.permissions import DjangoModelPermissions, SAFE_METHODS


class IsMatureUserWithModelPermissions(DjangoModelPermissions):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if not super().has_permission(request, view):
            return False

        user = request.user
        if not user or not user.is_authenticated or not user.date_joined:
            return False

        return (timezone.now() - user.date_joined) > timedelta(hours=24)