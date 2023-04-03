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
python3 url.py filename.txt --e --ov valid.txt --ox invalid.txt
```

# Help

```
> filename: The path to the file containing the list of URLs to be validated. This argument is required.

> --ov: Optional argument to specify the output filename for valid URLs. The default value is valid.txt.

> --ox: Optional argument to specify the output filename for invalid URLs. The default value is invalid.txt.

> --e: Optional argument to indicate whether to ignore empty lines in the input file.
```
