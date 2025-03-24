# Pick Toys in one line max two types of toys

def pickToys(arr):
    i = 0
    hmap = {}
    mx = 0

    for j in range(len(arr)):
        char = arr[j]
        hmap[char] = hmap.get(char, 0) + 1

        # Shrink the window if more than 2 types of toys are present
        while len(hmap) > 2:
            left_char = arr[i]
            hmap[left_char] -= 1
            if hmap[left_char] == 0:
                del hmap[left_char]
            i += 1

        # Update the maximum length whenever the window is valid (len(hmap) <= 2)
        mx = max(mx, j - i + 1)

    return mx

print(pickToys("abaccab"))  # Output: 4 ("acca")