##
#  Constants that affect the entire system
##

CO2_PER_KWH_AUSTRIA_ELECTRICITYMAP = 177
CO2_PER_KWH_WIEN_ENERGIE = 134
CO2_PER_KWH_US_COMPARISON = 402

UCARVER_BATTERY_CAPACITY_KW = 0.259
UCARVER_RANGE = 25
UCARVER_KWH_PER_KM = UCARVER_BATTERY_CAPACITY_KW / UCARVER_RANGE

AVERAGE_CAR_LIFETIME_KM = 130000
AVERAGE_CO_CAR_PRODUCTION_PER_TON = 5500000

CAR_WEIGHTS_TONS = {
    'car_smart': 0.880000,
    'car_golf': 1.142000,
    'car_touareg': 2.154000,
    'car_cayenne': 2.215000,
    'eScooter': 0.0299,
}

# CO2 per KM for different vehicles

VEHICLE_TYPE_CO2 = {
    'walk': {
        'title': 'Fussgänger',                                                  # Guardian Liste
        'emissions_fuel': 24.15,
        'emissions_prod': 0,
        'emissions_tailpipe': 0
        },
    'cycle': {
        'title': 'Fahrradfahren',                                               # Guardian Liste
        'emissions_fuel': 18.40,
        'emissions_prod': 5,
        'emissions_tailpipe': 0,
        },
    'ucarver': {
        'title': 'uCarver (Durchschnittstrom Ö)',
        'emissions_fuel': UCARVER_KWH_PER_KM * CO2_PER_KWH_AUSTRIA_ELECTRICITYMAP,   # 1,83372
        'emissions_prod': 7,
        'emissions_tailpipe': 0
        },
    'ucarver_wien': {
        'title': 'uCarver (Durchschnittstrom Wien Energie)',
        'emissions_fuel': UCARVER_KWH_PER_KM * CO2_PER_KWH_WIEN_ENERGIE,        # 1,38824
        'emissions_prod': 7,
        'emissions_tailpipe': 0
        },
    'ucarver_us': {
        'title': 'uCarver (Durchschnittstrom US East Coast)',
        'emissions_fuel': UCARVER_KWH_PER_KM * CO2_PER_KWH_US_COMPARISON,       # 4,16472
        'emissions_prod': 7,
        'emissions_tailpipe': 0
        },
    'moped': {
        'title': 'Moped (50cc)',
        'emissions_fuel': 6.227,
        'emissions_prod': 4.7,                                                  # Guardian Liste
        'emissions_tailpipe': 39.0,
        },
    'motorcycle_125': {
        'title': 'Leichtmotorrad (125cc)',
        'emissions_fuel': 8.099,
        'emissions_prod': 6.230,                                                # Guardian Liste
        'emissions_tailpipe': 51.0,
        },
    'motorcycle': {
        'title': 'Motorrad (250c-750cc)',
        'emissions_fuel': 15.691,
        'emissions_prod': 12.070,                                               # Guardian Liste
        'emissions_tailpipe': 100.0,
        },
    'escooter_standard': {
        'title': 'eMoped',
        'emissions_fuel': 30.98,                                                     # Guardian Liste
        'emissions_tailpipe': 0,
        'emissions_prod': 14,
        },
    'escooter_green': {
        'title': 'eMoped (Grüner Strom)',
        'emissions_fuel': 7.44,                                                      # Guardian Liste
        'emissions_tailpipe': 0,
        'emissions_prod': 14,
        },
    'ebike': {
        'title': 'eBike / Pedelec',
        'emissions_fuel': 17.8,                                                      # ifeu, Datenbank Umwelt & Verkehr: http://www.emobil-umwelt.de/index.php/umweltbilanzen/gesamtbilanzen/pedelecs
        'emissions_tailpipe': 0,
        'emissions_prod': 7,
        },
    'car_smart': {
        'title': 'Smart fortwo',
        'emissions_fuel': 17.94,
        'emissions_prod': CAR_WEIGHTS_TONS['car_smart'] * AVERAGE_CO_CAR_PRODUCTION_PER_TON / AVERAGE_CAR_LIFETIME_KM,                                                    # Smart fortwo passion (45bhp) https://www.energy.eu/car-co2-emissions; 50 g/km production/disposal
        'emissions_tailpipe': 88.0,
        },
    'car_golf': {
        'title': 'Volkswagen Golf S 1.4 TSI 5dr',
        'emissions_fuel': 24.44,
        'emissions_prod': CAR_WEIGHTS_TONS['car_golf'] * AVERAGE_CO_CAR_PRODUCTION_PER_TON / AVERAGE_CAR_LIFETIME_KM,                                                     # Volkswagen Golf S 1.4 TSI 5dr https://www.energy.eu/car-co2-emissions; 50 g/km production/disposal
        'emissions_tailpipe': 138.0,
        },
    'car_touareg': {
        'title': 'Volkswagen Touareg 2.5 TDI',
        'emissions_fuel': 38.09,
        'emissions_prod': CAR_WEIGHTS_TONS['car_touareg'] * AVERAGE_CO_CAR_PRODUCTION_PER_TON / AVERAGE_CAR_LIFETIME_KM,                                                 # Volkswagen Touareg 2.5 TDI https://www.energy.eu/car-co2-emissions; 50 g/km production/disposal
        'emissions_tailpipe': 243.0,
        },
    'car_cayenne': {
        'title': 'Porsche Cayenne Turbo',
        'emissions_fuel': 53.04,
        'emissions_prod': CAR_WEIGHTS_TONS['car_cayenne'] * AVERAGE_CO_CAR_PRODUCTION_PER_TON / AVERAGE_CAR_LIFETIME_KM,                                                   # Porsche Cayenne Turbo https://www.energy.eu/car-co2-emissions/porsche.php; 50 g/km production/disposal
        'emissions_tailpipe': 358.0,
        },
    'pt_subway': {
        'title': 'UBahn (Wiener Linien)',
        'emissions_fuel': 12.0,                                                 # source: Wiener Linien 12.0,                                                      # source: Wiener Linien
        'emissions_tailpipe': 0.0,
        'emissions_prod': 16.0,
        },
    'pt_bus': {
        'title': 'Bus',
        'emissions_fuel': 1.0,                                                  # source: Wiener Linien
        'emissions_prod': 6.0,
        'emissions_tailpipe': 95.0,
        },
}