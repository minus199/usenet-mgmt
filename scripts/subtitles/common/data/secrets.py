creds = {
    'addic7ed': {'u': "mrmarket", 'p': "xfpH0vAAO9"},
    'legendastv': {'u': "minus199", 'p': "4zwnDfY05W"},
    'opensubtitles': {'u': "N/A", 'p': "N/A"},
    'omdb_api_key': {'k': "9a741426"}  # (minus199 email)
}


def to_config():
    return {
        'refiner_configs': {'omdb': {'apikey': creds['omdb_api_key']['k']}},
        'provider_configs': {
            'addic7ed': {'username': creds['addic7ed']['u'], 'password': creds['addic7ed']['p']},
            'legendastv': {'username': creds['legendastv']['u'], 'password': creds['legendastv']['p']},
            'opensubtitles': {'username': creds['opensubtitles']['u'], 'password': creds['opensubtitles']['p']}
        }
    }
