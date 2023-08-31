from urllib.request import urlopen
from pdfminer.high_level import extract_text

def readPDF(pdfUrl):  # 関数の引数名も変更しました
    text = extract_text(pdfUrl)  # ファイルオブジェクトではなく、ファイルのURLを渡します
    return text

pdf_url = "http://pythonscraping.com/pages/warandpeace/chapter1.pdf"
output_string = readPDF(pdf_url)  # ファイルのURLを渡すように修正
print(output_string)
