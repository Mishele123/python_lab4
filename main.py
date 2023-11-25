
import pandas as pd
import cv2
import random
from matplotlib import pyplot as plt

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

    is_balanced = False
    if abs(class_stats["leopard"] - class_stats["tiger"]) <= 1:
        is_balanced = True

    print("\n Набор данных является сбалансированным:", is_balanced)
    df = filter_DataFrame(df, 0)

    print(df)

    df = filter_DataFrame_by_task(df, 0, image_size_stats["width"]["max"], image_size_stats["height"]["max"])

    print(df)

    df = grouping_DataFrame(df, 0)

    print(df)
    
    create_hustogram(df, 0)

def get_image_properties(img_path: str) -> int:
    image = cv2.imread(img_path)
    height, width, channels = image.shape
    return height, width, channels


def filter_DataFrame(df: pd.DataFrame, mark: int) -> pd.DataFrame:
    sorted_df = df.sort_values(by = "mark")
    return  sorted_df[sorted_df["mark"] == mark].reset_index(drop=True)

def filter_DataFrame_by_task(df: pd.DataFrame, mark: int, max_width: int, max_height: int) -> pd.DataFrame:
    sorted_df = filter_DataFrame(df, mark)
    sorted_df = df.sort_values(by = ["height", "width"])
    return sorted_df[(sorted_df["height"] <= max_height) & (sorted_df["width"] <= max_width)].reset_index(drop=True)

def grouping_DataFrame(df: pd.DataFrame, mark: int) -> pd.DataFrame:
    df = filter_DataFrame(df, mark)
    df["number_of_pixels"] = df["height"] * df["width"] * df["channels"]
    grouped_df_pixels = df['number_of_pixels'].agg(['min', 'max', 'mean'])
    print(grouped_df_pixels)
    return df    


def create_hustogram(df: pd.DataFrame, mark: int) -> None:
    filter_DataFrame(df, mark)
    arr = df["Directory"].tolist()
    random.shuffle(arr)

     

def main() -> None:
    create_DataFrame("D:\\python_labs\\datas\\annotation.csv")


if __name__ == "__main__":
    main()