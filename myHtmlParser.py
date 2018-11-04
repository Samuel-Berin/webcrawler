# Code inspired by https://docs.python.org/3/library/html.parser.html (PYTHON DOCUMENTATION)
from HTMLParser import HTMLParser

class myHtmlParser(HTMLParser):
    getThisFlag = False
    secret_flags = []

    def handle_starttag(self, tag, attrs):
        if tag == "h2":
            for attr in attrs:
                if attr[0] == 'class' and attr[1] == 'secret_flag':
                    self.getThisFlag = True

    def handle_data(self, data):
        if (self.getThisFlag):
            self.secret_flags.append(data)

    def getFlags(self):
        return self.secret_flags

parser = myHtmlParser()
parser.feed('<h2 class=\'secret_flag\' style="color:red">FLAG: 64-characters-of-random-alphanumerics</h2>')
print(parser.getFlags())
