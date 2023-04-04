import argparse
import requests
import threading
import re
from queue import Queue


print('''\
                                                                                    
                                                                                    
UUUUUUUU     UUUUUUUU        RRRRRRRRRRRRRRRRR           VVVVVVVV           VVVVVVVV
U::::::U     U::::::U        R::::::::::::::::R          V::::::V           V::::::V
U::::::U     U::::::U        R::::::RRRRRR:::::R         V::::::V           V::::::V
UU:::::U     U:::::UU        RR:::::R     R:::::R        V::::::V           V::::::V
 U:::::U     U:::::U           R::::R     R:::::R         V:::::V           V:::::V 
 U:::::D     D:::::U           R::::R     R:::::R          V:::::V         V:::::V  
 U:::::D     D:::::U           R::::RRRRRR:::::R            V:::::V       V:::::V   
 U:::::D     D:::::U           R:::::::::::::RR              V:::::V     V:::::V    
 U:::::D     D:::::U           R::::RRRRRR:::::R              V:::::V   V:::::V     
 U:::::D     D:::::U           R::::R     R:::::R              V:::::V V:::::V      
 U:::::D     D:::::U           R::::R     R:::::R               V:::::V:::::V       
 U::::::U   U::::::U           R::::R     R:::::R                V:::::::::V        
 U:::::::UUU:::::::U         RR:::::R     R:::::R                 V:::::::V         
  UU:::::::::::::UU   ...... R::::::R     R:::::R ......           V:::::V          
    UU:::::::::UU     .::::. R::::::R     R:::::R .::::.            V:::V           
      UUUUUUUUU       ...... RRRRRRRR     RRRRRRR ......             VVV            
                                                             @github.com/Fla4sh
                                                             @twitter : fla4sh403\
''')

def validate_urls(urls, ignore_empty, follow_redirects, response_range, valid_queue, invalid_queue, redirect_queue):
    for url in urls:
        url = url.strip()
        if ignore_empty and not url:
            continue
        try:
            response = requests.head(url, allow_redirects=follow_redirects, timeout=5)
            if response.status_code in response_range:
                valid_queue.put((url, response.status_code, "valid"))
            elif response.status_code >= 300 and response.status_code < 400:
                redirect_queue.put((url, response.status_code, response.headers.get("location")))
            else:
                invalid_queue.put((url, response.status_code, f">>>>Error: {response.reason}"))
        except requests.exceptions.RequestException as e:
            invalid_queue.put((url, "", f">>>>Error: {e}"))


def save_urls(queue, filename):
    with open(filename, 'w', encoding='utf-8') as outfile:
        while True:
            url_status = queue.get()
            if url_status is None:
                break
            outfile.write(f"{url_status[0]}\t{url_status[1]}\t{url_status[2]}\n")


def main(filename, ov, ox, e, f, r):
    with open(filename, 'r', encoding='utf-8') as infile:
        urls = infile.readlines()

    valid_queue = Queue()
    invalid_queue = Queue()
    redirect_queue = Queue()

    valid_thread = threading.Thread(target=save_urls, args=(valid_queue, ov))
    invalid_thread = threading.Thread(target=save_urls, args=(invalid_queue, ox))

    valid_thread.start()
    invalid_thread.start()

    validate_urls(urls, e, f, r, valid_queue, invalid_queue, redirect_queue)

    valid_queue.put(None)
    invalid_queue.put(None)

    valid_thread.join()
    invalid_thread.join()

    valid_count = valid_queue.qsize()
    invalid_count = invalid_queue.qsize()

    with open(ov, 'r', encoding='utf-8') as outfile:
        valid_lines = len(outfile.readlines())
    with open(ox, 'r', encoding='utf-8') as outfile:
        invalid_lines = len(outfile.readlines())

    print(f"{valid_lines} valid URLs written to {ov} ({valid_lines} lines)")
    print(f"{invalid_lines} invalid URLs written to {ox} ({invalid_lines} lines)")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Validate URLs in a file and write the results to separate files.')
    parser.add_argument('filename', help='input file name')
    parser.add_argument('--ov', default='valid.txt', help='output filename for valid URLs (default: %(default)s)')
    parser.add_argument('--ox', default='invalid.txt', help='output filename for invalid URLs (default: %(default)s)')
    parser.add_argument('--e', action='store_true', help='ignore empty lines')
    parser.add_argument('--f', action='store_true', help='follow redirects')
    parser.add_argument('--r', nargs=2, type=int, metavar=('LOWER', 'UPPER'), default=[200, 299], help='response code range for valid URLs (default: %(default)s)')
    args = parser.parse_args()
    main(args.filename, args.ov, args.ox, args.e, args.f, range(args.r[0], args.r[1] + 1))
