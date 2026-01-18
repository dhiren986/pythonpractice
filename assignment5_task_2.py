numbers = list(range(1, 11))

extractedList =numbers[:5]

reversedList = extractedList.copy()

reversedList.reverse()
print("Original list:", numbers)
print("Extracted first five elements:", extractedList)
print("Reversed extracted elements:", reversedList)