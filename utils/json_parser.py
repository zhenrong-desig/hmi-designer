import json


class json_parser:

    def load_item_data_from_config(
        self,
        config_file_path,
        item=None,
    ):
        with open(
                config_file_path,
                "r",
                encoding="utf-8",
        ) as file:
            self.data = json.load(file)
        if item is not None and self.data is not None:
            return self.data.get(item, [])
        else:
            return self.data
