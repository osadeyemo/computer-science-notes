guest_list = ['Ali', 'Mom', 'Rohn']
message = "would you like to have dinner with me tonight?"
print(f"Hello Mr. {guest_list[0]}, {message}")
print(f"Hello {guest_list[1]}, {message}")
print(f"Hello Mr. {guest_list[2]}, {message}")

print(f"Hello Mr. {guest_list[0]}, {guest_list[1]}, and Mr. {guest_list[2]}, I found a bigger table to accomordate more people.")
guest_list.insert(0, 'Wale')
print(guest_list)
guest_list.insert(2, 'Mary')
print(guest_list)
guest_list.append('Labi')
print(guest_list)
print(f"\nHello Mr. {guest_list[0]}, {message}")
print(f"\nHello Mr. {guest_list[1]}, {message}")
print(f"\nHello Mrs. {guest_list[2]}, {message}")
print(f"\nHello {guest_list[3]}, {message}")
print(f"\nHello Mr. {guest_list[4]}, {message}")
print(f"\nHello Mr. {guest_list[5]}, {message}")
print(guest_list)

message = f"I am inviting {len(guest_list)} people to dinner."
print(message)


