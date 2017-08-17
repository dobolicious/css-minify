from os import listdir
from os.path import isfile, join
import os


def strip_lines(lines):

    stripped = ""
    for line in lines:
        line_stripped = line.strip()
        stripped += line_stripped

    return stripped


def stripper(text, index):

    stripped = ""
    options = ["{", ":", ","]

    arr = text.split(options[index])
    count = 0

    for split in arr:
        strip = split.strip()
        stripped += strip
        if count < len(arr) - 1:
            stripped += options[index]

        count = count + 1

    index = index + 1
    if index < len(options):
        return stripper(stripped, index)
    else:

        return stripped


def main():

    cssFile = os.path.abspath("/Users/michael/Dropbox/python/css/main.css")
    compileFile = os.path.abspath("/Users/michael/Dropbox/python/css/main.min.css")

    fr = open(cssFile, "r")
    fw = open(compileFile, "w+")

    stripped = strip_lines(fr)
    stripped = stripper(stripped, 0)

    fw.write(stripped)
    originalSize = os.stat(cssFile).st_size
    compiled = os.stat(compileFile).st_size
    print("Original size:", originalSize)
    print("Compiled size:", compiled)


main()
