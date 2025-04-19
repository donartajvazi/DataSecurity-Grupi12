# Vigenere cipher duke gjeneruar celes nga keystream duke perdorur nje int32 ose string si seed

## Përshkrimi
Ky projekt implementon algoritmin klasik të Vigenère për enkriptim dhe dekriptim të mesazheve tekstuale. Risi e këtij implementimi është gjenerimi dinamik i çelësit (keystream) duke përdorur një `int32` ose `string` si seed, duke siguruar kështu një nivel shtesë të sigurisë dhe përshtatshmëri për aplikime të ndryshme.

## Teknologjitë
- Python 3.x
- Biblioteka standarde: hashlib, random

## Instalimi
1. Klono repository-n:
   git clone https://github.com/donartajvazi/DataSecurity-Grupi12.git
   cd DataSecurity-Grupi12

2. (Opsionale) Krijo një mjedis virtual:
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate       # Windows

3. Ekzekuto aplikacionin:
   python main.py

## Përdorimi
1. Zgjidh nëse dëshiron të enkriptosh (E) ose dekriptosh (D) kur të kërkohet.
2. Jep seed-in (string ose numër) për të gjeneruar çelësin.
3. Shkruaj mesazhin (plaintext) për enkriptim ose ciphertext për dekriptim.
4. Shiko tabelën me detajet e konvertimeve numerike dhe rezultatin.
## Shembull Përdorimi

```text
Do you want to encrypt or decrypt? (E/D): E
Enter a seed (string or number): 12345
Enter your message to encrypt: Hello World!

--- ENCRYPTION DETAILS ---
Index Plain  P#   Key   K#   Cipher C#
0     H      7    Q     16   X      23
1     E      4    W     22   A      0
2     L      11   E     4    P      15
3     L      11   R     17   C      2
4     O      14   T     19   H      7
5     W      22   Y     24   U      20
6     O      14   U     20   I      8
7     R      17   I     8    Z      25
8     L      11   O     14   Z      25
9     D      3    P     15   S      18
10    !      -    -     -    !      -

Encryption Results:
Generated Key: QWERTYUIOP
Ciphertext: XAPCHUIZZS!


## Struktura e Projektit
DataSecurity-Grupi12/
├── .idea/                - Cilësimet e IDE
├── main.py               - Logjika kryesore
└── README.md             - Dokumentacioni

## Detajet e Algoritmit
- Hash i seed-it: MD5 i seed-it, marrim 4 bajtët e parë për një integer 32-bit.
- Gjenerimi i çelësit: Inicializojmë random me këtë integer dhe krijojmë çelës rastësor me shkronja të mëdha.
- Enkriptim/Dekriptim: Operacione Vigenère mbi karakteret alfabetike, me ruajtje të karaktereve jo-alfabetike.

## Institucioni
Universiteti i Prishtinës "Hasan Prishtina"  
Fakulteti i Inxhinierisë Elektrike dhe Kompjuterike (FIEK)  
Departamenti i Inxhinierisë Kompjuterike dhe Softuerike  
Lënda: Siguria e të Dhënave  
Prishtinë, Kosovë

## Anëtarët e Ekipit
- Dion Haradinaj
- Diona Sadiku
- Donart Ajvazi
- Donart Spahiu

