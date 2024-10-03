from contextlib import contextmanager

@contextmanager
def file_context_manager(filename):
    file = open(filename, 'r')
    try:
        yield file
    finally:
        file.close()

...

with file_context_manager('sample.txt') as file:
    print(file.read())