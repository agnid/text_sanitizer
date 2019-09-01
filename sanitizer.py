import unidecode
import sys
import os
import io

'''
TBD: check for newline chars
'''

if "--input" in sys.argv:
    input_path = str(sys.argv[sys.argv.index("--input") + 1])
    while os.path.isfile(input_path) is False:
        input_path = str(input("Provide path to correct data source (must be a file): "))
    text = io.open(input_path, "r", encoding="utf-8").read()
else:
    text = str(input("Your text: "))

if "--output" in sys.argv:
    output_path = str(sys.argv[sys.argv.index("--output") + 1])
else:
    output_path = os.path.realpath("output.txt")


def sanitizer(source):
    return unidecode.unidecode(source)


output_file = io.open(output_path, "w", encoding="utf-8")
output_file.write(sanitizer(text))
output_file.close()
