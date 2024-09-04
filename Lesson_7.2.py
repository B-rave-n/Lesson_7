def correct_sentence(text):
    if text[0].islower() and text[-1] != '.':
        return f"{text.capitalize()}."
    elif text[0].islower():
        return f"{text.capitalize()}"
    elif text[-1] != '.':
        return f"{text}."
    else:
        return f"{text}"


assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
