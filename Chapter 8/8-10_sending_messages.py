def send_messages(messages, sent_messages):
    """Send a series of messsages to another list.."""
    while messages:
        sending = messages.pop()
        print(f"Sending: {sending}")
        sent_messages.append(sending)

def print_messages():
    print(sent_messages)
    print(messages)

messages = ['Hey there!', 'How are ya?', "What's up?", ]
sent_messages = []

send_messages(messages, sent_messages)
print_messages()