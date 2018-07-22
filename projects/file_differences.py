"""
Project for Week 4 of "Python Data Representations".
Find differences in file contents.

Be sure to read the project description page for further information
about the expected behavior of the program.
"""

IDENTICAL = -1

def singleline_diff(line1, line2):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
    Output:
      Returns the index where the first difference between
      line1 and line2 occurs.

      Returns IDENTICAL if the two lines are the same.
    """
    len1 = len(line1)
    len2 = len(line2)
    minor_len = len2 if len1 > len2 else len1

    for index in range(0, minor_len):
        if line1[index] != line2[index]:
            return index

    return IDENTICAL if len1 == len2 else minor_len



## tests
def test(message, result, expected_result):
    success = "yes" if result == expected_result else "ERROR!"
    print(message, "result:", result, "success?:", success)

print(">>>> testing singleline_diff")
test("identical lines:", singleline_diff("aaa", "aaa"), IDENTICAL)
test("different lines:", singleline_diff("aba", "aaa"), 1)
test("different first line is greater:", singleline_diff("abaaaa", "aaaa"), 1)
test("different and second line is greater:", singleline_diff("012345", "01234?6"), 5)
test("same chars but fisrt line is greater:", singleline_diff("012345", "0123456"), 6)
test("same chars but second line is greater:", singleline_diff("01234567", "012345"), 6)



def singleline_diff_format(line1, line2, idx):
    """
    Inputs:
      line1 - first single line string
      line2 - second single line string
      idx   - index at which to indicate difference
    Output:
      Returns a three line formatted string showing the location
      of the first difference between line1 and line2.

      If either input line contains a newline or carriage return,
      then returns an empty string.

      If idx is not a valid index, then returns an empty string.
    """
    return ""


def multiline_diff(lines1, lines2):
    """
    Inputs:
      lines1 - list of single line strings
      lines2 - list of single line strings
    Output:
      Returns a tuple containing the line number (starting from 0) and
      the index in that line where the first difference between lines1
      and lines2 occurs.

      Returns (IDENTICAL, IDENTICAL) if the two lists are the same.
    """
    return (IDENTICAL, IDENTICAL)


def get_file_lines(filename):
    """
    Inputs:
      filename - name of file to read
    Output:
      Returns a list of lines from the file named filename.  Each
      line will be a single line string with no newline ('\n') or
      return ('\r') characters.

      If the file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    return []


def file_diff_format(filename1, filename2):
    """
    Inputs:
      filename1 - name of first file
      filename2 - name of second file
    Output:
      Returns a four line string showing the location of the first
      difference between the two files named by the inputs.

      If the files are identical, the function instead returns the
      string "No differences\n".

      If either file does not exist or is not readable, then the
      behavior of this function is undefined.
    """
    return ""