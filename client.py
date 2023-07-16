"""
Multi-instance app test
=======================

Client
------

Client script that will query the server for the computation results.
"""

import datetime
import sys

import requests


# constants
SERVER_URL = 'http://0.0.0.0:80'
S1 = datetime.timedelta(seconds=1)


def ping_server() -> None:
    """Execute a single client request."""
    r = requests.get(SERVER_URL)
    return r


def get_rps(r: requests.Response) -> float:
    """Return the live RPS value from the last request."""
    request_time = r.elapsed
    rps = int(S1 / request_time)
    return rps


def get_message(r: requests.Response) -> str:
    """Return the message from the last request."""
    msg = r.json()['message']
    return msg


def print_status(msg: str, rps: list[float]) -> None:
    avg_rps = sum(rps) / len(rps)
    console_msg = f'{msg} | {avg_rps:5.1f} RPS'
    sys.stdout.write('\r')
    sys.stdout.flush()
    print(console_msg, end='')
    return None


def main() -> int:
    """Execute the client loop."""
    start_time = datetime.datetime.now()
    rps = []
    while True:
        current_time = datetime.datetime.now()
        if (current_time - start_time) > datetime.timedelta(seconds=1):
            print_status(msg, rps)
            start_time = current_time
            rps = []
        r = ping_server()
        rps.append(get_rps(r))
        msg = get_message(r)
    return 0



if __name__ == '__main__':
    sys.exit(main())
