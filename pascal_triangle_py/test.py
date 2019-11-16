from solution import PascalTriangle

if __name__ == "__main__":

    testcase = [5, 0]
    expected_results = [[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]], []]
    subject = PascalTriangle()

    results = map(subject.perform, testcase)
    for r in results:
        print r

    if expected_results == results:
        print "PASS"
    else:
        print "FAIL"


