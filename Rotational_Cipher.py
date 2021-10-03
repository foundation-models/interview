import math
# Add any extra import statements you may need here


def rotate(char, min, max, rotation_factor):
  if min > char or max < char:
    return char
  else:
    remainder = ((ord(char) + rotation_factor - ord(min)) % (ord(max) - ord(min) + 1))  + ord(min) 
    return chr(remainder)


def rotationalCipher(input, rotation_factor):
  result = ""
  for char in input:
    char = rotate(char, '0', '9', rotation_factor)
    char = rotate(char, 'a', 'z', rotation_factor)
    char = rotate(char, 'A', 'Z', rotation_factor)
    result += char
  return result



# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom.

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  printString(">>" + rotationalCipher("AByzYZ", 3))
  
  if True:

    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

  # Add your own test cases here
  