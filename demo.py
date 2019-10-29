import os
import sys
import importlib

importlib.reload(sys)
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


base_dir = os.path.dirname(__file__)

reports = os.path.join(base_dir, "年报")

files = os.listdir(reports)
names = [x for x in files if x.endswith(".txt")]
files = [x for x in files if x.endswith(".pdf")]


def set_path(file):
    source = os.path.join(reports, file)
    parse_file = os.path.join(reports, f"{file[0:-4]}.txt")
    return source, parse_file


def parse(path):
    print(path)
    fp, pf = set_path(path)
    if os.path.exists(pf):
        return
    fp = open(fp, "rb")
    parser = PDFParser(fp)
    doc = PDFDocument()
    parser.set_document(doc)
    doc.set_parser(parser)

    doc.initialize()

    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        for page in doc.get_pages():
            interpreter.process_page(page)
            layout = device.get_result()

            for x in layout:
                if isinstance(x, LTTextBoxHorizontal):
                    with open(pf, "a", encoding="utf-8") as f:
                        results = x.get_text()
                        f.write(results + "\n")


def file_content(file):
    fp, pf = set_path(file)
    with open(pf, "r", encoding="utf-8") as f:
        text = f.readlines()
    text = "".join(text)
    return text


def complex(content):
    rate = {
        "1": ["螺纹钢", "线材"],
        "2": ["热轧", "冷轧", "中厚板"],
        "3": ["大型型材", "中小型型材"],
        "4": ["无缝管", "焊接管", "球墨铸铁"],
        "5": ["工具钢", "结构钢", "特殊用钢"],
    }
    rating = 1
    for r in range(0, 5):
        key = str(5 - r)
        for value in rate[key]:
            if value in content:
                rating = key
                return rating
    return rating


if __name__ == "__main__":
    for file in files:
        parse(file)
