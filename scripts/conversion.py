import re  # regular expression library

from os import listdir
from os.path import isfile, isdir, join
collectionDirectories = [f for f in listdir() if isdir(f)]
files = [f for f in listdir() if isfile(f)]


collectionDirectory = collectionDirectories[1]
print(collectionDirectories)
print(files)

allDirectories = [f for f in listdir(collectionDirectory) if isdir(join(collectionDirectory,f))]

for mDirectory in allDirectories:
    htmlFile = open(join(collectionDirectory, mDirectory, "index.cnxml.html"), "r")

    mathJaxLine = """
                     <link rel="stylesheet" href="../content.css" media="screen">\n
                     <script type="text/javascript" async'
                     src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-MML-AM_CHTML">
                     </script>\n """

    # file-output.py
    myHtmlFile = open(join(collectionDirectory, mDirectory,'myIndex.html'),'w')


    for line in htmlFile:
        imgRegexp=re.compile('<img src')
        imgMatch = imgRegexp.findall(line)

        if imgMatch:
            newLine = re.sub(r'"','"', line)
            myHtmlFile.write(newLine)
        else:
            myHtmlFile.write(line)
            htmlRegexp=re.compile('<html')
            htmlMatch = htmlRegexp.findall(line)

            if htmlMatch:
                myHtmlFile.write(mathJaxLine)

    myHtmlFile.close()
    htmlFile.close()

import os

def get_filepaths(directory):
    """
    This function will generate the file names in a directory
    tree by walking the tree either top-down or bottom-up. For each
    directory in the tree rooted at directory top (including top itself),
    it yields a 3-tuple (dirpath, dirnames, filenames).
    """
    file_paths = []  # List which will store all of the full filepaths.

    # Walk the tree.
    for root, directories, files in os.walk(directory):
        for filename in files:
            # Join the two strings in order to form the full filepath.
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)  # Add it to the list.

    return file_paths  # Self-explanatory.

# Run the above function and store its results in a variable.
full_file_paths = get_filepaths('/Users/veillettem/Google Drive/221/university-physics-volume-1-5.60/col12031_1.5_complete')


for f in full_file_paths:
  if f.endswith(".html"):
    print(f)
