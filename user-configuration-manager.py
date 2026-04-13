test_settings = {
    'Theme': 'dark',
    'Notifications': 'enabled',
    'Volume': 'high'
}

def add_setting(settings, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_s, new_setting):
    key, value = new_setting
    key = key.lower()
    value = value.lower()
    if key in settings_s:
        settings_s[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_new, key):
    key = key.lower()
    if key not in settings_new:
        return 'Setting not found!'
    else:
        del settings_new[key]
        return f"Setting '{key}' deleted successfully!"

def view_settings(dictionary):
    if not (dictionary):
        return 'No settings available.'
    else:
        return_str = ("Current User Settings:\n")
        for item in dictionary.items():
           
            for i in [0,1]:           
                if i == 0:
                    return_str = return_str + item[i].capitalize() + ': '                  
                if i == 1:
                    return_str = return_str + item[i] + '\n'                    
    return return_str
settings_in_test = {"theme": "light", "language": "English", "notifications": "enabled"}
result = view_settings(settings_in_test)
print(result)
