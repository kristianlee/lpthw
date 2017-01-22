tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

escape = """
\\ backslash
\' single quote
\" double quote 
\a ASCII bell
\b ASCII backspace
\f ASCII formfeed
\n ASCII linefeed
\N{name} character named name in the unicode database
\r Carriage return
\t horizontal tab  
\v ASCII vertical tab  
\ooo character with octal value ooo 

"""

print escape 