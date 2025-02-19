from utils import get_dir
from utils import get_files

class BlackoutCry:
    def __init__(self):
        self.root_dir = get_dir()
        self.files = []
        pass
    
    def run(self):
        self.files = get_files(self.root_dir)
        print(self.files)

    