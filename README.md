# Overview

This script is designed to check the availability of onion domains. It generates random domain names, checks if they exist, and saves the results to a text file. The script also includes a check to see if the `result.txt` file already exists, and if it does, it deletes it before writing to it.

## Requirements

- Python 3.6 or higher
- The `dns.resolver`, `string`, `random`, `concurrent.futures`, `os`, `requests`, `stem`, and `stem.control` Python libraries
- A running instance of TOR with the control port set to 9051

## How to Run

1. Make sure you have Python 3.6 or higher installed on your machine.
2. Install the required Python libraries by running `pip install dnspython requests stem` in your terminal.
3. Make sure you have a running instance of TOR with the control port set to 9051.
4. Save the script to a file, for example `check_domains.py`.
5. Run the script by executing `python check_domains.py` in your terminal.

## What the Script Does

The script works as follows:

1. It generates a list of random domain names.
2. It checks each domain to see if it exists.
3. It saves the results to a text file named `result.txt`.
4. If the `result.txt` file already exists, it deletes it before writing to it.
5. It uses the TOR network to check the availability of the domains.

## Output

The script outputs a text file named `result.txt` in the same directory as the script. Each line in the file corresponds to a domain that was checked, and indicates whether the domain was available or not.
