class LongestCommonPrefix:
    def perform(self, strs):

        if strs == []:
            return ""

        strs.sort(key=len)

        prefix = ""

        first_word = strs[0]
        rest_words = strs[1:len(strs)]

        for idx, char in enumerate(first_word):

            for word in rest_words:

                if word[idx] != char:
                    return prefix

            prefix += char

        return prefix

