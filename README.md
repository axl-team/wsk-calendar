# WSK-CALENDAR

## Utilisation API france mobilité en temps réel.

ref : https://prim.iledefrance-mobilites.fr/apis/idfm-navitia-general-v2

Récupération de toute les lignes sur ce lien : https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/lines

Récupération des lignes avec le uri : https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/{uri}/lines
Pour récupérer les types de transport : https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/commercial_modes

Example pour récupérer les lignes de métro : https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia/commercial_modes%2Fcommercial_mode%3AMetro/lines

Version finale de l'appel : 

Types de transports récupérés:
- commercial_mode:LocalTrain -> Train transilien
- commercial_mode:Metro -> Métro
- commercial_mode:RapidTransit -> RER
- commercial_mode:Tramway -> Tramway
