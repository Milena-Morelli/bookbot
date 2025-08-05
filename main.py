from stats import print_final
import sys

try:
    print_final(sys.argv[1])
except Exception as e:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)