
import pandas as pd


def create_DataFrame(annotation: str) -> None:
    file = open(annotation, "r", encoding="utf-8")

    df = pd.DataFrame(columns=["ClassName", "Directory"])

    for line in file:
        line = line.split(",")
        df.loc[len(df.index)] = [line[2].split("\n")[0], line[0]]
    
    print(df)

def main() -> None:
    create_DataFrame("D:\\python_labs\\datas\\annotation.csv")


if __name__ == "__main__":
    main()