import sys
import data_validator

if len(sys.argv) != 2:
    print("Usage: python date_validator.py DD.MM.YYYY")
    sys.exit(1)

date_input = sys.argv[1]

if data_validator.is_valid_date(date_input):
    print('True')
else:
    print('False')


