from sys import argv

script, filename = argv #ex15.py, ex15_sample.txt = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()
close(txt)
close(txt_again)