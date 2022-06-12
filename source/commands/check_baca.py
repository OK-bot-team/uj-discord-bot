import requests

BACA_URL = "https://baca.ii.uj.edu.pl/"


def check_baca() -> bool:
    try:
        baca_status_code = requests.get(
            BACA_URL, verify=False, timeout=10
        ).status_code

        if baca_status_code == 200:
            return True
        else:
            return False
    except (
        requests.ReadTimeout,
        requests.ConnectTimeout,
        requests.ConnectionError,
    ):
        return False
