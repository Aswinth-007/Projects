def calculate_flames(name1, name2):
    name1 = name1.lower().replace(" ", "")
    name2 = name2.lower().replace(" ", "")
    
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, "", 1)
            name2 = name2.replace(char, "", 1)
    
    combined_length = len(name1) + len(name2)
    flames = ['Friends', 'Lovers', 'Affection', 'Marriage', 'Enemies', 'Siblings']
    
    while len(flames) > 1:
        index = (combined_length % len(flames)) - 1
        if index >= 0:
            flames = flames[index+1:] + flames[:index]
        else:
            flames = flames[:len(flames)-1]
    
    return flames[0]

# Get input from the user
name1 = input("Enter the first name: ")
name2 = input("Enter the second name: ")

# Calculate and display the result
result = calculate_flames(name1, name2)
print("Relationship status:", result)
