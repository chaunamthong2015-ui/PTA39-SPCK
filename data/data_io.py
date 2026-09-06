import json

class DataIO:
    @staticmethod # khong can tao object van dung duoc ham (def)
    def read_json(file_path) -> None:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f) # json -> python dict
        return data

    @staticmethod
    def write_json(file_path, data) -> None:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4) # python object -> json


        print(f"Data written to {file_path} successfully.")


# test drive
if __name__ == "__main__":
    path = "data/test.json"
    # viet file
    user_list = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35}
    ]
    DataIO.write_json(path, user_list) 