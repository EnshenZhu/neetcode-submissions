class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for single_str in strs:
            length = len(single_str)
            res += str(length) + "#" + single_str
        return res

    def decode(self, s: str) -> List[str]:
        print(s)
        res = []
        ptr = 0  # to track the input s
        while ptr < len(s):
            # get the str element lenght
            str_e_length = 0
            while s[ptr] != "#":
                str_e_length = str_e_length * 10 + int(s[ptr])
                ptr += 1

            # obtain the string element and append it to the res
            str_e = s[ptr + 1 : ptr + 1 + str_e_length]
            res.append(str_e)

            # handle the ptr jumping after appending the string element
            ptr += 1 + str_e_length

        return res
