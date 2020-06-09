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

civ_winrate = {
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
    'Arabia': civ_winrate,
    'Archipelago': civ_winrate,
    'Baltic': civ_winrate,
    'Black Forest': civ_winrate,
    'Coastal': civ_winrate,
    'Continental': civ_winrate,
    'Crater Lake': civ_winrate,
    'Fortress': civ_winrate,
    'Gold Rush': civ_winrate,
    'Highland': civ_winrate,
    'Islands': civ_winrate,
    'Mediterranean': civ_winrate,
    'Migration': civ_winrate,
    'Rivers': civ_winrate,
    'Team Islands': civ_winrate,
    'Scandinavia': civ_winrate,
    'Mongolia': civ_winrate,
    'Yucatan': civ_winrate,
    'Salt Marsh': civ_winrate,
    'Arena': civ_winrate,
    'Oasis': civ_winrate,
    'Ghost Lake': civ_winrate,
    'Nomad': civ_winrate,
    'Acropolis': civ_winrate,
    'Budapest': civ_winrate,
    'Cenotes': civ_winrate,
    'City of Lakes': civ_winrate,
    'Golden Pit': civ_winrate,
    'Hideout': civ_winrate,
    'Hill Fort': civ_winrate,
    'Lombardia': civ_winrate,
    'Steppe': civ_winrate,
    'Valley': civ_winrate,
    'MegaRandom': civ_winrate,
    'Hamburger': civ_winrate,
    'Kilimanjaro': civ_winrate,
    'Mountain Pass': civ_winrate,
    'Nile Delta': civ_winrate,
    'Serengeti': civ_winrate,
    'Socotra': civ_winrate,
    'Sandbank': civ_winrate,
    'Water Nomad': civ_winrate,
    'Alpine Lakes': civ_winrate,
    'Bogland': civ_winrate,
    'Mountain Ridge': civ_winrate,
    'Ravines': civ_winrate,
    'Wolf Hill': civ_winrate,
    'Golden Swamp': civ_winrate,
    'Four Lakes': civ_winrate
}

weekly_maps = ['Arabia', 'Black Forest', 'Arena', 'Nomad', 'Scandinavia', 'Hill Fort', 'Lombardia', 'MegaRandom', 'Wolf Hill']
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


if __name__ == '__main__':
    app.run()
