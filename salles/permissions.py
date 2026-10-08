"""Tache 4 : permissions personnalisees.

A FAIRE :
  - IsOwnerOrReadOnly : lecture pour tous, modification/suppression
    reservee a l'auteur de la reservation (obj.utilisateur).
"""
from rest_framework import permissions  # noqa: F401  (a utiliser)

# TODO : votre code ici

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read-only permissions for GET
        if request.method in permissions.SAFE_METHODS:
            return True
        #permissions to PUT, PATCH (edit anything) is only granted to the owner of the reservation
        return obj.utilisateur == request.user