import xml.sax

class BookHandler(xml.sax.ContentHandler):
    def __init__(self):
        super().__init__()  # Initialize the parent class
        self.current_tag = ""  # Track the current XML tag name
        self.title = ""  # Store book title
        self.author = ""  # Store book author
        self.year = ""  # Store book year

    # Triggered when the parser encounters an opening tag (like <title>)
    def startElement(self, tag, attributes):
        self.current_tag = tag  # Update current_tag with the tag name

    # Triggered when the parser encounters text inside a tag (like "Learning Python" in <title>Learning Python</title>)
    def characters(self, content):
        if self.current_tag == "title":
            self.title = content
        elif self.current_tag == "author":
            self.author = content
        elif self.current_tag == "year":
            self.year = content

    # Triggered when the parser encounters a closing tag (like </title>)
    def endElement(self, tag):
        if tag == "book":  # At the end of each book, print collected data
            print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")
            # Reset the attributes for the next book
            self.title = ""
            self.author = ""
            self.year = ""
        self.current_tag = ""  # Reset current tag name

# Create a SAX parser
parser = xml.sax.make_parser()

# Create an instance of our BookHandler
handler = BookHandler()

# Tell the parser to use our custom handler
parser.setContentHandler(handler)

# Parse the XML file
parser.parse("data.xml")
