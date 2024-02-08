import random
import hashlib
from tkinter import E

# 1. Deberá hacer g=2 e investigar el número primo p
g = 2
p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919  # Número primo utilizado actualmente en Diffie-Hellman

# 2. Generar las llaves privadas de Alice (A) y Bob (B)
a = random.getrandbits(256)
print("\n""La llave privada de Alice es:", a)
b = random.getrandbits(256)
print("\n""La llave privada de Bob es:", b)
e = random.getrandbits(256)
print("\n""La llave privada de Eve es:", e)

# 3. Simular el intercambio de números entre Alice y Bob
A = pow(g, a, p)
print("\n""El número que Alice le envía a Bob es:", A)
B = pow(g, b, p)
print("\n""El número que Bob le envía a Alice es:", B)
E = pow(g, e, p)
print("\n""El número que Eve le envía a Alice es:", E)


# 4. Hacer el cómputo de la llave secreta “s” y el modulo de la llave secreta
s1 = pow(E, a, p)
print("\n""La llave secreta de Alice es:", s1)
s2 = pow(A, e, p)
print("\n""La llave secreta de eve/alice es:", s2)
s3 = pow(E, b, p)
print("\n""La llave secreta de Bob es:", s3)
s4 = pow(B, e, p)
print("\n""La llave secreta de eve/bob es:", s4)

if s1 == s2:
    s = hashlib.sha256(str(s1).encode()).hexdigest()
    print("\n""La llave secreta es:", s)
else:
    print("Error: Las llaves secretas no coinciden.")
if s3 == s4:
    s = hashlib.sha256(str(s3).encode()).hexdigest()
    print("\n""La llave secreta es:", s)
else:
    print("Error: Las llaves secretas no coinciden.")

if s1 == s3:
    print("\n""Las llaves secretas de Alice y Bob coinciden.")
else:
    print("\n""Error: Las llaves secretas no coinciden.""\n")
