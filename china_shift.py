import argparse  # for parsing input arguments
import csv       # for reading comma-separated floats

# load dynamic C library for map shift
from ctypes import *
shift = cdll.LoadLibrary('./china_shift.dll')

class Location(Structure):
    _fields_ = [
        ('lon', c_double),
        ('lat', c_double)]

shift.transformFromWGSToGCJ.argtypes = [Location]
shift.transformFromWGSToGCJ.restype = Location
shift.transformFromGCJToWGS.argtypes = [Location]
shift.transformFromGCJToWGS.restype = Location

# load KML file
class NoShiftOptionException(Exception):
    pass

try:
    import xml.etree.cElementTree as et  # C version of ElementTree
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-g', '--wgs2gcj', help = 'shift from WGS-84 to GCJ-02', action = 'store_true')
    group.add_argument('-w', '--gcj2wgs', help = 'shift from GCJ-02 to WGS-84', action = 'store_true')
    parser.add_argument('input_file', help = 'name of input KML file')
    args = parser.parse_args()
    if not (args.wgs2gcj or args.gcj2wgs):
        raise NoShiftOptionException
    tree = et.ElementTree(file = args.input_file)
except ImportError:
    # in case of absence of cElementTree, use Python version of the library
    import xml.etree.ElementTree as et
except IOError:
    print 'Error: input file', args.input_file, 'not found.'
    quit()
except NoShiftOptionException:
    print 'Error: too few arguments.\n' + \
          '       Use -g (--wgs2gcj) to shift from WGS-84 to GCJ-02,\n' + \
          '        or -w (--gcj2wgs) to shift from GCJ-02 to WGS-84.'
    quit()

# process the file
count = 0

# coordinates in <gx:coord> tags, eg. Moves export file
for elem in tree.iterfind('.//{http://www.google.com/kml/ext/2.2}coord'):
    coord = [float(x) for x in elem.text.split()]
    loc = Location(lon = coord[0], lat = coord[1])
    if args.wgs2gcj:
        loc = shift.transformFromWGSToGCJ(loc)
    if args.gcj2wgs:
        loc = shift.transformFromGCJToWGS(loc)
    elem.text = str(loc.lon) +' '+ str(loc.lat) +' '+ str(0)
    count += 1

# coordinates in <coordinates> tags, eg. Google Earth path export file
for elem in tree.iterfind('.//{http://www.opengis.net/kml/2.2}coordinates'):
    coords = [s for s in elem.text.split()]
    text_buf = ''
    for coord in csv.reader(coords):
        loc = Location(lon = float(coord[0]), lat = float(coord[1]))
        if args.wgs2gcj:
            loc = shift.transformFromWGSToGCJ(loc)
        if args.gcj2wgs:
            loc = shift.transformFromGCJToWGS(loc)
        text_buf += str(loc.lon) +','+ str(loc.lat) +','+ str(0) +' '
        count += 1
    elem.text = text_buf

output = open('output.kml', 'w')
tree.write(output)
output.close()

if args.wgs2gcj:
    success_str = 'WGS-84 to GCJ-02.'
if args.gcj2wgs:
    success_str = 'GCJ-02 to WGS-84.'
print str(count), 'coordinates shifted from', success_str
