#Felix Ferreira
#6/5/2018

fName = "script.rpy"
directive = "#define"

f = open(fName, "r", encoding='utf8')

if(f == None):
    print("File: " + fName + " not found!")
else:
    print("File: " + fName + " found!")
    print("Parsing file...")
    print("First pass...")
    print("Getting #define statements...")

    #go through the file and fetch definitions
    #forces minimum 2 passes to parse file
    #because #define may be at bottom of file but used up top
    definitions = []
    
    for l in f.readlines():
        if not l:
            continue
        line = str.split(l)
        if not line:
            continue
        if line[0] == directive:
            string2 = line[2]
            end = string2[-2:]
            if end == "\n":
                string2 = string2[:-2]
            
            definitions.append([line[1], string2])
    f.close()
    print("Definitions read...")
    #print out what will be redefined
    for d in definitions:
        print("'", d[0], "' will be replaced by '", d[1], "'")
    #add spaces around definitions
    for d in definitions:
        d[0] = " " + d[0] + " "
        #d[1] = " " + d[1] + " " #add apces around replaced text, may or may not want this
    
    print()
    
    #read every line and put it into a list
    print("Second pass...")
    print("Reading in file...")
    
    f = open(fName, "r", encoding='utf8')
    
    file = []
    lineNumber = 0
    for line in f:
        file.append(line)
    
    f.close()
    print()
    #write out parsed file
    print("Third pass...")
    print("writting file...")
    
    #write back all lines to the file
    
    f = open(fName, "w", encoding='utf8')
    
    replacedWords = 0
    for line in file:
        if not line:
            continue
        if line[0] == "#":#if line is a comment or definition
            f.write(line)#skip it by just writting it
        else:
            out = list(line) #list of characters
            for i in range(len(definitions)):
                result = line.find(definitions[i][0])
                if result == -1:
                    continue
                else:
                    out[result] = definitions[i][1] # replace letter with string replacement
                    replacedWords += 1
                    index = result + 1
                    while index < len(out):
                        if out[index] == " " or out[index] == "\n":
                            break
                        del out[index]
                            
                        
            #expand out after all definitions have been written
            expandedOut = []
            
            for e in out:
                for c in e:
                    expandedOut.append(c)
            endString = "".join(expandedOut)
            #print expanded output to file
            f.write(endString)
            
            if endString[len(endString) - 1] != '\n':
                f.write("\n")
            
    
    f.close()
    print(replacedWords, " replaced words...")
    print("Done!")
    