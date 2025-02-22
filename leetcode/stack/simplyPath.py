# Simply Path 

# Path must start with '/'

# Directories within the path must be separated 
# by exactly one slash '/'.

# The path must not end with a slash '/'
#, unless it is the root directory.

# The path must not have any single or double periods ('.' and '..') 
#used to denote current or parent directories.



def simplyPath(path):

	st = []

	for ch in path.split('/'):
		print(ch)

		if not ch or ch == ".":
			continue

		elif ch == "..":
			if st:
				st.pop()

		else:
			st.append(ch)
		print(st)

	return "/" + "/".join(st)
	




print(simplyPath("/home/"))

print(simplyPath("/home//foo/"))

print(simplyPath("/home/user/Documents/../Pictures"))