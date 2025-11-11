"""
Extension Extractor
Given a string representing a filename, return the extension of the file.

The extension is the part of the filename that comes after the last period (.).
If the filename does not contain a period or ends with a period, return "none".
The extension should be returned as-is, preserving case.
"""
def get_extension(filename):
    
    extension = filename.split(".")[-1]
    if extension:
        if   len(filename.split(".")) > 1:
            return extension
        else: 
            return "none"
    
    else:
        return "none"

print(get_extension("final.draft."))
print(get_extension("README"))

"""
Tests
Waiting:1. get_extension("document.txt") should return "txt".
Waiting:2. get_extension("README") should return "none".
Waiting:3. get_extension("image.PNG") should return "PNG".
Waiting:4. get_extension(".gitignore") should return "gitignore".
Waiting:5. get_extension("archive.tar.gz") should return "gz".
Waiting:6. get_extension("final.draft.") should return "none".
"""
