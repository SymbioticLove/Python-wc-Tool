#!/usr/bin/env python3
import sys

def ccwc(filename=None, option='-c'):
    # Read from standard input if no filename is provided
    if filename is None:
        content = sys.stdin.read()
    else:
        with open(filename, 'r', encoding="utf-8") as file:
            content = file.read()

    # Count bytes
    if option == '-c':
        return (len(content.encode("utf-8")),)
    
    # Count lines
    elif option == '-l':
        return (len(content.splitlines()),)
    
    # Count words
    elif option == '-w':
        return (len(content.split()),)
    
    # Count characters
    elif option == '-m':
        return (len(content),)
    
    # Default option
    else:
        byte_count = len(content.encode("utf-8"))
        line_count = len(content.splitlines())
        word_count = len(content.split())
        return line_count, word_count, byte_count

def main():
    # Parse command-line arguments
    args = sys.argv[1:]
    
    # No arguments provided
    if not args:
        results = ccwc()
        for result in results:
            print(result)
    
    # One argument provided (could be option or filename)
    elif len(args) == 1:
        # Check if the provided argument is an option or filename
        if args[0].startswith('-'):
            print(ccwc(option=args[0])[0])
        else:
            results = ccwc(filename=args[0], option='-l')
            print(results[0])
            print(ccwc(filename=args[0], option='-w')[0])
            print(ccwc(filename=args[0], option='-c')[0])
    
    # Two arguments provided (option and filename)
    else:
        option = args[0]
        filename = args[1]
        
        # If the default option is provided
        if option not in ['-c', '-l', '-w', '-m']:
            results = ccwc(filename)
            for result in results:
                print(result)
        else:
            print(ccwc(filename, option)[0])

main()
