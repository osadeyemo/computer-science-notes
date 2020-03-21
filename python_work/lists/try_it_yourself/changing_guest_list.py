guest_list = ['Ali', 'Mom', 'Rohn']
message = "would you like to have dinner with me tonight?"
print(f"Hello Mr. {guest_list[0]}, {message}")
print(f"Hello {guest_list[1]}, {message}")
print(f"Hello Mr. {guest_list[2]}, {message}")
print(f'''\nSorry Mr. {guest_list[-1]} can't make it to dinner tonight.''')
guest_list[-1] = 'Dana'
print(guest_list)
print(f"\nHello Mr. {guest_list[0]}, {message}")
print(f"\nHello {guest_list[1]}, {message}")
print(f"\n\tHello Mrs. {guest_list[2]}, {message}")

