import argparse

parser=argparse.ArgumentParser(description='Counts lines, words, letters')
parser.add_argument('file', help="Name of the file that counted")
parser.add_argument('-l', help="To count lines", action='store_true')
parser.add_argument('-w', help="To count lines", action='store_true')
parser.add_argument('-b', help="To count lines", action='store_true')
args=parser.parse_args()

try:
    f=open(args.file)
    lcount=0
    wcount=0
    bcount=0

    for line in f:
        for letter in line:
            bcount=bcount+1
        words=line.split()
        wcount=wcount+len(words)
        lcount=lcount+1
    f.close()

    if args.l:
        print("Lines: " + str(lcount) + "\n")
    if args.w:
        print("Words: " + str(wcount) + "\n")
    if args.b:
        print("Characters: " + str(bcount) + "\n")


except IOError:
    print("The file does not exits.")
