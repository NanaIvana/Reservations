"""Tache 1 et 2 : serializers et validation.

A FAIRE :
  - SalleSerializer (ModelSerializer)
  - ReservationSerializer (ModelSerializer) :
      * le champ `utilisateur` est en LECTURE SEULE (il sera renseigne par la vue)
      * validation : `fin` strictement apres `debut`
      * validation : pas de chevauchement avec une autre reservation CONFIRMEE
        de la meme salle
"""
from rest_framework import serializers

from .models import Reservation, Salle  # noqa: F401  (a utiliser)

# TODO : votre code ici

class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = ['nom', 'capacite', 'batiment']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ["salle", "utilisateur", "debut", "fin", "motif", "statut", "cree_le"]
        read_only_fields = ["utilisateur"]

    def validate(self, data):
        instance = self.instance

       # Fallback to existing instance values during partial updates (PATCH)
        salle = data.get("salle", instance.salle if instance else None)
        debut = data.get("debut", instance.debut if instance else None)
        fin = data.get("fin", instance.fin if instance else None)
        statut = data.get("statut",instance.statut if instance else Reservation.Statut.CONFIRMEE)

        #une reservation dont fin n’est pas strictement posterieure debut
        if debut and fin and fin <= debut:
            raise serializers.ValidationError("La fin doit être strictement postérieure au début.")

        if salle and debut and fin and statut == Reservation.Statut.CONFIRMEE:
            #deux crØneaux qui se touchent (l’un nit 10h, l’autre commence 10h) ne se chevauchent pas
            conflits = Reservation.objects.filter(salle=salle, statut=Reservation.Statut.CONFIRMEE, debut__lt=fin, fin__gt=debut)
            if instance:
                #des creneaux sur des salles diffrentes ne se gŒnent jamais
                conflits = conflits.exclude(pk=instance.pk)
            if conflits.exists():
                raise serializers.ValidationError( "The class is already reserved.")

        return data