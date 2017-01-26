from xml.dom.minidom import parse
xml = parse("sample.xml")
entries = xml.getElementsByTagName("book")
for e in entries:
    rev = e.getAttribute("id")
    msg = e.getElementsByTagName("author")[0].firstChild.nodeValue
    print "book" + " " + rev + " " + msg
