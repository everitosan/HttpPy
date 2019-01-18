from colorama import Fore

def log_main(*args, **kwargs):
    __print_colorama(Fore.CYAN, *args, **kwargs)

def log_success(*args, **kwargs):
    __print_colorama(Fore.GREEN, *args, **kwargs)

def log_accent(*args, **kwargs):
    __print_colorama(Fore.MAGENTA, *args, **kwargs)

def log_error(*args, **kwargs):
    __print_colorama(Fore.RED, *args, **kwargs)

def log_warning(*args, **kwargs):
    __print_colorama(Fore.YELLOW, *args, **kwargs)

def __print_colorama(color, *args, **kwargs) -> None:
    print("{}{}{}".format(color, *args, Fore.WHITE), **kwargs)
