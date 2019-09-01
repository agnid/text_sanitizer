# Text sanitizer

Simple text data parser to escape all non-ASCII characters. Chars will be replaced with its ASCII version 
(e.g. ą with a, Ô with O, ẞ with ss).

## Requirements 
* Program require Python 3.6 or higher and is run from the command line
* Source data should use UTF-8 encoding

## How to use
Supported command line arguments:

**--input**: used to provide path to source file used for sanitization

**--output**: used to provide path to where sanitized text will be saved (if not provided, 
    file output.txt will be saved in current directory)
    
## Examples
### Example 1
 `python sanitizer.py --input source.html --output source-output.html`

Gets text from file source.html and after encoding to ASCII saves output to source-output.html. 
If source-output.html already exists, all its content will be removed and replaced with program's output.
### Example 2
 `python sanitizer.py`

You will be prompted to provide text. Output will be saved in output.txt in the current directory.
