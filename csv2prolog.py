#============================================
# File name:      csv2prolog.py
# Author:         Olivier Rey
# Date:           August 2020
# License:        GPL v3
#============================================
#!/usr/bin/env python3

import sys, getopt





def usage():
    print("csv2prolog usage:")
    print("  $ python3 csv2prolog -f [CSV_FILE] -p [PREFIX] -k |PKEY] C1:C4:C6")
    print("TBD")
    sys.exit(0)


def main():
    try:
        if len(sys.argv) == 1:
            usage()
        opts, args = getopt.getopt(sys.argv[1:], "f:p:k:hv", [])
    except getopt.GetoptError:
        # print help information and exit:
        usage()
    verbose = False
    csvfile = ""
    prefix = ""
    pkey = ""
    for o, a in opts:
        if o == "-v":
            verbose = True
            print("Verbose mode on")
        if o == "-h":
            usage()
        if o == "-f":
            csvfile = a
            if verbose: print("CSV file: " + a)
        if o == "-p":
            prefix = a
            if verbose: print("Prefix: " + a)
        if o == "-k":
            pkey = a
            if verbose: print("Primary key: " + a)
            
    


if __name__ == '__main__':
    main()
    
