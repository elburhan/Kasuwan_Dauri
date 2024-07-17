from KasuwanDauriInventory.helpers import renderResponse
from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        if hasattr(request.user,'role') and request.user.role == 'Super admin':
            return True
        return False
    
def _call_(self, request):
    if not self.has_permission(request, None):
        return renderResponse(data='You are not authorized to access this page', message='You are not authorized to access this page', status=401) # Unauthorized', status=401
    return None