import sys
import os
from html.parser import HTMLParser


version_menu_html = ""


class CustomHTMLParser(HTMLParser):
    def __init__(self):
        super(CustomHTMLParser, self).__init__()
        self.parsing_menu = False
        self.open_divs = 0
        self.old_menu_lines = []
        self.body_end_line = 0

    def handle_starttag(self, tag, attrs):
        if tag == "div":
            if self.parsing_menu:
                self.open_divs += 1

            for attr in attrs:
                if attr[0] == "class" and attr[1] == "versions_menu":
                    self.parsing_menu = True
                    self.old_menu_lines.append(self.getpos()[0])

    def handle_endtag(self, tag):
        if tag == "div":
            if self.parsing_menu and self.open_divs == 0:
                self.old_menu_lines.append(self.getpos()[0])
                self.parsing_menu = False
            self.open_divs -= 1
        elif tag == "body":
            self.body_end_line = self.getpos()[0]


def inject_menu(path):
    n_content = ""
    with open(path, "r+") as fp:
        content = fp.read()
        parser = CustomHTMLParser()
        parser.feed(content)

        arr_content = content.split("\n")
        if len(parser.old_menu_lines) == 0:
            arr_content = (
                arr_content[: parser.body_end_line - 1]
                + [version_menu_html]
                + arr_content[parser.body_end_line - 1 :]
            )
        else:
            arr_content = (
                arr_content[: parser.old_menu_lines[0] - 1]
                + [version_menu_html]
                + arr_content[parser.old_menu_lines[1] :]
            )
        n_content = "\n".join(arr_content)

        fp.seek(0)
        fp.truncate()
        fp.write(n_content)


def recursive_injection(path):
    print(path)
    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isfile(item_path) and item.endswith(".html"):
            print(item_path)
            inject_menu(item_path)
        elif os.path.isdir(item):
            recursive_injection(item_path)
        else:
            continue


if __name__ == "__main__":
    base_path = sys.argv[1]
    assert not base_path.strip() == "", "Provide a base path"
    with open(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), "versions_menu.html"),
        "r",
    ) as fp:
        version_menu_html = fp.read()

    recursive_injection(base_path)

