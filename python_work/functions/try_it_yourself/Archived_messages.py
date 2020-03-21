def send_messages(unsent_messages, sent_messages):
	while unsent_messages:
		current_messages = unsent_messages.pop()
		print(f"Sending messages: {current_messages}")
		sent_messages.append(current_messages)


def show_messages(sent_messages):
	print(f"\nThis messages has been sent:")
	for message in sent_messages:
		print(message.title())

unsent_messages = ['i love you', 'what is my name', 'i am a girl']
sent_messages = []

send_messages(unsent_messages[:], sent_messages)
show_messages(sent_messages)

print(f"\n{unsent_messages}")
print(f"\n{sent_messages}")