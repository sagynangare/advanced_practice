import re
import optparse
def Main():
    parser = optparse.OptionParser("Usage %prog -w <word> -f <file>")
    parser.add_option('-w', dest ='word', type='string', help="Specify a word to search for")
    parser.add_option('-f', dest ='fname', type='string', help="Specify a file to search for")
    (options,args) = parser.parse_args()
    if (options.word == None) | (options.fname == None):
        print(parser.usage)
        exit(0)
    else:
        word = options.word
        fname = options.fname
    searchFile = open(fname)
    lineNum = 0
    for line in searchFile.readlines():
        line = line.strip('\n\r')
        lineNum +=1
        searchResult = re.search(word, line, re.M|re.I)
        if searchResult:
            print(str(lineNum) + ": "+line)

if __name__ == '__main__':
    Main()
