import time

from adam.file import  read_module
from adam.lex import scanner
from adam.syntax import parser
from adam.semantic import generator
from adam.run import driver_file

vars_file = "adam/nateve_vars"

def build(file, args = ["none"],  main = "", exceptions = "\tpass", driver = ""):

    dev_mode = "dev" in args
    verbose_mode = ("-v" in args) or ("--verbose" in args)
    display_status_mode = verbose_mode or dev_mode

    start = time.time()

    module = read_module(file)
    file = file.split(".")[0]

    start_compilation = time.time()

    tokens, errors, lex_log, templates = scanner(module, args)
    tree, tokens, errors = parser(tokens, file, errors)
    errors = generator(tree, file, errors, main, exceptions, args, templates)

    if display_status_mode:
        now = time.time()
        compilation_time = now - start_compilation

        log = lex_log

        if errors != 0:
            stat = -1
            
        else:
            stat = 0

        print(f"Compilation finished with status {stat}")
        
        print(log, end = "")

    if dev_mode:
        print(tokens)
        tree.display()

    if display_status_mode:
        now = time.time()
        runtime = now - start
    
        try:
            f = open(vars_file)
            miliseconds = f.read().strip()
            f.close()

        except:
            miliseconds = "True"

        if miliseconds == "True":
            print(f"Machine time: {1000 * runtime} miliseconds")
            print(f"Compilation time: {1000 * compilation_time} miliseconds\n")

        else:
            print(f"Machine time: {runtime} seconds")
            print(f"Compilation time: {compilation_time} seconds\n")
    
    f = open(driver_file + ".py", "w")
    f.write(driver.format(file))
    f.close()

    return file
