replaces text with other text in a file using a c-like preprocessor directive
example:

#define red #FF0000
she sells seashells down by the seashore 
hello 
red 
my favorite color is red 
redredred 

would get turned into:

#define red #FF0000
she sells seashells down by the seashore 
hello 
#FF0000 
my favorite color is #FF0000 
redredred 

notice:
#define red #FF0000
[directive] [word to be replaced] [replacement]


to customize parser:
change input filename: edit fName variable in line 1
change preprocessor "key" character(# by default): edit directive variable in line 2
