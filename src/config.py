import json


class Config:
    def __init__(self):

        # Open the JSON file
        with open(f".\\config\\settings.json", 'r') as f:
            # Load the array from the JSON file
            data = json.load(f)
            self.settings = data["settings"]

        print(f"Config loaded {str(len(self.settings))} Settings")

    def get(self, key):
        return self.settings[key]
