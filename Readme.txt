1)Install python3
macos : brew install python
windows: Please follow the instructions https://www.python.org/downloads/windows/
2)Install pytest to run unit test
pip3 install -U pytest
3)Verify pytest installation
pytest --version
4)Clone the repository
git clone https://github.com/sanzzz/home_coding_challenge.git
cd home_coding_challenge

5)To run the pytest, run the following command
pytest

6)To execute the program 

echo "abc123" | python3 myProg

echo "abc123" | python3 myProg -x

echo "qq" | python3 myProg

echo "abc123" > file.tmp
python3 myProg -f file.tmp

7)To execute the script using different values
Usage:

i)Adding input digits
python3 myProg
465  - Enter the number
15

ii)Adding hexadecimal digits in decimal 
python3 myProg -x
Number: b34
18


iii)Adding digits in file
python3 myProg -f file.tmp
6
