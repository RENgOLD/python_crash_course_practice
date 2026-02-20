def get_formatted_name(first_name: object, last_name: object, middle_name: object = None) -> str:
    """Возвращает отформатированное полное имя."""
    if '' == False:
        print("'' == False")
    if None == False:
        print('None == False')
        
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)