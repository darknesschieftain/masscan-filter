import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-i",dest="input_file",help="file for filtering ips")
parser.add_argument("-o",dest="output_file",help="file for output")
args = parser.parse_args()

os.popen("cat " + args.input_file + " | awk '{print $6}' > " + args.output_file)
