from blackout_cry import BlackoutCry
from utils import get_os
import platform

if __name__ == "__main__":
    operating_system = get_os()
    if operating_system == "iOS":
        exit(0)

    randsom = BlackoutCry()
    randsom.run()