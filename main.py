
import pandas as pd


def create_DataFrame(annotation: str) -> None:
    file = open(annotation, "r", encoding="utf-8")

    for line in file:
        print(line)


def main() -> None:
    create_DataFrame("D:\\python_labs\\datas\\annotation.csv")


if __name__ == "__main__":
    main()