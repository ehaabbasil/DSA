  def merge(intervals):
  	# o (nlogn)
  	intervals.sort(key = lambda i : i[0])
  	output = [intervals[0]]


  	for start, end in intervals[1:]:
  		# how do we know it is overlapping 

  		lastEnd = output[-1][1]  # end value of most recent interval

  		if start <= lastEnd: # means overlapping now merge
  			output[-1][1] = max(lastEnd, end)
  		else:
  			output.append(start,end)

  			# [1,5] ,  [2,4] result in [1,5]





