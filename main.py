import urllib.request

link = "http://rapid-hub.org/data/angles_UCI_CS.csv"
file = urllib.request.urlopen(link).read().decode("utf-8")

# splitting the input file, ignoring the first comment
lines = file.split("\r\n")

print("\n\nprinting lines after splitting\n")
for i, line in enumerate(lines):
    print(i, ": ",line)

# tbd: manage the formatting of the output and calculate the cosine
