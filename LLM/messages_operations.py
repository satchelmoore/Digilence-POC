import json

def add_message(conversation, role, content):
    new_message = {"role": role, "content": content}
    conversation.append(new_message)
    return conversation

def update_message(conversation, index, new_content):
    if 0 <= index < len(conversation):
        conversation[index]['content'] = new_content
    else:
        print("Invalid index.")
    return conversation

def delete_message(conversation, index):
    if 0 <= index < len(conversation):
        del conversation[index]
    else:
        print("Invalid index.")
    return conversation

def get_message_content(conversation, index):
    if 0 <= index < len(conversation):
        return conversation[index]['content']
    else:
        print("Invalid index.")
        return None


