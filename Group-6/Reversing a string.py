text = "hello"
reversed_text = ""
index = len(text) - 1

while index >= 0:
    reversed_text += text[index]
    index -= 1

print(f"The reversed string is '{reversed_text}'")
