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

print(f"\nTo {guest_list[0]}, {guest_list[1]}, {guest_list[2]}, {guest_list[3]}, {guest_list[4]}, and {guest_list[5]}, sorry I can only invite 2 people to dinner tonight.")

guest_wale = guest_list.pop(0)
print(f"\nSorry {guest_wale}, I can't invite you to dinner tonight.")

print(f"\n{guest_list}")

guest_ali = 'Ali'
guest_list.remove(guest_ali)
print(f"\nSorry {guest_ali}, I can't invite you to dinner tonight.")

guest_rohn = 'Rohn'
guest_list.remove(guest_rohn)
print(f"\nSorry {guest_rohn}, I can't invite you to dinner tonight.")

guest_labi = 'Labi'
guest_list.remove(guest_labi)
print(f"\nSorry {guest_labi}, I can't invite you to dinner tonight.")

message = "you are still invited to dinner tonight."

print(f"\n{guest_list}")

print(f"\nHello {guest_list[0]}, {message}")
print(f"\nHello {guest_list[1]}, {message}")

del guest_list[0]
del guest_list[0]
print(guest_list)