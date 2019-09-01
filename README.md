# Text sanitizer

Very basic text data parser to escape all non-ASCII characters. Chars will be replaced with its ASCII version 
(e.g. ą with a, Ô with O, ẞ with ss).

Parser works best for texts in Latin or Cyrillic alphabets. 
If your text include characters from non-Latin alphabets 
or miscellaneous math symbols, they may not be replaced adequately. In such cases it is 
recommended to use script with -replace or -skip operator.

## Requirements 
* Program require Python 3.6 or higher
* Source data should use UTF-8 encoding

## How to use

All you need is to run the script from command line. 

And for control-lovers, there are some supported command line arguments:

**1. Input and output file handling:** 

**--input**: used to provide path to source file used for sanitization

**--output**: used to provide path to where sanitized text will be saved (if not provided, 
    file output.txt will be saved in current directory)

**2. Data handling**
Important! Using this arguments may slow down the program

**-replace**: unrecognized characters (such as letters from non-Latin or Cyrillic alphabets or non-ASCII math symbols)
will be replace with "?"

**-skip**: unrecognized characters (such as letters from non-Latin or Cyrillic alphabets or non-ASCII math symbols)
will be removed from encoded text
    
## Examples
### Example 1
 `python sanitizer.py --input source.html --output source-output.html`

Gets text from file source.html and after encoding to ASCII saves output to source-output.html. 
If source-output.html already exists, all its content will be removed and replaced with program's output.
### Example 2
 `python sanitizer.py`

You will be prompted to provide text. Output will be saved in output.txt in the current directory.

### Example 3
 `python sanitizer.py -skip`

Know characters will be replaced with its closes ASCII equivalent and unknown ones will be 
skipped while parsing text.

For example text

    chin. 漢字 / 汉字, Hànzì
    
will be encrypted as

    chin.  / , Hanzi
    
### Example 4
 `python sanitizer.py -replace`

Know characters will be replaced with its closes ASCII equivalent and unknown ones will be 
replaced with "?" while parsing text.

For example text

    chin. 漢字 / 汉字, Hànzì
    
will become after encryption

    chin. ?? / ??, Hanzi
