from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"


def hw02_1(q1_pdf):
    return PyPDFLoader(q1_pdf).load()[-1]

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    text = ""
    for doc in docs:
        text = text + doc.page_content + "\n"
    spliter = RecursiveCharacterTextSplitter(separators=["第 \\d+-?\\d* 條\n|第 .* 章"],
                                    chunk_size=0,
                                    chunk_overlap=0,
                                    is_separator_regex=True,
                                    keep_separator=True)
    result = spliter.create_documents([text])
    for index, doc in enumerate(result):
        print(index)
        print(doc.page_content)
    return len(result)