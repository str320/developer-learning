languages = ["python", "javascript", "go", "rust", "java"]

print(f"This is the first item of the list [{languages[0]}] | {languages}")
print(f"\nThis is the last item of the list [{languages[-1]}] | {languages}")

languages[0] = "c++"
print(f"\nThis is the new value of the first item [{languages[0]}] | {languages}")

languages.append("Django")
print(f"\nThis is the new item added to the end of the list [{languages[-1]}] | {languages}")

languages.insert(1, "python")
print(f"\nThis is the new item in the list at index 1 [{languages[1]}] | {languages}")

del languages[0]
print(f"\nThis is the list with one item deleted: {languages}")

item = languages.pop(-1)
print(f"\nThis is the item that was popped [{item}] | {languages}")

languages.remove("rust")
print(f"\nThis is the list with one item removed: {languages}")

print(f"\nThis is the list sorted: {sorted(languages)}")
print(f"\nThis is the list again {languages}")

languages.sort()
print(f"\nThis is the list sorted permanently: {languages}")

languages.reverse()
print(f"\nThis is the list reversed: {languages}")

languages.reverse()
print(f"\nThis is the list reversed back to original: {languages}")

print(f"This list has {len(languages)} languages: {languages}")

