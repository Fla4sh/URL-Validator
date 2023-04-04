# URV.py
## Description
This Python script checks a list of URLs for validity and writes the valid URLs to one file and the invalid URLs to another file. The script takes a filename as input and allows the user to specify output filenames for the valid and invalid URLs. The script uses the requests library to send HEAD requests to each URL and checks the response status code. URLs with status codes less than 400 are considered valid and are written to the valid URLs file. URLs with status codes of 400 or higher, or URLs that fail to connect, are considered invalid and are written to the invalid URLs file with an error message. The script also includes an option to ignore empty lines in the input file.

# Installation

To install URV, clone the repository and run the following command:
```
git clone https://github.com/Fla4sh/URL-Validator.git
pip3 install -r requirements.txt
```

# Usage:
![urv](https://user-images.githubusercontent.com/113174416/229416120-2f65eaf4-4e71-4629-a1da-85451707134c.png)


# One Line Command:

```
python script_name.py input_file_name [--ov output_valid_file_name] [--ox output_invalid_file_name] [--e] [--f] [--r LOWER_RANGE UPPER_RANGE]

```

# Help

```
> -h or --help: To view the help message
> --ov: this option specifies the output filename for the valid URLs. If not specified, the default filename is "valid.txt".
> --ox: this option specifies the output filename for the invalid URLs. If not specified, the default filename is "invalid.txt".
> --e: this option is a flag that indicates whether to ignore empty lines in the input file. If specified, empty lines will be skipped.
> --f: this option is a flag that indicates whether to follow redirects. If specified, redirects will be followed.
> --r: this option specifies the range of response codes that are considered valid. By default, the range is 200-299. For example, if the user wants to consider any response code between 400 and 499 as valid, they can use the option --r 400 499.

```
