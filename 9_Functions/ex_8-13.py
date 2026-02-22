# 8.13. Профиль. Начните с копии программы user_profile.py, приведенной в
# этом подразделе. Создайте собственный профиль с помощью вызова
# build_profile(),укажите имя, фамилию и три другие пары «ключ — значение»
# для вашего описания.

def build_profile(first, last, **user_info):
    """Создает словарь, содержащий информацию о пользователе."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info
user_profile = build_profile('firstname', 'lastname',
                             profession='profession',
                             location='location')
print(user_profile)
