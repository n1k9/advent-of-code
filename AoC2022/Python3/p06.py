# --- Day 6: Tuning Trouble ---
import doctest
from utils import read_file


def start_marker_len(buffer: str, marker_size=4) -> int:
    """
    >>> start_marker_len('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
    7
    >>> start_marker_len('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
    11
    >>> start_marker_len('mjqjpqmgbljsphdztnvjfqwrcgsmlb', 14)
    19
    """
    for i in range(len(buffer)-marker_size):
        if len(set(buffer[i:i+marker_size])) == marker_size:
            return i+marker_size
    return -1


if __name__ == "__main__":
    datastream = read_file('../datas/d06.txt').strip()

    # --- Part One ---
    print(f"1: {start_marker_len(datastream)}")

    # --- Part twe ---
    print(f"2: {start_marker_len(datastream, 14)}")
