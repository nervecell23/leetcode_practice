from solution import PascalTriangle

if __name__ == "__main__":

    testcase = 5
    expected_result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    subject = PascalTriangle()
    result = subject.perform(testcase)

    print result

    if expected_result == result:
        print "PASS"
    else:
        print "FAIL"


