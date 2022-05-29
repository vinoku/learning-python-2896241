# 
# Example file for parsing and processing HTML
# LinkedIn Learning Python course by Joe Marini
#

from html.parser import HTMLParser

paragraphs = 0
class MyHTMLParser(HTMLParser):
    def handle_comment(self, data):
        print ("Encountered comment:", data)
        pos = self.getpos()
        print ("\tAt line: ", pos[0], " position ", pos[1])

    def handle_starttag(self, tag, attrs):
        global paragraphs
        if tag == "p":
            paragraphs += 1

        print ("Encountered a start tag:", tag)
        pos = self.getpos() # returns a tuple indication line and character
        print ("\tAt line: ", pos[0], " position ", pos[1])

        if attrs.__len__() > 0:
            print ("\tAttributes:")
            for a in attrs:
                print ("\t", a[0],"=",a[1])

    def handle_data(self, data):
        if (data.isspace()):
            return
        print ("Encountered some text data:", data)
        pos = self.getpos()
        print ("\tAt line: ", pos[0], " position ", pos[1])

def main():
    # instantiate the parser and feed it some HTML
    parser = MyHTMLParser()
    
    f = open("samplehtml.html")
    if f.mode == "r":
        contents = f.read() # read the entire file
        parser.feed(contents)   

    print ("Paragraph tags:", paragraphs) 

if __name__ == "__main__":
    main()
  