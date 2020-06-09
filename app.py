from flask import Flask, jsonify
import requests

app = Flask(__name__)

aoe_2_net_api_base_url = 'https://aoe2.net/api/'
el_gordo_valor_steam_id = '76561198053912147'

maps_ids = {
    9: 'Arabia',
    10: 'Archipelago',
    11: 'Baltic',
    12: 'Black Forest',
    13: 'Coastal',
    14: 'Continental',
    15: 'Crater Lake',
    16: 'Fortress',
    17: 'Gold Rush',
    18: 'Highland',
    19: 'Islands',
    20: 'Mediterranean',
    21: 'Migration',
    22: 'Rivers',
    23: 'Team Islands',
    24: 'Full Random',
    25: 'Scandinavia',
    26: 'Mongolia',
    27: 'Yucatan',
    28: 'Salt Marsh',
    29: 'Arena',
    31: 'Oasis',
    32: 'Ghost Lake',
    33: 'Nomad',
    49: 'Iberia',
    50: 'Britain',
    51: 'Mideast',
    52: 'Texas',
    53: 'Italy',
    54: 'Central America',
    55: 'France',
    56: 'Norse Lands',
    57: 'Sea of Japan (East Sea)',
    58: 'Byzantium',
    59: 'Custom',
    60: 'Random Land Map',
    62: 'Random Real World Map',
    63: 'Blind Random',
    65: 'Random Special Map',
    66: 'Random Special Map',
    67: 'Acropolis',
    68: 'Budapest',
    69: 'Cenotes',
    70: 'City of Lakes',
    71: 'Golden Pit',
    72: 'Hideout',
    73: 'Hill Fort',
    74: 'Lombardia',
    75: 'Steppe',
    76: 'Valley',
    77: 'MegaRandom',
    78: 'Hamburger',
    79: 'CtR Random',
    80: 'CtR Monsoon',
    81: 'CtR Pyramid Descent',
    82: 'CtR Spiral',
    83: 'Kilimanjaro',
    84: 'Mountain Pass',
    85: 'Nile Delta',
    86: 'Serengeti',
    87: 'Socotra',
    88: 'Amazon',
    89: 'China',
    90: 'Horn of Africa',
    91: 'India',
    92: 'Madagascar',
    93: 'West Africa',
    94: 'Bohemia',
    95: 'Earth',
    96: 'Canyons',
    97: 'Enemy Archipelago',
    98: 'Enemy Islands',
    99: 'Far Out',
    100: 'Front Line',
    101: 'Inner Circle',
    102: 'Motherland',
    103: 'Open Plains',
    104: 'Ring of Water',
    105: 'Snakepit',
    106: 'The Eye',
    107: 'Australia',
    108: 'Indochina',
    109: 'Indonesia',
    110: 'Strait of Malacca',
    111: 'Philippines',
    112: 'Bog Islands',
    113: 'Mangrove Jungle',
    114: 'Pacific Islands',
    115: 'Sandbank',
    116: 'Water Nomad',
    117: 'Jungle Islands',
    118: 'Holy Line',
    119: 'Border Stones',
    120: 'Yin Yang',
    121: 'Jungle Lanes',
    122: 'Alpine Lakes',
    123: 'Bogland',
    124: 'Mountain Ridge',
    125: 'Ravines',
    126: 'Wolf Hill',
    132: 'Antarctica',
    137: 'Custom Map Pool',
    139: 'Golden Swamp',
    140: 'Four Lakes'
}

civs_ids = {
    0: "Aztecs",
    1: "Berbers",
    2: "Britons",
    3: "Bulgarians",
    4: "Burmese",
    5: "Byzantines",
    6: "Celts",
    7: "Chinese",
    8: "Cumans",
    9: "Ethiopians",
    10: "Franks",
    11: "Goths",
    12: "Huns",
    13: "Incas",
    14: "Indians",
    15: "Italians",
    16: "Japanese",
    17: "Khmer",
    18: "Koreans",
    19: "Lithuanians",
    20: "Magyars",
    21: "Malay",
    22: "Malians",
    23: "Mayans",
    24: "Mongols",
    25: "Persians",
    26: "Portuguese",
    27: "Saracens",
    28: "Slavs",
    29: "Spanish",
    30: "Tatars",
    31: "Teutons",
    32: "Turks",
    33: "Vietnamese",
    34: "Vikings"
}


