import requests

url = 'https://zerotojunior.dev/cezar.txt'

response = requests.get(url)

# Sprawdź, czy żądanie zakończyło się sukcesem (kod odpowiedzi 200)
if response.status_code == 200:
    # Odczytaj zawartość pliku, uwzględniając odpowiednie kodowanie znaków
    text = response.content.decode('UTF-8', errors='ignore')
    print("Pobrany tekst:")
    print(text)
else:
    print(f"Błąd pobierania pliku: {response.status_code}")

small = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
large = "AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYZŹŻ"

shift = (-5)


new_text= []

for i in range(len(text)):
    if text[i].isalpha():
        if text[i].isupper():
            if text[i] in large:
                index = large.index(text[i])
                new_index = (index + shift) % len(large)
                new_text.append(large[new_index])
                #print(large[new_index])
        else:
            if text[i] in small:
                index = small.index(text[i])
                new_index = (index + shift) % len(small)
                new_text.append(small[new_index])
                #print(small[new_index])
    else:
        new_text.append(text[i])


print(' '.join(new_text))