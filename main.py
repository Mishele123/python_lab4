
import pandas as pd
import cv2

# tiger = 0 leopard = 1

def create_DataFrame(annotation: str) -> None:
    

    df = pd.DataFrame(columns=["ClassName", "Directory"])

    with open(annotation, "r", encoding="utf-8") as file:
        for line in file:
            line = line.split(",")
            df.loc[len(df.index)] = [line[2].split("\n")[0], line[0]]

    df['mark'] = 0

    # Присваиваем значения 0 / 1
    df.loc[df["ClassName"] == "tiger", "mark"] = 0
    df.loc[df["ClassName"] == "leopard", "mark"] = 1

    # Создаем столбцы с размерами изображений
    df[["height", "width", "channels"]] = df["Directory"].apply(lambda x: pd.Series(get_image_properties(x)))
    print(df)

    image_size_stats = df[["height", "width", "channels"]].describe()
    class_stats = df["ClassName"].value_counts()

    print("Статистика по размерам изображений:")
    print(image_size_stats)
    print("\n Статистика по классам:")
    print(class_stats)

    is_balanced = abs(class_stats[0] - class_stats[1]) <= 1
    print("\n Набор данных является сбалансированным:", is_balanced)

    df = filter_DataFrame(df, 0)

    print(df)

def get_image_properties(img_path: str) -> int:
    image = cv2.imread(img_path)
    height, width, channels = image.shape
    return height, width, channels


def filter_DataFrame(df: pd.DataFrame, mark: int) -> pd.DataFrame:
    sorted_df = df.sort_values(by = "mark")
    return  sorted_df[sorted_df["mark"] == mark].reset_index(drop=True)

def main() -> None:
    create_DataFrame("D:\\python_labs\\datas\\annotation.csv")


if __name__ == "__main__":
    main()