def civ_winrate():
    return {
    "Aztecs": {"wins": 0, "loses": 0},
    "Berbers": {"wins": 0, "loses": 0},
    "Britons": {"wins": 0, "loses": 0},
    "Bulgarians": {"wins": 0, "loses": 0},
    "Burmese": {"wins": 0, "loses": 0},
    "Byzantines": {"wins": 0, "loses": 0},
    "Celts": {"wins": 0, "loses": 0},
    "Chinese": {"wins": 0, "loses": 0},
    "Cumans": {"wins": 0, "loses": 0},
    "Ethiopians": {"wins": 0, "loses": 0},
    "Franks": {"wins": 0, "loses": 0},
    "Goths": {"wins": 0, "loses": 0},
    "Huns": {"wins": 0, "loses": 0},
    "Incas": {"wins": 0, "loses": 0},
    "Indians": {"wins": 0, "loses": 0},
    "Italians": {"wins": 0, "loses": 0},
    "Japanese": {"wins": 0, "loses": 0},
    "Khmer": {"wins": 0, "loses": 0},
    "Koreans": {"wins": 0, "loses": 0},
    "Lithuanians": {"wins": 0, "loses": 0},
    "Magyars": {"wins": 0, "loses": 0},
    "Malay": {"wins": 0, "loses": 0},
    "Malians": {"wins": 0, "loses": 0},
    "Mayans": {"wins": 0, "loses": 0},
    "Mongols": {"wins": 0, "loses": 0},
    "Persians": {"wins": 0, "loses": 0},
    "Portuguese": {"wins": 0, "loses": 0},
    "Saracens": {"wins": 0, "loses": 0},
    "Slavs": {"wins": 0, "loses": 0},
    "Spanish": {"wins": 0, "loses": 0},
    "Tatars": {"wins": 0, "loses": 0},
    "Teutons": {"wins": 0, "loses": 0},
    "Turks": {"wins": 0, "loses": 0},
    "Vietnamese": {"wins": 0, "loses": 0},
    "Vikings": {"wins": 0, "loses": 0}
}

stats = {
    'Arabia': civ_winrate(),
    'Archipelago': civ_winrate(),
    'Baltic': civ_winrate(),
    'Black Forest': civ_winrate(),
    'Coastal': civ_winrate(),
    'Continental': civ_winrate(),
    'Crater Lake': civ_winrate(),
    'Fortress': civ_winrate(),
    'Gold Rush': civ_winrate(),
    'Highland': civ_winrate(),
    'Islands': civ_winrate(),
    'Mediterranean': civ_winrate(),
    'Migration': civ_winrate(),
    'Rivers': civ_winrate(),
    'Team Islands': civ_winrate(),
    'Scandinavia': civ_winrate(),
    'Mongolia': civ_winrate(),
    'Yucatan': civ_winrate(),
    'Salt Marsh': civ_winrate(),
    'Arena': civ_winrate(),
    'Oasis': civ_winrate(),
    'Ghost Lake': civ_winrate(),
    'Nomad': civ_winrate(),
    'Acropolis': civ_winrate(),
    'Budapest': civ_winrate(),
    'Cenotes': civ_winrate(),
    'City of Lakes': civ_winrate(),
    'Golden Pit': civ_winrate(),
    'Hideout': civ_winrate(),
    'Hill Fort': civ_winrate(),
    'Lombardia': civ_winrate(),
    'Steppe': civ_winrate(),
    'Valley': civ_winrate(),
    'MegaRandom': civ_winrate(),
    'Hamburger': civ_winrate(),
    'Kilimanjaro': civ_winrate(),
    'Mountain Pass': civ_winrate(),
    'Nile Delta': civ_winrate(),
    'Serengeti': civ_winrate(),
    'Socotra': civ_winrate(),
    'Sandbank': civ_winrate(),
    'Water Nomad': civ_winrate(),
    'Alpine Lakes': civ_winrate(),
    'Bogland': civ_winrate(),
    'Mountain Ridge': civ_winrate(),
    'Ravines': civ_winrate(),
    'Wolf Hill': civ_winrate(),
    'Golden Swamp': civ_winrate(),
    'Four Lakes': civ_winrate()
}

