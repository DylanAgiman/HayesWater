# Dylan Agiman water code for Hayes research group

import urllib.request
import math

link = "http://rapid-hub.org/data/angles_UCI_CS.csv"
file = urllib.request.urlopen(link).read().decode("utf-8")

# splitting the input file, ignoring the last empty line
lines = file.split("\r\n")[:-1]


# for debugging purposes to check the contents of the csv
# print("\n\nprinting lines after splitting\n")
# for i, line in enumerate(lines):
#    print(i, ": ",line)

# tbd: manage the formatting of the output and calculate the cosine
print("station_id  angle_degrees  cos_values")
for i, line in enumerate(lines[1:]):
    elems = [elem.strip() for elem in line.split(',')]
    station_id = int(elems[0])
    angle = float(elems[1])
    print("{:10d}  {:13}  {:10f}".format(station_id, angle, math.cos(math.radians(angle))))
