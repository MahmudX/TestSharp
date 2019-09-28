import platform


def Message():
    version = platform.python_version()
    print("Hello World.")
    print(f'Python Ver - {version}')
def main():
    Message()

if __name__ == "__main__": main()

