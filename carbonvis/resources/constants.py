##
#  Constants that affect the entire system
##

CO2_PER_KWH_AUSTRIA_ELECTRICITYMAP = 177
CO2_PER_KWH_WIEN_ENERGIE = 134
CO2_PER_KWH_US_COMPARISON = 402

UCARVER_BATTERY_CAPACITY_KW = 0.259
UCARVER_RANGE = 25
UCARVER_KWH_PER_KM = UCARVER_BATTERY_CAPACITY_KW / UCARVER_RANGE


# CO2 per KM for different vehicles

VEHICLE_TYPE_CO2 = {
    'ucarver': {
        'title': 'uCarver (Durchschnittstrom Ö)',
        'emissions': UCARVER_KWH_PER_KM * CO2_PER_KWH_AUSTRIA_ELECTRICITYMAP,   # 1,83372
        },
    'ucarver_wien': {
        'title': 'uCarver (Durchschnittstrom Wien Energie)',
        'emissions': UCARVER_KWH_PER_KM * CO2_PER_KWH_WIEN_ENERGIE,             # 1,38824
        },
    'ucarver_us': {
        'title': 'uCarver (Durchschnittstrom US East Coast)',
        'emissions': UCARVER_KWH_PER_KM * CO2_PER_KWH_US_COMPARISON,            # 4,16472
        },
    'moped': {
        'title': 'Moped (50cc)',
        'emissions': 47.90,                                                     # Guardian Liste
        },
    'motorcycle_125': {
        'title': 'Leichtmotorrad (125cc)',
        'emissions': 62.30,                                                     # Guardian Liste
        },
    'motorcycle': {
        'title': 'Motorrad (250c-750cc)',
        'emissions': 120.70,                                                    # Guardian Liste
        },
    'escooter_standard': {
        'title': 'eMoped',
        'emissions': 30.98,                                                     # Guardian Liste
        },
    'escooter_green': {
        'title': 'eMoped (Grüner Strom)',
        'emissions': 7.44,                                                      # Guardian Liste
        },
    'ebike': {
        'title': 'eBike / Pedelec',
        'emissions': 17.8,                                                      # ifeu, Datenbank Umwelt & Verkehr: http://www.emobil-umwelt.de/index.php/umweltbilanzen/gesamtbilanzen/pedelecs
        },
    'car_smart': {
        'title': 'Smart fortwo',
        'emissions': 88.0,                                                      # Smart fortwo passion (45bhp) https://www.energy.eu/car-co2-emissions
        },
    'car_golf': {
        'title': 'Volkswagen Golf S 1.4 TSI 5dr',
        'emissions': 138.0,                                                     # Volkswagen Golf S 1.4 TSI 5dr https://www.energy.eu/car-co2-emissions
        },
    'car_touareg': {
        'title': 'Volkswagen Touareg 2.5 TDI',
        'emissions': 243.0,                                                     # Volkswagen Touareg 2.5 TDI https://www.energy.eu/car-co2-emissions
        },
    'car_cayenne': {
        'title': 'Porsche Cayenne Turbo',
        'emissions': 358,                                                       # Porsche Cayenne Turbo https://www.energy.eu/car-co2-emissions/porsche.php
        },
    'pt_subway': {
        'title': 'UBahn (Wiener Linien)',
        'emissions': 12.0,                                                      # source: Wiener Linien
        },
}