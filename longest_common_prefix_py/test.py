from solution import LongestCommonPrefix

if __name__ == "__main__":

    testcase_list = [["app", "apple", "appless"], 
                    ["abc", "dcc", "ball"], 
                    ["apl", "apbb", "apble"], 
                    [],
                    ["aac","bb","bc","b","caca"]]
    expected_results = ["app", "", "ap", "", ""]
    subject = LongestCommonPrefix()

    result = map(subject.perform, testcase_list)

    for i in range(0, len(testcase_list)):
        print "{} : {} : {}".format(testcase_list[i], expected_results[i], result[i])

    if result == expected_results:
        print "PASS"
    else:
        print "FAIL"

