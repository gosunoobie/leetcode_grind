
# encode and decode strings - medium

class Soultion:
    
    def encode(self, strs):
        res = ""

        # make the string on the format of 4#asdf5#asdfg

        for s in strs:
            res += str(len(s)) + "#" + s 
        return res

    def decode(self, str):
        res, i = [], 0

        while i < len(str):
            j = i
            # increment j until it finds the #
            while str[j] != "#":
                j += 1

            # get the actual number i.e from 4#asdf get 4
            length = int(str[i : j])
            #get the substring from the # to the length of the string
            res.append(str[ j + 1: j + 1 + length])
            # set the i to the end of the string
            i = j + 1 + length
        return res

