l=["jack","app","banana","cat","doggy"]
sorted(l)
print("\nSorted by length:")
sorted_by_length = sorted(l, key=len)
for item in sorted_by_length:
    print(item)
