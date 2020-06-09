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

filled_stats = {"Acropolis":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Alpine Lakes":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Arabia":{"Aztecs":{"loses":800,"wins":816},"Berbers":{"loses":343,"wins":356},"Britons":{"loses":1393,"wins":1477},"Bulgarians":{"loses":511,"wins":485},"Burmese":{"loses":221,"wins":197},"Byzantines":{"loses":361,"wins":364},"Celts":{"loses":445,"wins":464},"Chinese":{"loses":625,"wins":559},"Cumans":{"loses":530,"wins":475},"Ethiopians":{"loses":946,"wins":1055},"Franks":{"loses":2076,"wins":2359},"Goths":{"loses":1065,"wins":1176},"Huns":{"loses":1029,"wins":1167},"Incas":{"loses":343,"wins":403},"Indians":{"loses":404,"wins":431},"Italians":{"loses":160,"wins":175},"Japanese":{"loses":403,"wins":389},"Khmer":{"loses":763,"wins":675},"Koreans":{"loses":203,"wins":149},"Lithuanians":{"loses":699,"wins":780},"Magyars":{"loses":979,"wins":1084},"Malay":{"loses":149,"wins":155},"Malians":{"loses":220,"wins":222},"Mayans":{"loses":1717,"wins":1803},"Mongols":{"loses":1428,"wins":1314},"Persians":{"loses":1008,"wins":1028},"Portuguese":{"loses":206,"wins":132},"Saracens":{"loses":418,"wins":348},"Slavs":{"loses":351,"wins":397},"Spanish":{"loses":611,"wins":629},"Tatars":{"loses":359,"wins":328},"Teutons":{"loses":654,"wins":701},"Turks":{"loses":230,"wins":199},"Vietnamese":{"loses":552,"wins":597},"Vikings":{"loses":550,"wins":549}},"Archipelago":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Arena":{"Aztecs":{"loses":664,"wins":694},"Berbers":{"loses":212,"wins":157},"Britons":{"loses":1429,"wins":1407},"Bulgarians":{"loses":334,"wins":348},"Burmese":{"loses":194,"wins":201},"Byzantines":{"loses":428,"wins":322},"Celts":{"loses":583,"wins":618},"Chinese":{"loses":455,"wins":489},"Cumans":{"loses":540,"wins":549},"Ethiopians":{"loses":487,"wins":401},"Franks":{"loses":1386,"wins":1463},"Goths":{"loses":1394,"wins":1687},"Huns":{"loses":455,"wins":412},"Incas":{"loses":222,"wins":228},"Indians":{"loses":369,"wins":296},"Italians":{"loses":192,"wins":174},"Japanese":{"loses":245,"wins":277},"Khmer":{"loses":1141,"wins":1252},"Koreans":{"loses":178,"wins":168},"Lithuanians":{"loses":595,"wins":618},"Magyars":{"loses":321,"wins":320},"Malay":{"loses":171,"wins":152},"Malians":{"loses":147,"wins":130},"Mayans":{"loses":975,"wins":968},"Mongols":{"loses":1031,"wins":992},"Persians":{"loses":862,"wins":756},"Portuguese":{"loses":227,"wins":175},"Saracens":{"loses":278,"wins":210},"Slavs":{"loses":465,"wins":423},"Spanish":{"loses":703,"wins":777},"Tatars":{"loses":172,"wins":142},"Teutons":{"loses":700,"wins":736},"Turks":{"loses":663,"wins":660},"Vietnamese":{"loses":437,"wins":398},"Vikings":{"loses":337,"wins":382}},"Baltic":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Black Forest":{"Aztecs":{"loses":144,"wins":190},"Berbers":{"loses":60,"wins":63},"Britons":{"loses":711,"wins":731},"Bulgarians":{"loses":105,"wins":112},"Burmese":{"loses":63,"wins":66},"Byzantines":{"loses":152,"wins":139},"Celts":{"loses":485,"wins":569},"Chinese":{"loses":175,"wins":205},"Cumans":{"loses":157,"wins":179},"Ethiopians":{"loses":173,"wins":226},"Franks":{"loses":408,"wins":498},"Goths":{"loses":476,"wins":634},"Huns":{"loses":142,"wins":172},"Incas":{"loses":93,"wins":96},"Indians":{"loses":95,"wins":110},"Italians":{"loses":81,"wins":85},"Japanese":{"loses":89,"wins":102},"Khmer":{"loses":510,"wins":570},"Koreans":{"loses":126,"wins":120},"Lithuanians":{"loses":150,"wins":161},"Magyars":{"loses":139,"wins":166},"Malay":{"loses":41,"wins":69},"Malians":{"loses":47,"wins":45},"Mayans":{"loses":256,"wins":305},"Mongols":{"loses":581,"wins":582},"Persians":{"loses":274,"wins":326},"Portuguese":{"loses":79,"wins":93},"Saracens":{"loses":101,"wins":99},"Slavs":{"loses":146,"wins":128},"Spanish":{"loses":269,"wins":298},"Tatars":{"loses":56,"wins":68},"Teutons":{"loses":278,"wins":329},"Turks":{"loses":232,"wins":243},"Vietnamese":{"loses":150,"wins":134},"Vikings":{"loses":116,"wins":162}},"Bogland":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Budapest":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Cenotes":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"City of Lakes":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Coastal":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Continental":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Crater Lake":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Fortress":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Four Lakes":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Ghost Lake":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Gold Rush":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Golden Pit":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Golden Swamp":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Hamburger":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Hideout":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Highland":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Hill Fort":{"Aztecs":{"loses":344,"wins":399},"Berbers":{"loses":186,"wins":190},"Britons":{"loses":779,"wins":886},"Bulgarians":{"loses":265,"wins":283},"Burmese":{"loses":162,"wins":126},"Byzantines":{"loses":211,"wins":205},"Celts":{"loses":258,"wins":266},"Chinese":{"loses":285,"wins":291},"Cumans":{"loses":345,"wins":388},"Ethiopians":{"loses":383,"wins":396},"Franks":{"loses":889,"wins":982},"Goths":{"loses":699,"wins":833},"Huns":{"loses":423,"wins":541},"Incas":{"loses":177,"wins":205},"Indians":{"loses":228,"wins":219},"Italians":{"loses":115,"wins":90},"Japanese":{"loses":205,"wins":175},"Khmer":{"loses":477,"wins":529},"Koreans":{"loses":88,"wins":105},"Lithuanians":{"loses":360,"wins":436},"Magyars":{"loses":302,"wins":324},"Malay":{"loses":115,"wins":95},"Malians":{"loses":100,"wins":107},"Mayans":{"loses":701,"wins":837},"Mongols":{"loses":688,"wins":756},"Persians":{"loses":492,"wins":463},"Portuguese":{"loses":90,"wins":96},"Saracens":{"loses":229,"wins":239},"Slavs":{"loses":197,"wins":222},"Spanish":{"loses":444,"wins":463},"Tatars":{"loses":270,"wins":225},"Teutons":{"loses":456,"wins":524},"Turks":{"loses":225,"wins":184},"Vietnamese":{"loses":305,"wins":250},"Vikings":{"loses":254,"wins":302}},"Islands":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Kilimanjaro":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Lombardia":{"Aztecs":{"loses":406,"wins":363},"Berbers":{"loses":188,"wins":213},"Britons":{"loses":816,"wins":868},"Bulgarians":{"loses":303,"wins":298},"Burmese":{"loses":137,"wins":111},"Byzantines":{"loses":233,"wins":187},"Celts":{"loses":275,"wins":258},"Chinese":{"loses":314,"wins":268},"Cumans":{"loses":337,"wins":282},"Ethiopians":{"loses":439,"wins":491},"Franks":{"loses":1137,"wins":1289},"Goths":{"loses":660,"wins":716},"Huns":{"loses":499,"wins":557},"Incas":{"loses":168,"wins":190},"Indians":{"loses":255,"wins":328},"Italians":{"loses":122,"wins":99},"Japanese":{"loses":218,"wins":206},"Khmer":{"loses":475,"wins":489},"Koreans":{"loses":116,"wins":86},"Lithuanians":{"loses":375,"wins":437},"Magyars":{"loses":478,"wins":528},"Malay":{"loses":135,"wins":106},"Malians":{"loses":133,"wins":115},"Mayans":{"loses":817,"wins":864},"Mongols":{"loses":781,"wins":846},"Persians":{"loses":608,"wins":543},"Portuguese":{"loses":122,"wins":87},"Saracens":{"loses":219,"wins":210},"Slavs":{"loses":199,"wins":214},"Spanish":{"loses":429,"wins":377},"Tatars":{"loses":225,"wins":223},"Teutons":{"loses":375,"wins":404},"Turks":{"loses":164,"wins":148},"Vietnamese":{"loses":290,"wins":301},"Vikings":{"loses":259,"wins":294}},"Mediterranean":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"MegaRandom":{"Aztecs":{"loses":255,"wins":279},"Berbers":{"loses":151,"wins":154},"Britons":{"loses":475,"wins":454},"Bulgarians":{"loses":180,"wins":184},"Burmese":{"loses":86,"wins":107},"Byzantines":{"loses":209,"wins":195},"Celts":{"loses":237,"wins":174},"Chinese":{"loses":245,"wins":249},"Cumans":{"loses":221,"wins":190},"Ethiopians":{"loses":245,"wins":257},"Franks":{"loses":589,"wins":702},"Goths":{"loses":459,"wins":528},"Huns":{"loses":383,"wins":398},"Incas":{"loses":155,"wins":162},"Indians":{"loses":154,"wins":182},"Italians":{"loses":126,"wins":126},"Japanese":{"loses":254,"wins":226},"Khmer":{"loses":349,"wins":310},"Koreans":{"loses":98,"wins":94},"Lithuanians":{"loses":292,"wins":293},"Magyars":{"loses":336,"wins":314},"Malay":{"loses":119,"wins":108},"Malians":{"loses":125,"wins":102},"Mayans":{"loses":526,"wins":602},"Mongols":{"loses":686,"wins":795},"Persians":{"loses":558,"wins":499},"Portuguese":{"loses":115,"wins":126},"Saracens":{"loses":141,"wins":128},"Slavs":{"loses":134,"wins":142},"Spanish":{"loses":271,"wins":284},"Tatars":{"loses":149,"wins":127},"Teutons":{"loses":263,"wins":281},"Turks":{"loses":103,"wins":119},"Vietnamese":{"loses":222,"wins":216},"Vikings":{"loses":419,"wins":434}},"Migration":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Mongolia":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Mountain Pass":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Mountain Ridge":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Nile Delta":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Nomad":{"Aztecs":{"loses":142,"wins":156},"Berbers":{"loses":87,"wins":106},"Britons":{"loses":271,"wins":220},"Bulgarians":{"loses":136,"wins":151},"Burmese":{"loses":64,"wins":47},"Byzantines":{"loses":104,"wins":94},"Celts":{"loses":148,"wins":131},"Chinese":{"loses":277,"wins":248},"Cumans":{"loses":191,"wins":178},"Ethiopians":{"loses":134,"wins":139},"Franks":{"loses":350,"wins":324},"Goths":{"loses":319,"wins":296},"Huns":{"loses":331,"wins":291},"Incas":{"loses":141,"wins":149},"Indians":{"loses":102,"wins":112},"Italians":{"loses":134,"wins":137},"Japanese":{"loses":332,"wins":315},"Khmer":{"loses":183,"wins":167},"Koreans":{"loses":139,"wins":128},"Lithuanians":{"loses":175,"wins":181},"Magyars":{"loses":168,"wins":146},"Malay":{"loses":174,"wins":141},"Malians":{"loses":190,"wins":198},"Mayans":{"loses":331,"wins":323},"Mongols":{"loses":357,"wins":315},"Persians":{"loses":819,"wins":788},"Portuguese":{"loses":110,"wins":101},"Saracens":{"loses":82,"wins":75},"Slavs":{"loses":76,"wins":69},"Spanish":{"loses":224,"wins":209},"Tatars":{"loses":78,"wins":60},"Teutons":{"loses":138,"wins":165},"Turks":{"loses":50,"wins":42},"Vietnamese":{"loses":213,"wins":190},"Vikings":{"loses":320,"wins":324}},"Oasis":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Ravines":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Rivers":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Salt Marsh":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Sandbank":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Scandinavia":{"Aztecs":{"loses":446,"wins":418},"Berbers":{"loses":219,"wins":265},"Britons":{"loses":794,"wins":917},"Bulgarians":{"loses":296,"wins":330},"Burmese":{"loses":144,"wins":147},"Byzantines":{"loses":249,"wins":266},"Celts":{"loses":386,"wins":359},"Chinese":{"loses":310,"wins":327},"Cumans":{"loses":299,"wins":290},"Ethiopians":{"loses":477,"wins":568},"Franks":{"loses":1097,"wins":1280},"Goths":{"loses":863,"wins":1068},"Huns":{"loses":558,"wins":624},"Incas":{"loses":208,"wins":285},"Indians":{"loses":273,"wins":312},"Italians":{"loses":223,"wins":253},"Japanese":{"loses":599,"wins":660},"Khmer":{"loses":483,"wins":521},"Koreans":{"loses":122,"wins":135},"Lithuanians":{"loses":457,"wins":474},"Magyars":{"loses":503,"wins":529},"Malay":{"loses":272,"wins":291},"Malians":{"loses":141,"wins":199},"Mayans":{"loses":870,"wins":930},"Mongols":{"loses":1893,"wins":2246},"Persians":{"loses":702,"wins":747},"Portuguese":{"loses":128,"wins":114},"Saracens":{"loses":224,"wins":235},"Slavs":{"loses":216,"wins":278},"Spanish":{"loses":380,"wins":400},"Tatars":{"loses":202,"wins":207},"Teutons":{"loses":491,"wins":554},"Turks":{"loses":171,"wins":137},"Vietnamese":{"loses":371,"wins":336},"Vikings":{"loses":670,"wins":723}},"Serengeti":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Socotra":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Steppe":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Team Islands":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Valley":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Water Nomad":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}},"Wolf Hill":{"Aztecs":{"loses":776,"wins":836},"Berbers":{"loses":61,"wins":68},"Britons":{"loses":390,"wins":506},"Bulgarians":{"loses":126,"wins":135},"Burmese":{"loses":44,"wins":67},"Byzantines":{"loses":76,"wins":86},"Celts":{"loses":126,"wins":102},"Chinese":{"loses":107,"wins":96},"Cumans":{"loses":91,"wins":76},"Ethiopians":{"loses":189,"wins":202},"Franks":{"loses":361,"wins":437},"Goths":{"loses":283,"wins":315},"Huns":{"loses":148,"wins":188},"Incas":{"loses":77,"wins":86},"Indians":{"loses":103,"wins":111},"Italians":{"loses":48,"wins":35},"Japanese":{"loses":79,"wins":82},"Khmer":{"loses":165,"wins":163},"Koreans":{"loses":57,"wins":67},"Lithuanians":{"loses":801,"wins":948},"Magyars":{"loses":251,"wins":304},"Malay":{"loses":44,"wins":43},"Malians":{"loses":44,"wins":42},"Mayans":{"loses":292,"wins":318},"Mongols":{"loses":267,"wins":334},"Persians":{"loses":159,"wins":144},"Portuguese":{"loses":42,"wins":39},"Saracens":{"loses":81,"wins":77},"Slavs":{"loses":64,"wins":76},"Spanish":{"loses":146,"wins":138},"Tatars":{"loses":97,"wins":112},"Teutons":{"loses":167,"wins":161},"Turks":{"loses":59,"wins":62},"Vietnamese":{"loses":97,"wins":98},"Vikings":{"loses":95,"wins":113}},"Yucatan":{"Aztecs":{"loses":0,"wins":0},"Berbers":{"loses":0,"wins":0},"Britons":{"loses":0,"wins":0},"Bulgarians":{"loses":0,"wins":0},"Burmese":{"loses":0,"wins":0},"Byzantines":{"loses":0,"wins":0},"Celts":{"loses":0,"wins":0},"Chinese":{"loses":0,"wins":0},"Cumans":{"loses":0,"wins":0},"Ethiopians":{"loses":0,"wins":0},"Franks":{"loses":0,"wins":0},"Goths":{"loses":0,"wins":0},"Huns":{"loses":0,"wins":0},"Incas":{"loses":0,"wins":0},"Indians":{"loses":0,"wins":0},"Italians":{"loses":0,"wins":0},"Japanese":{"loses":0,"wins":0},"Khmer":{"loses":0,"wins":0},"Koreans":{"loses":0,"wins":0},"Lithuanians":{"loses":0,"wins":0},"Magyars":{"loses":0,"wins":0},"Malay":{"loses":0,"wins":0},"Malians":{"loses":0,"wins":0},"Mayans":{"loses":0,"wins":0},"Mongols":{"loses":0,"wins":0},"Persians":{"loses":0,"wins":0},"Portuguese":{"loses":0,"wins":0},"Saracens":{"loses":0,"wins":0},"Slavs":{"loses":0,"wins":0},"Spanish":{"loses":0,"wins":0},"Tatars":{"loses":0,"wins":0},"Teutons":{"loses":0,"wins":0},"Turks":{"loses":0,"wins":0},"Vietnamese":{"loses":0,"wins":0},"Vikings":{"loses":0,"wins":0}}}


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
        return_text += "<li>" + civilization_winrate[0] + ": " + str(round(civilization_winrate[1], 2)) + "% (Times picked: " + str(civilization_winrate[2]) + ")</li>"
    return return_text


if __name__ == '__main__':
    app.run()
