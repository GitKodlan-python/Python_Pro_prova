meme_dict = {
            "CRINGE": "Qualcosa di eccezionalmente strano o imbarazzante",
            "LOL": "Una risposta comune a qualcosa di divertente",
            "SHEESH": "leggera disapprovazione",
            "CREEPY": "spaventoso, inquietante",
            "PARA": "preoccuparsi per qualcosa, paranoiarsi"
            }

parola = input("Scrivi una parola che non capisci (usa solo lettere maiuscole!): ")

if parola in meme_dict.keys():
    # Cosa fare se la parola è stata trovata?
    print(meme_dict[])
else:
    # Cosa fare se la parola non è stata trovata?
    print("mi dispiace ma questa parola non esiste nel dizionario")
