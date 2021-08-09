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

echo "abc123" | ./myProg

echo "abc123" | ./myProg -x

echo "qq" | ./myProg

echo "abc123" > file.tmp
./myProg -f file.tmp

7)To execute the script using different values
Usage:

i)Adding input digits
./myProg
465  - Enter the number
15

ii)Adding hexadecimal digits in decimal 
./myProg -x
Number: b34
18


iii)Adding digits in file
./myProg -f file.tmp
6
