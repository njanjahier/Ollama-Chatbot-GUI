Lokalni LLM Chatbot: Demonstracija Ollama API Integracije
Ovaj projekat predstavlja Python desktop aplikaciju kreiranu sa ciljem demonstracije vještine integracije Velikih Jezičnih Modela (LLM) u prilagođena rješenja. Aplikacija koristi Ollama API za lokalnu interakciju sa LLM-ovima (npr. Mistral, Llama 3) i Tkinter za izradu korisničkog interfejsa.

Ključne Vještine i Tehnička Vrijednost
Ovaj projekat je dizajniran da prikaže sljedeće vještine relevantne za IT Konsalting i Data Science pozicije:

API Integracija i Lokalno Hostovanje: Korištenje Ollama API-ja (umjesto gotovih cloud servisa) pokazuje razumijevanje lokalnog implementiranja i integracije ML modela u funkcionalni softver.

Sistematska Konfiguracija: Primjena System Prompt-a i mogućnost promjene modela (MODEL = "mistral") demonstrira vještinu rada sa softverskim rješenjima koja su lako konfigurabilna i prilagodljiva potrebama klijenta.

Sigurnosna Praksa (Best Practice): Korištenje .gitignore fajla za zaštitu osjetljivih ključeva i podataka (npr. .env i chat_history.txt).

GUI Razvoj (Frontend): Korištenje Tkinter biblioteke za kreiranje funkcionalnog korisničkog interfejsa.

Tehničke Specifikacije
Komponenta	Tehnologija/Biblioteka	Napomena
Glavni Jezik	Python	Standardni programski jezik.
LLM Integracija	Ollama	Python klijent za interakciju s lokalno hostovanim LLM-ovima.
Korisnički Interfejs	Tkinter	Ugrađena Python biblioteka za izradu GUI-a.
Logika	ollama_gui_chatbot.py	Upravlja lančanim razgovorom, kontekstom i čuvanjem historije.

Izvezi u Tablice
Uputstvo za Pokretanje
Da biste pokrenuli aplikaciju, potrebno je da imate instaliran Python 3 i da slijedite ove korake:

Instalirajte Ollamu: Preuzmite i instalirajte Ollama Desktop aplikaciju (https://ollama.com).

Pokrenite Model: Otvorite terminal i preuzmite model po izboru (npr. Mistral):

Bash

ollama pull mistral
Instalirajte Python biblioteke:

Bash

pip install -r requirements.txt
Pokrenite Aplikaciju:

Bash

python ollama_gui_chatbot.py
Autor: Sanja Savić | Godina: 2025.
