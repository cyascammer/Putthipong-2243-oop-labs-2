'''
Putthipong Phukhansung 
633040224-3
'''

txt = input("Enter text: ")
pattern_input = input("Enter pattern: ")
position = txt.find(pattern_input)

if position == -1:
    print(f"Cannot find {pattern_input} in {txt}")
else:
    print(f"Found {pattern_input} in {txt} at {position}")
