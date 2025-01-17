import os
from pathlib import Path
from sorter import Sorter


def main():
    DOWNLOADS = os.path.join(Path.home(), "Downloads")

    sorter: Sorter = Sorter(DOWNLOADS, "extension_mapping.json")
    sorter.sort()


if __name__ == "__main__":
    main()
