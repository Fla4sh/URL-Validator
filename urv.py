import argparse
import requests
import threading
import re


print('''\
UUUUUUUU     UUUUUUUURRRRRRRRRRRRRRRRR   VVVVVVVV           VVVVVVVV
U::::::U     U::::::UR::::::::::::::::R  V::::::V           V::::::V
U::::::U     U::::::UR::::::RRRRRR:::::R V::::::V           V::::::V
UU:::::U     U:::::UURR:::::R     R:::::RV::::::V           V::::::V
 U:::::U     U:::::U   R::::R     R:::::R V:::::V           V:::::V 
 U:::::D     D:::::U   R::::R     R:::::R  V:::::V         V:::::V  
 U:::::D     D:::::U   R::::RRRRRR:::::R    V:::::V       V:::::V   
 U:::::D     D:::::U   R:::::::::::::RR      V:::::V     V:::::V    
 U:::::D     D:::::U   R::::RRRRRR:::::R      V:::::V   V:::::V     
 U:::::D     D:::::U   R::::R     R:::::R      V:::::V V:::::V      
 U:::::D     D:::::U   R::::R     R:::::R       V:::::V:::::V       
 U::::::U   U::::::U   R::::R     R:::::R        V:::::::::V        
 U:::::::UUU:::::::U RR:::::R     R:::::R         V:::::::V         
  UU:::::::::::::UU  R::::::R     R:::::R          V:::::V          
    UU:::::::::UU    R::::::R     R:::::R           V:::V           
      UUUUUUUUU      RRRRRRRR     RRRRRRR            VVV     @github.com/Fla4sh\
''')




def validate_urls(urls, ignore_empty):
    valid_urls = []
    invalid_urls = []
    for url in urls:
        url = url.strip()
        if ignore_empty and not url:
            continue
        try:
            response = requests.head(url, allow_redirects=True, timeout=5)
            if response.status_code < 400:
                valid_urls.append(url)
            else:
                invalid_urls.append((url, f">>>>Error: {response.status_code} {response.reason}"))
        except requests.exceptions.RequestException as e:
            invalid_urls.append((url, f">>>>Error: {e}"))
    return valid_urls, invalid_urls

def main(filename, ov, ox, e):
    with open(filename, 'r', encoding='utf-8') as infile:
        urls = infile.readlines()
    valid_urls, invalid_urls = validate_urls(urls, e)
    with open(ov, 'w', encoding='utf-8') as outfile:
        outfile.write('\n'.join(valid_urls))
    with open(ox, 'w', encoding='utf-8') as outfile:
        for url_error in invalid_urls:
            outfile.write(f"{url_error[0]}\t{url_error[1]}\n")
    print(f"{len(valid_urls)} valid URLs written to {ov}")
    print(f"{len(invalid_urls)} invalid URLs written to {ox}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    parser.add_argument('--ov', default='valid.txt', help='output filename for valid URLs')
    parser.add_argument('--ox', default='invalid.txt', help='output filename for invalid URLs')
    parser.add_argument('--e', action='store_true', help='ignore empty lines')
    args = parser.parse_args()
    main(args.filename, args.ov, args.ox, args.e)
