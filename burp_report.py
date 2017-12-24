#!/usr/bin/python

import base64
import sys
import pickle
import os

HTML_TEMPLATE_FILE = "template.bin"

def main(argv):
    
    input_filename = argv[1]
    path, filename = os.path.split(input_filename)
    
   
    # Deserializes the template
    html_template = pickle.load(open(HTML_TEMPLATE_FILE,"rb"))
    
    # Decodes the template
    html_template = base64.b64decode(html_template);
    
    # Sets the TITLE
    html_code = html_template.replace("%TITLE%", filename);
    
    # Sets the data payload
    html_code = html_code.replace("%FILE_NAME%", filename);
    
    with open(input_filename + ".html", "w") as text_file:
        text_file.write(html_code)
    

if __name__ == '__main__':
    main(sys.argv)