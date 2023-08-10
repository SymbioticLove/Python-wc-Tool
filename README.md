## Architecture Overview for Python
Python is an interpreted, high-level, general-purpose programming language. It has a design philosophy which emphasizes code readability, and a syntax which allows programmers to express concepts in fewer lines of code than might be possible in languages such as C++ or Java. The Python runtime takes care of many of the underlying operations, such as memory management.

For this project, we'll use Python's standard library, which provides a wide array of functionalities. Specifically, we'll be using the `sys` module to handle command line arguments and basic file operations to count the bytes.

# Custom Count Word Character (CCWC) Script Documentation

The `ccwc` script is designed to count various textual elements (lines, words, characters, bytes) of a given text file or standard input.

## Usage

```bash
ccwc [option] [filename]
```

### Arguments

1. `option`: (Optional) Specifies what you want to count. Can be one of:
    - `-c`: Count bytes
    - `-l`: Count lines
    - `-w`: Count words
    - `-m`: Count characters
    - If no option is provided, the default behavior is to count lines, words, and bytes.
2. `filename`: (Optional) Path to the file you want to analyze. If no filename is provided, the script reads from standard input.

### Examples

1. Count bytes of a given file:
    ```bash
    ccwc -c sample.txt
    ```

2. Count lines, words, and bytes of a given file:
    ```bash
    ccwc sample.txt
    ```

3. Count lines from standard input:
    ```bash
    echo "Hello World" | ccwc -l
    ```

## Note

- The script assumes that the text file is encoded in UTF-8.
- If no arguments are provided, the script will read from standard input and count lines, words, and bytes.
