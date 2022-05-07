import csv
import os.path
from typing import List
from config import settings
from firebase.firebase import generate_dynamic_link, generate_long_dynamic_link


def csv_to_list(path: str):
    """
    対象ユーザーのCSVファイルを処理用にList化する
    :param path: BASE_URL以降のパスを指定する
    :return: 対象のcsvのリスト
    List({
        email: str,
        username: str,
        id: str
    })
    """
    result = []
    with open(os.path.join(settings.BASE_URL, path)) as f:
        reader = csv.reader(f)
        for row in reader:
            result.append(
                {
                    "email": row[0],
                    "username": row[1],
                    "id": row[2],
                }
            )

    return result


def generate_uri_user_page(user_id: str) -> str:
    second = "userpage"
    query_params = f"?user={user_id}"
    base = settings.SERVICE_BASE_URL
    return os.path.join(base, second + query_params)


def insert_results_csv_file(row: List[str]):
    with open(r'results.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(row)


if __name__ == "__main__":
    try:
        target_list = csv_to_list("config/target_list.csv")
        for target in target_list:
            link = generate_uri_user_page(target["id"])
            dynamic_link = generate_dynamic_link(link)
            dynamic_link_long = generate_long_dynamic_link(link)
            insert_results_csv_file([
                target["email"],
                target["username"],
                target["id"],
                dynamic_link,
                dynamic_link_long,
                link
            ])
    except Exception as err:
        print(f"ERR!: {err}")
    finally:
        print("処理完了")




