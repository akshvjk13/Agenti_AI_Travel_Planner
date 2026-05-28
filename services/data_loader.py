import json

def load_json_data(file_path):

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        print(f"Successfully loaded: {file_path}")

        return data

    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []

    except json.JSONDecodeError:
        print(f"Invalid JSON format in: {file_path}")
        return []

    except Exception as error:
        print(f"Unexpected error: {error}")
        return []