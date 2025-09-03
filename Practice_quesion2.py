def permute(s, l, r):
    if l == r:
        print("".join(s))
    else:
        for i in range(l, r + 1):
            # Swap current index with l
            s[l], s[i] = s[i], s[l]
            
            # Recurse for the rest
            permute(s, l + 1, r)
            
            s[l], s[i] = s[i], s[l]

# Example usage
string = "abc"
permute(list(string), 0, len(string) - 1)