weekly_maps = ['Arabia', 'Black Forest', 'Arena', 'Nomad', 'Scandinavia', 'Hill Fort', 'Lombardia', 'MegaRandom', 'Wolf Hill']

filled_stats = {"Acropolis":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Alpine Lakes":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Arabia":{"Aztecs":{"loses":627,"wins":645},"Berbers":{"loses":256,"wins":292},"Britons":{"loses":1077,"wins":1126},"Bulgarians":{"loses":414,"wins":373},"Burmese":{"loses":181,"wins":143},"Byzantines":{"loses":271,"wins":276},"Celts":{"loses":342,"wins":351},"Chinese":{"loses":475,"wins":440},"Cumans":{"loses":399,"wins":366},"Ethiopians":{"loses":759,"wins":837},"Franks":{"loses":1619,"wins":1825},"Goths":{"loses":790,"wins":859},"Huns":{"loses":828,"wins":918},"Incas":{"loses":261,"wins":322},"Indians":{"loses":319,"wins":332},"Italians":{"loses":133,"wins":151},"Japanese":{"loses":296,"wins":272},"Khmer":{"loses":589,"wins":509},"Koreans":{"loses":162,"wins":120},"Lithuanians":{"loses":544,"wins":611},"Magyars":{"loses":770,"wins":846},"Malay":{"loses":134,"wins":125},"Malians":{"loses":175,"wins":181},"Mayans":{"loses":1333,"wins":1410},"Mongols":{"loses":1109,"wins":1024},"Persians":{"loses":770,"wins":821},"Portuguese":{"loses":152,"wins":96},"Saracens":{"loses":343,"wins":284},"Slavs":{"loses":264,"wins":302},"Spanish":{"loses":465,"wins":468},"Tatars":{"loses":278,"wins":273},"Teutons":{"loses":528,"wins":545},"Turks":{"loses":178,"wins":143},"Vietnamese":{"loses":433,"wins":455},"Vikings":{"loses":436,"wins":442}},"Archipelago":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Arena":{"Aztecs":{"loses":540,"wins":559},"Berbers":{"loses":153,"wins":126},"Britons":{"loses":1155,"wins":1131},"Bulgarians":{"loses":277,"wins":287},"Burmese":{"loses":164,"wins":151},"Byzantines":{"loses":326,"wins":225},"Celts":{"loses":450,"wins":494},"Chinese":{"loses":352,"wins":371},"Cumans":{"loses":401,"wins":414},"Ethiopians":{"loses":353,"wins":286},"Franks":{"loses":1042,"wins":1100},"Goths":{"loses":1035,"wins":1282},"Huns":{"loses":356,"wins":322},"Incas":{"loses":161,"wins":167},"Indians":{"loses":284,"wins":231},"Italians":{"loses":154,"wins":136},"Japanese":{"loses":186,"wins":185},"Khmer":{"loses":865,"wins":966},"Koreans":{"loses":132,"wins":137},"Lithuanians":{"loses":475,"wins":466},"Magyars":{"loses":259,"wins":242},"Malay":{"loses":142,"wins":126},"Malians":{"loses":123,"wins":111},"Mayans":{"loses":771,"wins":762},"Mongols":{"loses":823,"wins":784},"Persians":{"loses":675,"wins":598},"Portuguese":{"loses":177,"wins":129},"Saracens":{"loses":214,"wins":169},"Slavs":{"loses":355,"wins":314},"Spanish":{"loses":556,"wins":626},"Tatars":{"loses":135,"wins":115},"Teutons":{"loses":528,"wins":574},"Turks":{"loses":516,"wins":526},"Vietnamese":{"loses":335,"wins":293},"Vikings":{"loses":277,"wins":315}},"Baltic":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Black Forest":{"Aztecs":{"loses":111,"wins":142},"Berbers":{"loses":46,"wins":52},"Britons":{"loses":528,"wins":561},"Bulgarians":{"loses":82,"wins":88},"Burmese":{"loses":48,"wins":47},"Byzantines":{"loses":107,"wins":91},"Celts":{"loses":378,"wins":451},"Chinese":{"loses":113,"wins":158},"Cumans":{"loses":100,"wins":122},"Ethiopians":{"loses":131,"wins":155},"Franks":{"loses":292,"wins":350},"Goths":{"loses":325,"wins":453},"Huns":{"loses":100,"wins":121},"Incas":{"loses":72,"wins":69},"Indians":{"loses":70,"wins":82},"Italians":{"loses":54,"wins":56},"Japanese":{"loses":56,"wins":73},"Khmer":{"loses":372,"wins":412},"Koreans":{"loses":97,"wins":90},"Lithuanians":{"loses":116,"wins":128},"Magyars":{"loses":100,"wins":126},"Malay":{"loses":30,"wins":58},"Malians":{"loses":38,"wins":31},"Mayans":{"loses":178,"wins":239},"Mongols":{"loses":449,"wins":447},"Persians":{"loses":206,"wins":248},"Portuguese":{"loses":58,"wins":72},"Saracens":{"loses":74,"wins":80},"Slavs":{"loses":98,"wins":102},"Spanish":{"loses":189,"wins":213},"Tatars":{"loses":41,"wins":50},"Teutons":{"loses":204,"wins":236},"Turks":{"loses":173,"wins":189},"Vietnamese":{"loses":110,"wins":101},"Vikings":{"loses":90,"wins":121}},"Bogland":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Budapest":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Cenotes":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"City of Lakes":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Coastal":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Continental":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Crater Lake":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Fortress":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Four Lakes":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Ghost Lake":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Gold Rush":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Golden Pit":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Golden Swamp":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Hamburger":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Hideout":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Highland":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Hill Fort":{"Aztecs":{"loses":267,"wins":317},"Berbers":{"loses":156,"wins":138},"Britons":{"loses":620,"wins":715},"Bulgarians":{"loses":206,"wins":220},"Burmese":{"loses":124,"wins":101},"Byzantines":{"loses":145,"wins":154},"Celts":{"loses":210,"wins":218},"Chinese":{"loses":223,"wins":234},"Cumans":{"loses":264,"wins":302},"Ethiopians":{"loses":290,"wins":304},"Franks":{"loses":671,"wins":768},"Goths":{"loses":517,"wins":608},"Huns":{"loses":337,"wins":411},"Incas":{"loses":139,"wins":165},"Indians":{"loses":171,"wins":177},"Italians":{"loses":84,"wins":65},"Japanese":{"loses":165,"wins":129},"Khmer":{"loses":352,"wins":394},"Koreans":{"loses":71,"wins":79},"Lithuanians":{"loses":295,"wins":356},"Magyars":{"loses":246,"wins":252},"Malay":{"loses":91,"wins":77},"Malians":{"loses":81,"wins":92},"Mayans":{"loses":545,"wins":652},"Mongols":{"loses":552,"wins":622},"Persians":{"loses":391,"wins":356},"Portuguese":{"loses":62,"wins":79},"Saracens":{"loses":191,"wins":198},"Slavs":{"loses":155,"wins":169},"Spanish":{"loses":334,"wins":345},"Tatars":{"loses":214,"wins":191},"Teutons":{"loses":353,"wins":392},"Turks":{"loses":180,"wins":147},"Vietnamese":{"loses":228,"wins":189},"Vikings":{"loses":207,"wins":239}},"Islands":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Kilimanjaro":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Lombardia":{"Aztecs":{"loses":309,"wins":280},"Berbers":{"loses":131,"wins":157},"Britons":{"loses":629,"wins":678},"Bulgarians":{"loses":238,"wins":232},"Burmese":{"loses":107,"wins":82},"Byzantines":{"loses":172,"wins":144},"Celts":{"loses":217,"wins":204},"Chinese":{"loses":241,"wins":216},"Cumans":{"loses":245,"wins":211},"Ethiopians":{"loses":348,"wins":391},"Franks":{"loses":891,"wins":1014},"Goths":{"loses":525,"wins":555},"Huns":{"loses":366,"wins":442},"Incas":{"loses":126,"wins":149},"Indians":{"loses":206,"wins":262},"Italians":{"loses":97,"wins":79},"Japanese":{"loses":155,"wins":142},"Khmer":{"loses":357,"wins":383},"Koreans":{"loses":95,"wins":69},"Lithuanians":{"loses":275,"wins":324},"Magyars":{"loses":378,"wins":426},"Malay":{"loses":112,"wins":83},"Malians":{"loses":105,"wins":97},"Mayans":{"loses":606,"wins":663},"Mongols":{"loses":621,"wins":669},"Persians":{"loses":490,"wins":445},"Portuguese":{"loses":91,"wins":64},"Saracens":{"loses":164,"wins":171},"Slavs":{"loses":143,"wins":158},"Spanish":{"loses":320,"wins":301},"Tatars":{"loses":176,"wins":175},"Teutons":{"loses":310,"wins":319},"Turks":{"loses":117,"wins":121},"Vietnamese":{"loses":214,"wins":223},"Vikings":{"loses":211,"wins":228}},"Mediterranean":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"MegaRandom":{"Aztecs":{"loses":188,"wins":225},"Berbers":{"loses":108,"wins":120},"Britons":{"loses":383,"wins":354},"Bulgarians":{"loses":138,"wins":156},"Burmese":{"loses":70,"wins":90},"Byzantines":{"loses":153,"wins":134},"Celts":{"loses":183,"wins":124},"Chinese":{"loses":180,"wins":192},"Cumans":{"loses":159,"wins":140},"Ethiopians":{"loses":187,"wins":210},"Franks":{"loses":444,"wins":531},"Goths":{"loses":374,"wins":408},"Huns":{"loses":293,"wins":315},"Incas":{"loses":125,"wins":133},"Indians":{"loses":120,"wins":142},"Italians":{"loses":98,"wins":95},"Japanese":{"loses":185,"wins":172},"Khmer":{"loses":264,"wins":232},"Koreans":{"loses":75,"wins":76},"Lithuanians":{"loses":224,"wins":234},"Magyars":{"loses":273,"wins":254},"Malay":{"loses":100,"wins":89},"Malians":{"loses":102,"wins":81},"Mayans":{"loses":400,"wins":441},"Mongols":{"loses":541,"wins":618},"Persians":{"loses":460,"wins":406},"Portuguese":{"loses":91,"wins":95},"Saracens":{"loses":115,"wins":98},"Slavs":{"loses":101,"wins":112},"Spanish":{"loses":199,"wins":211},"Tatars":{"loses":119,"wins":106},"Teutons":{"loses":205,"wins":230},"Turks":{"loses":80,"wins":101},"Vietnamese":{"loses":161,"wins":156},"Vikings":{"loses":335,"wins":354}},"Migration":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Mongolia":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Mountain Pass":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Mountain Ridge":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Nile Delta":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Nomad":{"Aztecs":{"loses":121,"wins":111},"Berbers":{"loses":61,"wins":88},"Britons":{"loses":208,"wins":171},"Bulgarians":{"loses":110,"wins":131},"Burmese":{"loses":48,"wins":37},"Byzantines":{"loses":74,"wins":66},"Celts":{"loses":118,"wins":104},"Chinese":{"loses":230,"wins":204},"Cumans":{"loses":140,"wins":129},"Ethiopians":{"loses":103,"wins":116},"Franks":{"loses":269,"wins":254},"Goths":{"loses":252,"wins":212},"Huns":{"loses":247,"wins":219},"Incas":{"loses":106,"wins":119},"Indians":{"loses":80,"wins":91},"Italians":{"loses":110,"wins":122},"Japanese":{"loses":255,"wins":257},"Khmer":{"loses":127,"wins":122},"Koreans":{"loses":113,"wins":97},"Lithuanians":{"loses":136,"wins":149},"Magyars":{"loses":135,"wins":122},"Malay":{"loses":136,"wins":114},"Malians":{"loses":155,"wins":174},"Mayans":{"loses":248,"wins":256},"Mongols":{"loses":278,"wins":254},"Persians":{"loses":684,"wins":660},"Portuguese":{"loses":82,"wins":82},"Saracens":{"loses":61,"wins":62},"Slavs":{"loses":61,"wins":53},"Spanish":{"loses":178,"wins":170},"Tatars":{"loses":62,"wins":50},"Teutons":{"loses":103,"wins":123},"Turks":{"loses":36,"wins":33},"Vietnamese":{"loses":157,"wins":149},"Vikings":{"loses":244,"wins":259}},"Oasis":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Ravines":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Rivers":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Salt Marsh":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Sandbank":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Scandinavia":{"Aztecs":{"loses":342,"wins":321},"Berbers":{"loses":175,"wins":212},"Britons":{"loses":627,"wins":720},"Bulgarians":{"loses":226,"wins":260},"Burmese":{"loses":108,"wins":107},"Byzantines":{"loses":176,"wins":195},"Celts":{"loses":309,"wins":293},"Chinese":{"loses":236,"wins":256},"Cumans":{"loses":215,"wins":212},"Ethiopians":{"loses":356,"wins":430},"Franks":{"loses":823,"wins":986},"Goths":{"loses":638,"wins":819},"Huns":{"loses":411,"wins":471},"Incas":{"loses":160,"wins":215},"Indians":{"loses":213,"wins":242},"Italians":{"loses":174,"wins":212},"Japanese":{"loses":444,"wins":514},"Khmer":{"loses":346,"wins":387},"Koreans":{"loses":89,"wins":105},"Lithuanians":{"loses":355,"wins":373},"Magyars":{"loses":377,"wins":413},"Malay":{"loses":212,"wins":238},"Malians":{"loses":107,"wins":154},"Mayans":{"loses":665,"wins":708},"Mongols":{"loses":1525,"wins":1813},"Persians":{"loses":555,"wins":580},"Portuguese":{"loses":93,"wins":86},"Saracens":{"loses":179,"wins":179},"Slavs":{"loses":176,"wins":210},"Spanish":{"loses":252,"wins":288},"Tatars":{"loses":154,"wins":165},"Teutons":{"loses":390,"wins":435},"Turks":{"loses":134,"wins":108},"Vietnamese":{"loses":285,"wins":245},"Vikings":{"loses":516,"wins":574}},"Serengeti":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Socotra":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Steppe":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Team Islands":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Valley":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Water Nomad":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Wolf Hill":{"Aztecs":{"loses":624,"wins":670},"Berbers":{"loses":47,"wins":54},"Britons":{"loses":295,"wins":380},"Bulgarians":{"loses":93,"wins":93},"Burmese":{"loses":38,"wins":54},"Byzantines":{"loses":54,"wins":52},"Celts":{"loses":97,"wins":83},"Chinese":{"loses":80,"wins":71},"Cumans":{"loses":69,"wins":56},"Ethiopians":{"loses":149,"wins":159},"Franks":{"loses":276,"wins":335},"Goths":{"loses":222,"wins":244},"Huns":{"loses":112,"wins":136},"Incas":{"loses":67,"wins":75},"Indians":{"loses":77,"wins":85},"Italians":{"loses":38,"wins":26},"Japanese":{"loses":58,"wins":62},"Khmer":{"loses":117,"wins":125},"Koreans":{"loses":49,"wins":50},"Lithuanians":{"loses":621,"wins":716},"Magyars":{"loses":200,"wins":244},"Malay":{"loses":39,"wins":38},"Malians":{"loses":37,"wins":32},"Mayans":{"loses":220,"wins":242},"Mongols":{"loses":221,"wins":265},"Persians":{"loses":131,"wins":113},"Portuguese":{"loses":29,"wins":34},"Saracens":{"loses":64,"wins":63},"Slavs":{"loses":52,"wins":61},"Spanish":{"loses":102,"wins":98},"Tatars":{"loses":77,"wins":83},"Teutons":{"loses":127,"wins":131},"Turks":{"loses":42,"wins":47},"Vietnamese":{"loses":74,"wins":84},"Vikings":{"loses":75,"wins":89}},"Yucatan":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}}}


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/gordo_valor_rank')
def gvalorrank():
    rank = get_gordo_valor_tg_rank()
    return jsonify(rank)


def get_gordo_valor_tg_rank():
    # url = aoe_2_net_api_base_url + 'leaderboard?game=aoe2de&leaderboard_id=4&steam_id=' + el_gordo_valor_steam_id + '&count=1'
    # response = requests.get(url=url)
    # response_json = response.json()
    # leaderboard = response_json['leaderboard']
    # rank = leaderboard[0]["rank"]
    return 14968


def get_upper_bound(rank):
    return rank - 5000


@app.route('/neighbours')
def get_gordo_valor_neighbours_ids_api():
    return jsonify(get_gordo_valor_neighbours_ids())


def get_gordo_valor_neighbours_ids():
    rank = get_gordo_valor_tg_rank()
    upper_bound = rank - 5000
    url = aoe_2_net_api_base_url + 'leaderboard?game=aoe2de&leaderboard_id=4&start=' + str(upper_bound) + '&count=10000'
    response = requests.get(url=url)
    response_json = response.json()
    leaderboard = response_json['leaderboard']
    ids = []
    for player in leaderboard:
        player_id = player['steam_id']
        ids.append(player_id)
    return ids


@app.route('/current_stats')
def get_current_stats():
    return jsonify(stats)


@app.route('/stats')
def fill_stats_with_neighbours_data():
    print("arrancose")
    neighbours_ids = get_gordo_valor_neighbours_ids()
    iteration = 0
    print(str(len(neighbours_ids)))
    for neighbour_id in neighbours_ids:
        iteration += 1
        if iteration % 100 == 0:
            print(str(iteration))
        if neighbour_id is not None:
            try:
                url = aoe_2_net_api_base_url + 'player/matches?game=aoe2de&steam_id=' + str(neighbour_id) + '&count=50'
                response = requests.get(url=url)
                matches = response.json()
                for match in matches:
                    if match["leaderboard_id"] == 4 and maps_ids[match["map_type"]] in weekly_maps:
                        map_name = maps_ids[match["map_type"]]
                        players = match["players"]
                        for player in players:
                            if player["steam_id"] == str(neighbour_id):
                                civ_name = civs_ids[player["civ"]]
                                if player["won"]:
                                    stats[map_name][civ_name]["wins"] += 1
                                else:
                                    stats[map_name][civ_name]["loses"] += 1
            except:
                print("pincho la wea para el wachin con id: " + str(neighbour_id))
    return jsonify(stats)


@app.route('/stats/map/<map_name>')
def get_stats_for_map(map_name):
    map_stats = filled_stats[map_name]
    winrates = []
    for civilization_name in map_stats:
        civilization_stats = map_stats[civilization_name]
        total_played = (civilization_stats["wins"] + civilization_stats["loses"])
        winrate = (civilization_stats["wins"] / total_played )*100
        winrates.append((civilization_name, winrate, total_played))
    sorted_winrates = sorted(winrates, key=lambda x: x[1], reverse=True)
    return_text = "<b>" + map_name + " Winrates </b> <br/><ol>"
    for civilization_winrate in sorted_winrates:
        return_text += "<li>" + civilization_winrate[0] + ": " + str(round(civilization_winrate[1], 2)) + "% (matches picked: " + str(civilization_winrate[2]) + ")</li>"
    return return_text


if __name__ == '__main__':
    app.run()
