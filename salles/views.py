"""Taches 3, 4, 5 (et bonus) : vues de l'API.

A FAIRE :
  - SalleViewSet (ModelViewSet), avec l'action `occupation` (tache 5)
  - ReservationViewSet (ModelViewSet), avec perform_create (tache 3)
"""
from rest_framework import viewsets, permissions  # noqa: F401  (a utiliser)

from .models import Reservation, Salle  # noqa: F401  (a utiliser)
from .serializers import ReservationSerializer, SalleSerializer
from rest_framework.pagination import PageNumberPagination
from .permissions import IsOwnerOrReadOnly

# TODO : votre code ici
class SalleViewSet(viewsets.ModelViewSet):
  queryset = Salle.objects.all()
  serializer_class = SalleSerializer

  def get_permissions(self):
      if self.action in ('list','retreive'):
          return [permissions.AllowAny]
      return[permissions.IsAdminUser]
#pagination of 10 on servervation pages
class ReservationPagination(PageNumberPagination):
    page_size = 10 


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    permission_classes =[permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]