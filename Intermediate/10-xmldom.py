from xml.dom.minidom import parse

# Parse the XML file and get the root element
dom_tree = parse("data.xml")  # Load the XML file into memory and parse it as a tree
library = dom_tree.documentElement  # Get the root element, <library>

# Retrieve all <book> elements from the XML tree
books = library.getElementsByTagName("book")

# Loop through each <book> element and extract information
for book in books:
    # For each <book>, retrieve the <title>, <author>, and <year> elements
    title = book.getElementsByTagName("title")[0].childNodes[0].data
    author = book.getElementsByTagName("author")[0].childNodes[0].data
    year = book.getElementsByTagName("year")[0].childNodes[0].data
    
    # Print out the book information
    print(f"Title: {title}, Author: {author}, Year: {year}")
