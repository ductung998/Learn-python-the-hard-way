from sys import argv

script, user_name = argv
promt = '> '

print "Hi %s, I'm the %s script" % (user_name, script)
print "Do you like me %s?" % user_name

like = raw_input(promt)

print "What kind of computer do you have?"

computer = raw_input(promt)

print """
So you said %r about liking me
and are using %r computer
""" % (like, computer)

raw_input("Press enter to exit")
