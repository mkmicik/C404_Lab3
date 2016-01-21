#!/usr/bin/env python

# Taken from https://pointlessprogramming.wordpress.com/2011/02/13/python-cgi-tutorial-1/ 01.20.16
# Copyright Nick Zarczynski

import os, json, cgi

print "Content-type: text/html"
print
print "<HTML><BODY>"
print "<TITLE>Test CGI</TITLE>"
print "<h2>Hello World!</h2>"
print "<FORM method = post><INPUT name = 'x'></FORM>"

form = cgi.FieldStorage()

print "<P>X was: " + cgi.escape(str(form.getvalue('x'))) + "</P>"

print "</BODY></HTML>"
#print json.dumps(dict(os.environ), indent=4)