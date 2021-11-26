language =['c','c++','python']
language_tuple=('java','cobol')
language_set={'.net','c##'}
language.extend(language_tuple)
print("The new language list:",language)
language.extend(language_set)
print("The new language list:",language)
