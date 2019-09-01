import unidecode
import unicodedata
import sys
import os

if "--input" in sys.argv:
    input_path = str(sys.argv[sys.argv.index("--input") + 1])
    while os.path.isfile(input_path) is False:
        input_path = str(input("Provide path to correct data source (must be a file): "))
    text = open(input_path, "rt", encoding="utf-8").read()
else:
    text = str(input("Your text: "))

if "--output" in sys.argv:
    output_path = str(sys.argv[sys.argv.index("--output") + 1])
else:
    output_path = os.path.realpath("output.txt")

replacement_char = None
if "-skip" or "-replace" in sys.argv:
    if "-skip" in sys.argv:
        replacement_char = ""
    elif "-replace" in sys.argv:
        replacement_char = "?"


def sanitizer(source):
    if replacement_char is not None:
        others = ["Lo", "No", "So", "Sm", "Sk"]
        for x in source:
            if x.isascii() is False and unicodedata.category(x) in others:
                source = source.replace(x, replacement_char)
    return unidecode.unidecode(source)


output_file = open(output_path, "w", encoding="utf-8")
output_file.write(sanitizer(text))
output_file.close()
print(f"Parsed text was successfully saved in {output_path}")
