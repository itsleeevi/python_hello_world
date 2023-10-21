def helloWorldBot(command):
    if command == "/whatsup":
        return "Hello!"
    else:
        return "I don't understand that command."

# Test
user_input = input("Enter your command: ")
response = helloWorldBot(user_input)
print(response)