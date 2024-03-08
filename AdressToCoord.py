from geopy.geocoders import Nominatim
from geopy.exc import GeocoderServiceError
import ssl

def main (params):

    # Désactiver la vérification du certificat SSL
    ssl._create_default_https_context = ssl._create_unverified_context

    # Adresse à géocoder
    

    # Création d'une instance de la classe Nominatim
    geolocator = Nominatim(user_agent="my_request")

    try:
        # Application de la méthode geocode pour obtenir la localisation
        location = geolocator.geocode(params['adresse'])

        # Affichage de l'adresse et des coordonnées
    except GeocoderServiceError as e:
        print(f"Erreur lors de la géolocalisation : {e}")

    return {
    "loc_Latitude": location.latitude,
    "loc_Longitude": location.longitude,
    "adress": params['adresse']
    } 