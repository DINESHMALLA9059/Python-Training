from collections import Counter

def odd_occur(lst):
    count = Counter(lst)
    odd_occur_elements = []

    for element, cnt in count.items():
        if cnt%2!=0:
            odd_occur_elements.append(element)
    
    return odd_occur_elements
l1=[1,2,2,3,3,4,5,1,1,2,4,5]
result = odd_occur(l1)
print("Elements with odd occurrences:", result)
