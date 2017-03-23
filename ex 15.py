from sys import argv
#import argv
script, filename = argv
#set the script and file name to open
txt = open(filename)
#set open the file above to txt
print "Here is your file %r:" % filename
#just print
print txt.read()
#print read the txt just openned
print "type the file name again:"
#just print
file_again = raw_input("> ")
#input another file
txt_again = open(file_again)
#open it
print txt_again.read()
#and print again
raw_input("Press enter to exit")
#pause cmd, not exactly needed
