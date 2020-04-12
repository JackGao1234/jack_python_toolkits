HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

def print_warn(*args):
    _just_print(WARNING, *args)

def print_header(*args):
    _just_print(HEADER, *args)

def print_green(*args):
    _just_print(OKGREEN, *args)

def print_bold(*args):
    _just_print(BOLD, *args)


def _just_print(level, *args):
    print(level, end="")
    print(*args, end="")
    print(ENDC)
