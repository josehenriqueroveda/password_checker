# Password Checker

Tool to check the security of a password counting how many times it was leaked.

This script allows you to check a large amount of passwords and seeing how many times it has previously appeared in a data breach, using the **k-anonymity**  property.

> A strong password provides essential protection
> from financial fraud and identity theft.
> One of the most common ways that hackers
> break into computers is by guessing passwords.

### Usage

Password Checker requires [Python3](https://www.python.org/) to run.

Create a *.txt* file with the passwords to check, separating them with spaces or line breaks. For example:
> myperfectpassword123 dummypass 123456 
> qwert123 iLOVEmath mypass123 InGodWeTrust
> puppyDogz s3cur&password7 anotherdummy

With the *password_checker.py* file and the *passwords.txt* file in the same directory:
Run command in terminal.

```sh
python password_checker.py passwords.txt
```

#### Output
It's going to output each password tested:
```sh
123456 was found 23547453 times. You should change your password!
```
The above for passwords that can be compromised and the below for secure passwords so far:
```sh
s3cur&password7 was NOT found. It is a secure password at the moment!
```

**Did you like it?**
Follow me on [LinkedIn](https://www.linkedin.com/in/jhroveda/)
