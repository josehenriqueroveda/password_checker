import requests
import hashlib
import sys

def request_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error: {res.status_code} - Check the API docs and try again')
    return res


def get_password_leaks(hashes, hash_tail):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, leaks in hashes:
        if h == hash_tail:
            return leaks
    return 0


def check_api_passwords(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    five_chars, tail = sha1password[:5],  sha1password[5:]
    response = request_data(five_chars)
    return get_password_leaks(response, tail)


def main(pw_file):
    try:
        with open(f'./{pw_file}', mode='r') as pw_list:
            for line in pw_list:
                for password in line.split():
                    count = check_api_passwords(password)
                    if count:
                        print(f'{password} was found {count} times. You should change your password!')
                    else:
                        print(f'{password} was NOT found. It is a secure password at the moment!')
            return
    except FileNotFoundError as e:
        print(f'Check again the file path! {e}')


if __name__ == '__main__':
    sys.exit(main(sys.argv[1]))