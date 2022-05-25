from sys import stderr
from panflute import *

headers = []

def prepare(input_doc):
    input_doc.replace_keyword("BOLD", Strong(Str("BOLD")))

def upper_headers(now_element, doc):
    if isinstance(now_element, Header) and now_element.level > 2:
        return Header(Str(stringify(now_element).upper), level=now_element.level)


def header_attention(now_element, doc):
    if isinstance(now_element, Header):
        text = stringify(now_element)
        if text in headers:
            print("Repeat headlines: " + text, file=stderr)
        else:
            headers.append(text)


def finalize(doc):
    pass

def main(doc=None):
    return run_filters([upper_headers, header_attention], prepare=prepare, finalize=finalize, doc=doc)

if __name__ == '__main__':
    main()