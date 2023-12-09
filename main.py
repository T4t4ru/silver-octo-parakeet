import string
import random
import concurrent.futures
import os
import requests
from stem import Signal
from stem.control import Controller

def generate_domain(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def check_domain(domain):
    try:
     
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)

        response = requests.get(f'http://{domain}.onion')

        if response.status_code == 200:
            return True
        else:
            return False
    except Exception as e:
        print(f'Error: {e}')
        return False

def check_domains(domains):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(check_domain, domains))
    return results

domains = [generate_domain(i) for i in range(2, 549755813888)]
results = check_domains(domains)

if os.path.exists('result.txt'):

    os.remove('result.txt')

with open('result.txt', 'w') as f:
    for domain, result in zip(domains, results):
        if result:
            f.write(f'The domain {domain}.onion is available\n')
        else:
            f.write(f'The domain {domain}.onion is unavailable\n')
