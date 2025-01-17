import os
import json
from shutil import move


class Sorter:
    def __init__(self, directory: str, mapping_file: str):
        self.DIRECTORY: str = directory
        self.MAPPINGS: dict[str, str] = self.__read_json_mappings(mapping_file)
        self.CATEGORIES: list[str] = self.__get_catagory_list(self.MAPPINGS)

    def __read_json_mappings(self, file: str) -> dict[str, str]:
        with open(file) as f:
            content: dict[str, str] = json.load(f)
            return content

    def __get_catagory_list(self, mappings: dict[str, str]) -> list[str]:
        categories: set[str] = set()
        for x in mappings.values():
            if x not in categories:
                categories.add(x)

        categories.add("other")

        return list(categories)

    def sort(self):
        self.__create_subdir(self.DIRECTORY, self.CATEGORIES)
        self.__sort_content(self.DIRECTORY, self.MAPPINGS, self.CATEGORIES)

    def __is_download(self, extension: str) -> bool:

        temp_ext = ("crdownload", "tmp")

        if extension in temp_ext:
            return True
        return False

    def __create_subdir(self, path: str, categories: list[str]):
        for category in categories:
            category_path = os.path.join(path, category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)

    def __sort_content(
        self, path: str, mappings: dict[str, str], categories: list[str]
    ):
        items = os.listdir(path)

        # remove directories themselves
        for x in categories:
            items.remove(x)

        for item in items:
            str_split = item.split(".")
            if len(str_split) > 1:
                extension = str_split[1]
                category = (
                    "other"
                    if mappings.get(extension) is None
                    else str(mappings.get(extension))
                )
            else:
                category = "other"

            source_path = os.path.join(path, item)
            destination_path = os.path.join(path, category, item)

            move(source_path, destination_path)
