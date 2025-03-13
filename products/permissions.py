from rest_framework import permissions

class IsArtistOrReadOnly(permissions.BasePermission):
    """ Custom permission:
    - Artist (sellers) can add, edit, and delete products.
    - Customers can only browse products.
    """

    def has_permission(self, request, view):
        # Allow GET requests for everyone
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow other methods only for artist
        return request.user.is_authenticated and request.user.role == "artist"

    def has_object_permission(self, request, view, obj):
        """ Object-level permission:
        - Artist can modify their own products.
        - Customers can only read.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.artist  # Only the owner can modify
