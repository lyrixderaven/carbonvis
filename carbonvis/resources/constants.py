##
#  Constants that affect the entire system
##

CO2_PER_KWH_AUSTRIA_ELECTRICITYMAP = 177
CO2_PER_KWH_WIEN_ENERGIE = 134.88
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
        'title': 'Fussgänger',
        'emissions_fuel': 24.15,
        'emissions_prod': 0,
        'emissions_tailpipe': 0,
        'info': '''
            <h2>Fussgänger</h2>
            <h3>"Treibstoff"</h3>
            FussgängerInnen verbrauchen Kalorien, welche als Nahrung zu sich genommen werden. Der CO₂-Fussabdruck hängt hier hauptsächlich von Art und Produktionsort der Zutaten ab. Importierte Nahrungsmittel und fleischhaltige Kost sind hier besonders CO₂-intensiv, lokale Nahrunsmittel und fleischlose Zutaten produzieren einen geringeren Fussabdruck.<br />
            Der verwendete Wert von <span class='formula'>24,15 g CO₂/km</span> basiert auf einer <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a><br />
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck= Distanz * 24,15 g CO₂/km</span>
        ''',
        },# Guardian Liste
    'cycle': {
        'title': 'Fahrradfahren',
        'emissions_fuel': 18.40,
        'emissions_prod': 5,
        'emissions_tailpipe': 0,
        'info': '''
            <h2>Fahrradfahren</h2>
            <h3>"Treibstoff"</h3>
            FahrradfahrerInnen verbrauchen Kalorien, welche als Nahrung zu sich genommen werden. Der CO₂-Fussabdruck hängt hier hauptsächlich von Art und Produktionsort der Zutaten ab. Importierte Nahrungsmittel und fleischhaltige Kost sind hier besonders CO₂-intensiv, lokale Nahrunsmittel und fleischlose Zutaten produzieren einen geringeren Fussabdruck.<br />
            Der verwendete Wert von <span class='formula'>18,40 g CO₂/km</span> basiert auf einer <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a><br />
            <h3>Produktion</h3>
            Die Produktion eines Fahrrads verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe.<br />
            Der verwendete Wert von <span class='formula'>5,0 g CO₂/km</span> basiert auf einer <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a>
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (18,40 g CO₂/km + 5,0 g CO₂/km)</span>
        ''',
        },# Guardian Liste
    'ucarver': {
        'title': 'uCarver (AT)',
        'emissions_fuel': UCARVER_KWH_PER_KM * CO2_PER_KWH_AUSTRIA_ELECTRICITYMAP,
        'emissions_prod': 7,
        'emissions_tailpipe': 0,
        'info': '''
            <h2>uCarver (Durchschnittstrom Ö)</h2>
            <h3>Treibstoff</h3>
            eScooter verbrauchen Strom, welcher je nach Erzeugungsart unterschiedlichen CO₂-Ausstoß verursacht. Die Zusammenstellung des Stroms dieser Kategorie basiert auf der <a href="https://www.electricitymap.org/?page=country&solar=false&remote=true&wind=false&countryCode=AT">durchschnittlichen Stromzusammensetzung in Österreich</a> und ist tagesaktuell teilweise starken Schwankungen unterworfen. Je mehr Strom in Österreich aus Wind- und Wasserkraft (mit geringem CO₂-Ausstoss) erzeugt werden kann, desto weniger Strom wird aus Gas-, Biomasse- und Kohlekraftwerken erzeugt oder zugekauft.<br />
            Der tatsächliche Verbrauch errechnet sich aus der maximalen Reichweite des eScooters (<span class='formula'>25 km</span>) und der Kapazität der Batterie (<span class='formula'>0,259 kW</span>) .
            <h3>Produktion</h3>
            Die Produktion eines eScooters verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe, insbesondere der Batterien/Akkus.<br />
            Der verwendete Wert von <span class='formula'>7,0 g CO₂/km</span> basiert auf dem Wert für vergleichbare eBikes einer <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a>.
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (0,259 kW / 25 km * 177 g CO₂ / kWh) + 7,0 g CO₂/km)</span>
        ''',
        },# 1,83372
    'ucarver_wien': {
        'title': 'uCarver (WienEnergie)',
        'emissions_fuel': UCARVER_KWH_PER_KM * CO2_PER_KWH_WIEN_ENERGIE,
        'emissions_prod': 7,
        'emissions_tailpipe': 0,
        'info': '''
            <h2>uCarver (Durchschnittstrom Wien Energie)</h2>
            <h3>Treibstoff</h3>
            eScooter verbrauchen Strom, welcher je nach Erzeugungsart unterschiedlichen CO₂-Ausstoß verursacht. Die Zusammenstellung des Stroms dieser Kategorie basiert auf der <a href="https://www.wienenergie.at/media/files/2018/stromkennzeichnung_privat_2018-04_243252.pdf">durchschnittlichen Stromzusammensetzung des WienEnergie 'OPTIMA' Tarifs im Jahr 2017</a> und ist tagesaktuell teilweise starken Schwankungen unterworfen. Je mehr Strom die WienEnergie Vertrieb GMBH aus Wind- und Wasserkraft (mit geringem CO₂-Ausstoss) beziehen kann, desto weniger Strom wird aus Gas-, Biomasse- und Kohlekraftwerken erzeugt oder zugekauft.<br />
            Der tatsächliche Verbrauch errechnet sich aus der maximalen Reichweite des eScooters (<span class='formula'>25 km</span>) und der Kapazität der Batterie (<span class='formula'>0,259 kW</span>).
            <h3>Produktion</h3>
            Die Produktion eines eScooters verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe, insbesondere der Batterien/Akkus.<br />
            Der verwendete Wert von <span class='formula'>7,0 g CO₂/km</span> basiert auf dem Wert für vergleichbare eBikes einer <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a>.
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (0,259 kW / 25 km * 134,88 g CO₂ / kWh) + 7,0 g CO₂/km)</span>
        ''',
        },# 1,38824
    'ucarver_us': {
        'title': 'uCarver (US)',
        'emissions_fuel': UCARVER_KWH_PER_KM * CO2_PER_KWH_US_COMPARISON,
        'emissions_prod': 7,
        'emissions_tailpipe': 0,
        'info': '''
            <h2>uCarver (Durchschnittstrom US East Coast)</h2>
            <h3>Treibstoff</h3>
            eScooter verbrauchen Strom, welcher je nach Erzeugungsart unterschiedlichen CO₂-Ausstoß verursacht. Die Zusammenstellung des Stroms dieser Kategorie basiert auf der <a href="https://www.eia.gov/environment/emissions/state/analysis/">durchschnittlichen Stromzusammensetzung an der Ostküste der USA</a> und ist tagesaktuell teilweise starken Schwankungen unterworfen. Im Vergleich mit Österreich erzeugen die USA weit mehr Strom aus CO₂-intensiven, fossilen Rohstoffen wie Kohle- oder Kernkraftwerken. Je mehr Strom aus Wind- und Wasserkraft (mit geringem CO₂-Ausstoss) bezogen werden kann, desto weniger Strom wird aus Gas-, Biomasse- und Kohlekraftwerken erzeugt oder zugekauft.<br />
            Der tatsächliche Verbrauch errechnet sich aus der maximalen Reichweite des eScooters (<span class='formula'>25 km</span>) und der Kapazität der Batterie (0,259 kW).
            <h3>Produktion</h3>
            Die Produktion eines eScooters verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe, insbesondere der Batterien/Akkus.<br />
            Der verwendete Wert von <span class='formula'>7,0 g CO₂/km </span>basiert auf dem Wert für vergleichbare eBikes einer <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a>.
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (0,259 kW / 25 km * 402,88 g CO₂ / kWh) + 7,0 g CO₂/km)</span>
        ''',
        },# 4,16472
    'moped': {
        'title': 'Moped (50cc)',
        'emissions_fuel': 6.227,
        'emissions_prod': 4.7,
        'emissions_tailpipe': 39.0,
        'info': '''
            <h2>Moped (50cc)</h2>
            <h3>Treibstoff</h3>
            Die Produktion und der Transport von Treibstoffen wie Benzin oder Diesel verursachen signifikante CO₂-Ausstöße, bevor sie überhaupt beim Endverbraucher ankommen. Fahrzeuge mit höherem Verbrauch verursachen somit auch beim Auftanken bereits höhere CO₂-Ausstöße. Der verwendete Wert von <span class='formula'>6.227 g CO₂/km</span> basiert auf <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und ist mit etwa 13\% des CO₂-Ausstoßes über den Lebenszyklus des Fahrzeuges pro km und Passagier laut einer <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a> angesetzt.
            <h3>Produktion</h3>
            Die Produktion eines Mopeds verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe.<br />
            Der verwendete Wert von <span class='formula'>4,7 g CO₂/km</span> basiert auf der Aufteilung für des CO₂-Ausstoßes pro Kilomenter von PKWs einer <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und ist mit etwa <span class='formula'>10\%</span> des CO₂-Ausstoßes über den Lebenszyklus des Fahrzeuges pro km und Passagier laut einer <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a> angesetzt.
            <h3>Abgase</h3>
            Die Verbrennung von Treibstoffen zum Antrieb eines Fahrzeugmotors verursacht Abgase, welche unter anderem auch CO₂ beinhalten. Der verwendete Wert von <span class='formula'>39,0 g CO₂/km </span>basiert auf der <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a>.
            <h3>Berechnung</h3>
           <span class='formula'> CO₂ Fußabdruck = Distanz * (6,227 g CO₂ / kWh + 4,7 g CO₂/km + 39,0 g CO₂/km)</span>
        ''',
        },# Guardian Liste
    'motorcycle_125': {
        'title': 'Leichtmotorrad (125cc)',
        'emissions_fuel': 8.099,
        'emissions_prod': 6.230,
        'emissions_tailpipe': 51.0,
        'info': '''
            <h2>Leichtmotorrad (125cc)</h2>
            <h3>Treibstoff</h3>
            Die Produktion und der Transport von Treibstoffen wie Benzin oder Diesel verursachen signifikante CO₂-Ausstöße, bevor sie überhaupt beim Endverbraucher ankommen. Fahrzeuge mit höherem Verbrauch verursachen somit auch beim Auftanken bereits höhere CO₂-Ausstöße. Der verwendete Wert von <span class='formula'>8,099 g CO₂/km</span> basiert auf <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und ist mit etwa <span class='formula'>13\%</span> des CO₂-Ausstoßes über den Lebenszyklus des Fahrzeuges pro km und Passagier laut einer <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a> angesetzt.
            <h3>Produktion</h3>
            Die Produktion eines Leichtmotorrads verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe.<br />
            Der verwendete Wert von <span class='formula'>6,230 g CO₂/km</span> basiert auf der Aufteilung für des CO₂-Ausstoßes pro Kilomenter von PKWs einer <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und ist mit etwa <span class='formula'>10\%</span> des CO₂-Ausstoßes über den Lebenszyklus des Fahrzeuges pro km und Passagier laut einer <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a> angesetzt.
            <h3>Abgase</h3>
            Die Verbrennung von Treibstoffen zum Antrieb eines Fahrzeugmotors verursacht Abgase, welche unter anderem auch CO₂ beinhalten. Der verwendete Wert von <span class='formula'>51,0 g CO₂/km</span> basiert auf der <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a>.
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (8,099 g CO₂ / kWh + 6,23 g CO₂/km + 51,0 g CO₂/km)</span>
        ''',
        },# Guardian Liste
    'motorcycle': {
        'title': 'Motorrad (250c-750cc)',
        'emissions_fuel': 15.691,
        'emissions_prod': 12.070,
        'emissions_tailpipe': 100.0,
        'info': '''
            <h2>Motorrad (250c-750cc)</h2>
            Die Produktion und der Transport von Treibstoffen wie Benzin oder Diesel verursachen signifikante CO₂-Ausstöße, bevor sie überhaupt beim Endverbraucher ankommen. Fahrzeuge mit höherem Verbrauch verursachen somit auch beim Auftanken bereits höhere CO₂-Ausstöße. Der verwendete Wert von <span class='formula'>15,691 g CO₂/km</span> basiert auf <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und ist mit etwa <span class='formula'>13\%</span> des CO₂-Ausstoßes über den Lebenszyklus des Fahrzeuges pro km und Passagier laut einer <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a> angesetzt.
            <h3>Produktion</h3>
            Die Produktion eines Motorrads verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe.<br />
            Der verwendete Wert von <span class='formula'>12,07 g CO₂/km</span> basiert auf der Aufteilung für des CO₂-Ausstoßes pro Kilomenter von PKWs einer <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und ist mit etwa <span class='formula'>10\%</span> des CO₂-Ausstoßes über den Lebenszyklus des Fahrzeuges pro km und Passagier laut einer <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a> angesetzt.
            <h3>Abgase</h3>
            Die Verbrennung von Treibstoffen zum Antrieb eines Fahrzeugmotors verursacht Abgase, welche unter anderem auch CO₂ beinhalten. Der verwendete Wert von <span class='formula'>100,0 g CO₂/km</span> basiert auf der <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a>.
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (15,691 g CO₂ / kWh + 12,07 g CO₂/km + 100,0 g CO₂/km)</span>
        ''',
        },# Guardian Liste
    'escooter_standard': {
        'title': 'eMoped',
        'emissions_fuel': 30.98,
        'emissions_tailpipe': 0,
        'emissions_prod': 14,
        'info': '''
            <h2>eMoped</h2>
            <h3>Treibstoff</h3>
            eMopeds verbrauchen Strom, welcher je nach Erzeugungsart unterschiedlichen CO₂-Ausstoß verursacht. Der verwendete Wert von <span class='formula'>30,98 g CO₂/km</span> des Stroms dieser Kategorie basiert auf der <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a> für europäischen Durchschnittsstrom und ist tagesaktuell teilweise starken Schwankungen unterworfen. Je mehr Strom aus Wind- und Wasserkraft (mit geringem CO₂-Ausstoss) erzeugt kann, desto weniger Strom wird aus Gas-, Biomasse- und Kohlekraftwerken erzeugt oder zugekauft.<br />
            <h3>Produktion</h3>
            Die Produktion eines eMopeds verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe, insbesondere der Batterien/Akkus.<br />
            Der verwendete Wert von <span class='formula'>14,0 g CO₂/km</span> basiert auf dem Wert für vergleichbare eBikes und Mopeds einer <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a>.
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (30,98 g CO₂ / kWh + 14,0 g CO₂/km)</span>
        ''',
        },# Guardian Liste
    'escooter_green': {
        'title': 'eMoped (Grüner Strom)',
        'emissions_fuel': 7.44,
        'emissions_tailpipe': 0,
        'emissions_prod': 14,
        'info': '''
            <h2>eMoped (Grüner Strom)</h2>
            <h3>Treibstoff</h3>
            eMopeds verbrauchen Strom, welcher je nach Erzeugungsart unterschiedlichen CO₂-Ausstoß verursacht. Der verwendete Wert von <span class='formula'>7,44 g CO₂/km</span> des Stroms dieser Kategorie basiert auf der <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a> für europäischen ÖKO-Strom aus rein erneuerbaren Energiequellen wie Wasserkraft- oder Windkraftanlagen und ist tagesaktuell teilweise starken Schwankungen unterworfen.<br />
            <h3>Produktion</h3>
            Die Produktion eines eMopeds verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe, insbesondere der Batterien/Akkus.<br />
            Der verwendete Wert von <span class='formula'>14,0 g CO₂/km</span> basiert auf dem Wert für vergleichbare eBikes und Mopeds einer <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a>.
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (7,44 g CO₂ / kWh + 14,0 g CO₂/km)</span>
        ''',
        },# Guardian Liste
    'ebike': {
        'title': 'eBike / Pedelec',
        'emissions_fuel': 10.8 + 6.0,
        'emissions_tailpipe': 0,
        'emissions_prod': 7,
        'info': '''
            <h2>eBike / Pedelec</h2>
            <h3>Treibstoff</h3>
        eBikes verbrauchen Strom, welcher je nach Erzeugungsart unterschiedlichen CO₂-Ausstoß verursacht. Der verwendete Wert von <span class='formula'>10,8 g CO₂/km</span> des Stroms dieser Kategorie basiert auf <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> für europäischen Durchschnitts-Strom und ist tagesaktuell teilweise starken Schwankungen unterworfen. <br />
            Die Benutzung von eBikes forder weiters gewissen körperlichen Einsatz und verbraucht damit Kalorien, welche als Nahrung zu sich genommen werden. Der CO₂-Fussabdruck hängt hier hauptsächlich von Art und Produktionsort der Zutaten ab. Importierte Nahrungsmittel und fleischhaltige Kost sind hier besonders CO₂-intensiv, lokale Nahrunsmittel und fleischlose Zutaten produzieren einen geringeren Fussabdruck. Der verwendete Wert von <span class='formula'>6,0 g CO₂/km</span> basiert auf obiger <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a>.
            <h3>Produktion</h3>
            Die Produktion eines eBikes verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe, insbesondere der Batterien/Akkus.<br />
            Der verwendete Wert von <span class='formula'>7,0 g CO₂/km</span> basiert auf der obigen <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a>.
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (10,8 g CO₂ / kWh + 6,0 g CO₂ / kWh + 7,0 g CO₂/km)</span>
        ''',
        },     # ifeu, Datenbank Umwelt & Verkehr: http://www.emobil-umwelt.de/index.php/umweltbilanzen/gesamtbilanzen/pedelecs
    'car_smart': {
        'title': 'Smart fortwo',
        'emissions_fuel': 17.94,
        'emissions_prod': CAR_WEIGHTS_TONS['car_smart'] * AVERAGE_CO_CAR_PRODUCTION_PER_TON / AVERAGE_CAR_LIFETIME_KM,
        'emissions_tailpipe': 88.0,
        'info': '''
            <h2>Smart fortwo</h2>
            <h3>Treibstoff</h3>
            Die Produktion und der Transport von Treibstoffen wie Benzin oder Diesel verursachen signifikante CO₂-Ausstöße, bevor sie überhaupt beim Endverbraucher ankommen. Fahrzeuge mit höherem Verbrauch verursachen somit auch beim Auftanken bereits höhere CO₂-Ausstöße. Der verwendete Wert von <span class='formula'>17,94 g CO₂/km</span> basiert auf einer<a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und ist mit etwa <span class='formula'>13\%</span> des CO₂-Ausstoßes über den Lebenszyklus des Fahrzeuges pro km und Passagier laut einer <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a> angesetzt.
            <h3>Produktion</h3>
            Die Produktion eines PKW verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe.<br />
            Der verwendete Wert von <span class='formula'>37,32 g CO₂/km</span> basiert auf der <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und berechnet sich aus dem Leergewicht der Fahrzeuges in Tonnen (<span class='formula'>0,88 t</span>), dem CO₂-Ausstoß bei der Produktion von PKWs  (<span class='formula'>5.5 t CO₂ / t</span>) und der durchschnittlichen Lebensdauer des PKW in Kilometern (<span class='formula'>130.000 km</span>) wie folgt:<br />
                <span class='formula'>CO₂ Produktion = (0,88 t * 5.500.000 g CO₂/t) / 130.000 km</span>
            <h3>Abgase</h3>
            Die Verbrennung von Treibstoffen zum Antrieb eines Fahrzeugmotors verursacht Abgase, welche unter anderem auch CO₂ beinhalten. Der verwendete Wert von <span class='formula'>88,0 g CO₂/km</span> basiert auf einer Liste  des <a href="hhttps://www.energy.eu/car-co2-emissions/">European Energy Portal</a>.
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (17,94 g CO₂/km + 37,32 g CO₂/km + 88,0 g CO₂/km)</span>
        ''',
        },# Smart fortwo passion (45bhp) https://www.energy.eu/car-co2-emissions; 50 g/km production/disposal
    'car_golf': {
        'title': 'Volkswagen Golf S 1.4 TSI 5dr',
        'emissions_fuel': 24.44,
        'emissions_prod': CAR_WEIGHTS_TONS['car_golf'] * AVERAGE_CO_CAR_PRODUCTION_PER_TON / AVERAGE_CAR_LIFETIME_KM,
        'emissions_tailpipe': 138.0,
        'info': '''
            <h2>Volkswagen Golf S 1.4 TSI 5dr</h2>
            <h3>Treibstoff</h3>
            Die Produktion und der Transport von Treibstoffen wie Benzin oder Diesel verursachen signifikante CO₂-Ausstöße, bevor sie überhaupt beim Endverbraucher ankommen. Fahrzeuge mit höherem Verbrauch verursachen somit auch beim Auftanken bereits höhere CO₂-Ausstöße. Der verwendete Wert von <span class='formula'>24,44 g CO₂/km</span> basiert auf einer<a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und ist mit etwa <span class='formula'>13\%</span> des CO₂-Ausstoßes über den Lebenszyklus des Fahrzeuges pro km und Passagier laut einer <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a> angesetzt.
            <h3>Produktion</h3>
            Die Produktion eines PKW verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe.<br />
            Der verwendete Wert von <span class='formula'>48,31 g CO₂/km </span>basiert auf der <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und berechnet sich aus dem Leergewicht der Fahrzeuges in Tonnen (<span class='formula'>1,14 t</span>), dem CO₂-Ausstoß bei der Produktion von PKWs  (<span class='formula'>5.5 t CO₂ / t</span>) und der durchschnittlichen Lebensdauer des PKW in Kilometern (<span class='formula'>130.000 km</span>) wie folgt:<br />
                <span class='formula'>CO₂ Produktion = (1,152 t * 5.500.000 g CO₂/t) / 130.000 km</span>
            <h3>Abgase</h3>
            Die Verbrennung von Treibstoffen zum Antrieb eines Fahrzeugmotors verursacht Abgase, welche unter anderem auch CO₂ beinhalten. Der verwendete Wert von <span class='formula'>138,0 g CO₂/km</span> basiert auf einer Liste des <a href="hhttps://www.energy.eu/car-co2-emissions/">European Energy Portal</a>.
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (24,44 g CO₂/km + 48,31 g CO₂/km + 138,0 g CO₂/km)</span>
        ''',
        },# Volkswagen Golf S 1.4 TSI 5dr https://www.energy.eu/car-co2-emissions; 50 g/km production/disposal
    'car_touareg': {
        'title': 'Volkswagen Touareg 2.5 TDI',
        'emissions_fuel': 38.09,
        'emissions_prod': CAR_WEIGHTS_TONS['car_touareg'] * AVERAGE_CO_CAR_PRODUCTION_PER_TON / AVERAGE_CAR_LIFETIME_KM,
        'emissions_tailpipe': 243.0,
        'info': '''
            <h2>Volkswagen Touareg 2.5 TDI</h2>
            <h3>Treibstoff</h3>
            Die Produktion und der Transport von Treibstoffen wie Benzin oder Diesel verursachen signifikante CO₂-Ausstöße, bevor sie überhaupt beim Endverbraucher ankommen. Fahrzeuge mit höherem Verbrauch verursachen somit auch beim Auftanken bereits höhere CO₂-Ausstöße. Der verwendete Wert von <span class='formula'>38,09 g CO₂/km</span> basiert auf einer<a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und ist mit etwa <span class='formula'>13\% </span>des CO₂-Ausstoßes über den Lebenszyklus des Fahrzeuges pro km und Passagier laut einer <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a> angesetzt.
            <h3>Produktion</h3>
            Die Produktion eines PKW verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe.<br />
            Der verwendete Wert von <span class='formula'>90,96 g CO₂/km</span> basiert auf der <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und berechnet sich aus dem Leergewicht der Fahrzeuges in Tonnen (<span class='formula'>2,15 t</span>), dem CO₂-Ausstoß bei der Produktion von PKWs  (<span class='formula'>5.5 t CO₂ / t</span>) und der durchschnittlichen Lebensdauer des PKW in Kilometern (<span class='formula'>130.000 km</span>) wie folgt:<br />
                <span class='formula'>CO₂ Produktion = (2,15 t * 5.500.000 g CO₂/t) / 130.000 km</span>
            <h3>Abgase</h3>
            Die Verbrennung von Treibstoffen zum Antrieb eines Fahrzeugmotors verursacht Abgase, welche unter anderem auch CO₂ beinhalten. Der verwendete Wert von <span class='formula'>243,0 g CO₂/km</span> basiert auf einer Liste des <a href="hhttps://www.energy.eu/car-co2-emissions/">European Energy Portal</a>.
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (38,09 g CO₂/km + 90,96 g CO₂/km + 243,0 g CO₂/km)</span>
        ''',
        },# Volkswagen Touareg 2.5 TDI https://www.energy.eu/car-co2-emissions; 50 g/km production/disposal
    'car_cayenne': {
        'title': 'Porsche Cayenne Turbo',
        'emissions_fuel': 53.04,
        'emissions_prod': CAR_WEIGHTS_TONS['car_cayenne'] * AVERAGE_CO_CAR_PRODUCTION_PER_TON / AVERAGE_CAR_LIFETIME_KM,
        'emissions_tailpipe': 358.0,
        'info': '''
            <h2>Porsche Cayenne Turbo</h2>
            <h3>Treibstoff</h3>
            Die Produktion und der Transport von Treibstoffen wie Benzin oder Diesel verursachen signifikante CO₂-Ausstöße, bevor sie überhaupt beim Endverbraucher ankommen. Fahrzeuge mit höherem Verbrauch verursachen somit auch beim Auftanken bereits höhere CO₂-Ausstöße. Der verwendete Wert von <span class='formula'>53,04 g CO₂/km</span> basiert auf einer<a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und ist mit etwa <span class='formula'>13\%</span> des CO₂-Ausstoßes über den Lebenszyklus des Fahrzeuges pro km und Passagier laut einer <a href="https://www.theguardian.com/environment/datablog/2009/sep/02/carbon-emissions-per-transport-type">CO₂-Verbrauchs-Liste des Guardian</a> angesetzt.
            <h3>Produktion</h3>
            Die Produktion eines PKW verursacht CO₂ bei Abbau, Transport und Verarbeitung der nötigen Rohstoffe.<br />
            Der verwendete Wert von <span class='formula'>93,5 g CO₂/km</span> basiert auf der <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a> und berechnet sich aus dem Leergewicht der Fahrzeuges in Tonnen (<span class='formula'>2,21 t</span>), dem CO₂-Ausstoß bei der Produktion von PKWs  (<span class='formula'>5.5 t CO₂ / t</span>) und der durchschnittlichen Lebensdauer des PKW in Kilometern (<span class='formula'>130.000 km</span>) wie folgt:<br />
                <span class='formula'>CO₂ Produktion = (2,21 t * 5.500.000 g CO₂/t) / 130.000 km</span>
            <h3>Abgase</h3>
            Die Verbrennung von Treibstoffen zum Antrieb eines Fahrzeugmotors verursacht Abgase, welche unter anderem auch CO₂ beinhalten. Der verwendete Wert von <span class='formula'>358,0 g CO₂/km</span> basiert auf einer Liste des <a href="hhttps://www.energy.eu/car-co2-emissions/">European Energy Portal</a>.
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (53,04 g CO₂/km + 93,5 g CO₂/km + 358,0 g CO₂/km)</span>
        ''',
        },# Porsche Cayenne Turbo https://www.energy.eu/car-co2-emissions/porsche.php; 50 g/km production/disposal
    'pt_subway_double': {
        'title': 'UBahn (Wiener Linien, 200%)',
        'emissions_fuel': 12.0,
        'emissions_tailpipe': 0.0,
        'emissions_prod': 16.0,
        'info': '''
            <h2>UBahn (Wiener Linien)</h2>
            <h3>Elektrizität</h3>
            Die Wiener Ubahn verbraucht Strom, welcher je nach Erzeugungsart unterschiedlichen CO₂-Ausstoß verursacht. Je mehr Strom aus Wind- und Wasserkraft (mit geringem CO₂-Ausstoss) bezogen werden kann, desto weniger Strom wird aus Gas-, Biomasse- und Kohlekraftwerken erzeugt oder zugekauft.<br />
            Der tatsächliche CO₂-Ausstoß errechnet sich aus dem Stromverbrauch pro km und der Passagieranzahl; der hier verwendete Wert von <span class='formula'>12,0 g CO₂/km</span> geht von einer übervollen Auslastung (<span class='formula'>200%</span>) der U-Bahn aus (alle Sitze besetzt, weitere Passagiere müssen stehen) und basiert auf einer <a href="https://www.wienerlinien.at/media/files/2014/wl_oekologischer_fussabdruck_54089.pdf">Informationsbroschüre der Wiener Linien</a>.
            <h3>Produktion</h3>
            Die Produktion einer U-Bahn erfodert signifikante Resourcen, wird jedoch durch die lange Lebensdauer und hohe Passagieranzahl stark relativiert. Der verwendete Wert von <span class='formula'>16 g CO₂/km</span> pro Passagier basiert auf der Schätzung der <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a>
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (12,0 g CO₂/km + 16,0 g CO₂/km)</span>
        ''',
        },# source: Wiener Linien 12.0, ECF
    'pt_subway_full': {
        'title': 'UBahn (Wiener Linien, 100%)',
        'emissions_fuel': 24.0,
        'emissions_tailpipe': 0.0,
        'emissions_prod': 16.0,
        'info': '''
            <h2>UBahn (Wiener Linien)</h2>
            <h3>Elektrizität</h3>
            Die Wiener Ubahn verbraucht Strom, welcher je nach Erzeugungsart unterschiedlichen CO₂-Ausstoß verursacht. Je mehr Strom aus Wind- und Wasserkraft (mit geringem CO₂-Ausstoss) bezogen werden kann, desto weniger Strom wird aus Gas-, Biomasse- und Kohlekraftwerken erzeugt oder zugekauft.<br />
            Der tatsächliche CO₂-Ausstoß errechnet sich aus dem Stromverbrauch pro km und der Passagieranzahl; der hier verwendete Wert von <span class='formula'>24,0 g CO₂/km</span> geht von einer vollen Auslastung (<span class='formula'>100%</span>) der U-Bahn aus (alle Sitze besetzt) und basiert auf einer <a href="https://www.wienerlinien.at/media/files/2014/wl_oekologischer_fussabdruck_54089.pdf">Informationsbroschüre der Wiener Linien</a>.
            <h3>Produktion</h3>
            Die Produktion einer U-Bahn erfodert signifikante Resourcen, wird jedoch durch die lange Lebensdauer und hohe Passagieranzahl stark relativiert. Der verwendete Wert von <span class='formula'>16 g CO₂/km</span> pro Passagier basiert auf der Schätzung der <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a>
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (24,0 g CO₂/km + 16,0 g CO₂/km)</span>
        ''',
        },# source: Wiener Linien 12.0, ECF
    'pt_subway_average': {
        'title': 'UBahn (Wiener Linien, 40%)',
        'emissions_fuel': 60,
        'emissions_tailpipe': 0.0,
        'emissions_prod': 16.0,
        'info': '''
            <h2>UBahn (Wiener Linien)</h2>
            <h3>Elektrizität</h3>
            Die Wiener Ubahn verbraucht Strom, welcher je nach Erzeugungsart unterschiedlichen CO₂-Ausstoß verursacht. Je mehr Strom aus Wind- und Wasserkraft (mit geringem CO₂-Ausstoss) bezogen werden kann, desto weniger Strom wird aus Gas-, Biomasse- und Kohlekraftwerken erzeugt oder zugekauft.<br />
            Der tatsächliche CO₂-Ausstoß errechnet sich aus dem Stromverbrauch pro km und der Passagieranzahl; der hier verwendete Wert von <span class='formula'>60 g CO₂/km</span> geht von einer durchschnittlichen Auslastung (<span class='formula'>40%</span>) der U-Bahn aus (40\% der Sitze besetzt) und basiert auf einer <a href="https://www.wienerlinien.at/media/files/2014/wl_oekologischer_fussabdruck_54089.pdf">Informationsbroschüre der Wiener Linien</a>.
            <h3>Produktion</h3>
            Die Produktion einer U-Bahn erfodert signifikante Resourcen, wird jedoch durch die lange Lebensdauer und hohe Passagieranzahl stark relativiert. Der verwendete Wert von <span class='formula'>16 g CO₂/km</span> pro Passagier basiert auf der Schätzung der <a href="https://ecf.com/sites/ecf.com/files/ECF_CO2_WEB.pdf">Studie der European Cyclist Federation</a>
            <h3>Berechnung</h3>
            <span class='formula'>CO₂ Fußabdruck = Distanz * (60,0 g CO₂/km + 16,0 g CO₂/km)</span>
        ''',
        },# source: Wiener Linien 12.0, ECF
}