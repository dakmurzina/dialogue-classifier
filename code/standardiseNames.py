def rename_characters(name):
    if name in ['Raj)', 'Koothrappali', 'Rai', 'Rajj', 'Ra']:
        name = name.replace(name, 'Raj')
        return name
    elif name in ['Leonard)', 'Leonard-warrior', 'Hofstadter', 'Leonard:', 'Leoanard']:
        name = name.replace(name, 'Leonard')
        return name
    elif name in ['Sheldon)', 'Cooper', 'Cooper)', 'Shedon', 'Shldon', 'Sehldon', 'Sgeldon', 'Sheldon-bot']:
        name = name.replace(name, 'Sheldon')
        return name
    elif name in ['Penny)', 'Penny(leaving)', 'Penny-warrior']:
        name = name.replace(name, 'Penny')
        return name
    elif name in ['Howard)', 'Wolowitz', 'Wolowitz)', 'Howatd']:
        name = name.replace(name, 'Howard')
        return name
    else:
        return name