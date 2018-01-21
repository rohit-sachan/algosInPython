segments = [(3,'a'), (1,'c'), (1,'b'), (4,'a')]
sortedSegment = sorted(segments, key= lambda x : (x[0],x[1]), reverse=True)

print(sortedSegment)