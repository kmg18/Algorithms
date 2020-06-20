class LCS(object):

    def longest_common_string_recursive_helper(self, str1, str2, pos1, pos2, check_equal):
        if pos1 == -1 or pos2 == -1:
            return 0

        if check_equal:
            if str1[pos1] == str2[pos2]:
                return 1 + self.longest_common_string_recursive_helper(str1, str2, pos1 - 1, pos2 - 1, True)
            else:
                return 0

        longest = 0     # start (again) to find the longest from the current positions
        if str1[pos1] == str2[pos2]:
            longest = 1 + self.longest_common_string_recursive_helper(str1, str2, pos1 - 1, pos2 - 1, True)

        return max(longest,
                   self.longest_common_string_recursive_helper(str1, str2, pos1, pos2 - 1, False),
                   self.longest_common_string_recursive_helper(str1, str2, pos1 - 1, pos2, False))


    def longest_common_substring_recursive(self, str1, str2):
        return self.longest_common_string_recursive_helper(str1, str2, len(str1) - 1, len(str2) - 1, False)


    def longest_common_substring(self, str1, str2):
        cols = len(str1) + 1     # Add 1 to represent 0 valued col for DP
        rows = len(str2) + 1     # Add 1 to represent 0 valued row for DP

        T = [[0 for _ in range(cols)] for _ in range(rows)]

        max_length = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if str2[i - 1] == str1[j - 1]:
                    T[i][j] = T[i - 1][j - 1] + 1
                    max_length = max(max_length, T[i][j])

        return max_length


if __name__ == '__main__':
    str1 = "nanmukesnanihani"
    str2 = "nani"
    obj = LCS()

    print(obj.longest_common_substring_recursive(str1, str2))
