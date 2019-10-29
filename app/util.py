import os

import tabula

from app.config import base_path


def source_file_path():
    return os.path.join(base_path, "年报")


def reports_pdf():
    path = source_file_path()
    files = os.listdir(path)
    files = [x for x in files if x.endswith("pdf")]
    return files


def reports_txt():
    path = source_file_path()
    files = os.listdir(path)
    files = [x for x in files if x.endswith("txt")]
    return files


def report_content(file_name):
    src = source_file_path()
    file = os.path.join(src, file_name)
    with open(file, "r", encoding="utf-8") as f:
        text = f.readlines()
    text = [t for t in text if t != "\n"]
    text = "".join(text)
    return text


def read_table(file_name):
    """读取pdf文件的表格"""
    src = source_file_path()
    path = os.path.join(src, file_name)
    df = tabula.read_pdf(path, pages="all")
    print(df)



if __name__ == '__main__':
    print(reports_txt())
