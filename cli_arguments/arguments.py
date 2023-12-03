import sys
import argparse

def main(argv):
   # Parser creation
   argParser = argparse.ArgumentParser()

   # Add as many add_argument() as needed
   argParser.add_argument("-n", "--name", help="your name")

   # Parsing
   # Note that the -h option is automagically created
   args = argParser.parse_args(argv)

   print("args=%s" % args)
   print("args.name=%s" % args.name)

if __name__ == "__main__":
   main(sys.argv[1:])
