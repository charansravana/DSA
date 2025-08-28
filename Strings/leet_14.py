def Longest_Common_prefix(strs):
    prefix=strs[0]
    for i in range(1, len(strs)):
        # Narrow down the prefix with each comparison
        while not strs[i].startswith(prefix):
            # Shorten prefix by one character
            prefix = prefix[:-1]
            # If prefix becomes empty → no common prefix
            if not prefix:
                return ""

    return prefix

#example usage
strs=["float","flower","flow","flight"]
print("Longest common prefix is : ", Longest_Common_prefix(strs))