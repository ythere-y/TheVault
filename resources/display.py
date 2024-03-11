# 读取function/java/small_train.jsonl中的数据
# 取出前100行制作成一个新的jsonl文件,写入到function/java/small_train_100.jsonl中

import json
import os


def read_jsonl_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    return lines


def write_jsonl_file(file_path, lines):
    with open(file_path, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(json.dumps(line, ensure_ascii=False))
            f.write("\n")


def main():
    # 读取function/java/small_train.jsonl中的数据
    lines = read_jsonl_file("resources/function/java/small_train.jsonl")
    # 取出前100行制作成一个新的jsonl文件,写入到function/java/small_train_100.jsonl中
    write_jsonl_file("resources/function/java/small_train_100.jsonl", lines[:100])


if __name__ == "__main__":
    main()
