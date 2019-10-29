import re

from app.config import corporation

from app import util


def search(content, key):
    """关键字查找"""
    content = re.sub("\n", "", content)
    content = re.split(r"[。？！]", content)
    ratio = []
    for c in content:
        if key in c:
            # if re.match(r"\d+", c):
            ratio.append(c)
    ratio = "。".join(ratio)
    return ratio


if __name__ == '__main__':
    # files = util.reports_txt()
    # file = files[0]
    # for file in files:
    #     _content = util.report_content(file)
    #     s = search(_content, "焦炭")
    #     print(file, s)
    files = util.reports_pdf()
    file = files[0]
    util.read_table(file)
