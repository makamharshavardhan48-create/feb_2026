#mini project of dicionary
#Name: harshavardhan
dictionary = {}
while True:
    print("\nDictionary Management system")
    print("1. Add a word")
    print("2. Search for maning")
    print("3. Display All Words")
    print("4. Update Meaning")
    print("5. Delete word")
    print("6. Exit")
    
    choice = input("enter your choice:")
    
    if choice =="1":
        word = input("enter the word: ").lower()
        meaning = input("enter the meaning: ")
        dictionary[word] = meaning
        print("word added successfully!")
    elif choice =="2":
        word = input("enter the word to search: ").lower()
        if word in dictionary:
            print("meaning:",dictionary[word])
        else:
            print("word not found in the dictionary.")
    elif choice =="3":
        if dictionary:
            print("Words and their meanings:") 
            for word, meaning in dictionary.i():
                print(f"{word}:{meaning}")  
        else:
            print("dictionary is empty.")
    elif choice =="4":
        word = input("enter the word to update meaning: ").lower()
        if word in dictionary:
            new_meaning = input("enter the new meaning: ")
            dictionary[word] = new_meaning
            print("meaning updated successfully!")
            print("updated meaning:", dictionary[word])
        else:
            print("word not found in the dictionary.")
    elif choice =="5":
        word = input("enter the word to delete: ").lower()
        if word in dictionary:
            del dictionary[word]
            print("word deleted successfully! ")
        else:
            print("word not found in the dictionary.")
    elif choice =="6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice! pllease enter a valid option.")
        
    
    
    
    