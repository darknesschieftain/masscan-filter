
usage: python3 masscan-filter.py [-h] [-i INPUT_FILE] [-o OUTPUT_FILE]

optional arguments:
-h, --help      show this help message and exit
-i INPUT_FILE   file for filtering ips
-o OUTPUT_FILE  file for output

example:
masscan -p80 0.0.0.0/24 > file.txt
python3 masscan-filter.py -i file.txt -o newfile.txt
