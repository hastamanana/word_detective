import string


a = [i for i in string.ascii_uppercase]
print(a, len(a))

LATIN_GLAS = [i for i in 'AEIOUY']
print(LATIN_GLAS)


print(a - (a & LATIN_GLAS), len(a - (a & LATIN_GLAS)))

