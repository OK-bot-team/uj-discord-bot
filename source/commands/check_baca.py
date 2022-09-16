import requests

BACA_URL = "https://baca.ii.uj.edu.pl/"


def check_baca() -> bool:
    try:
        baca_status_code = requests.get(
            BACA_URL, verify=False, timeout=10
        ).status_code

        return baca_status_code == 200
    except (
        requests.ReadTimeout,
        requests.ConnectTimeout,
        requests.ConnectionError,
    ):
        return False
