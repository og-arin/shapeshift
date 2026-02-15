#!/usr/bin/env python3
import argparse
import base64
import binascii
import codecs
import urllib.parse
import sys

# Dependency Check
try:
    from rich.console import Console
    from rich.table import Table
except ImportError:
    print("[!] Error: 'rich' library missing. Run: pip install rich")
    sys.exit(1)

console = Console()

# --- DICTIONARIES ---
MORSE_DICT = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'}
BACON_DICT = {'A': 'aaaaa', 'B': 'aaaab', 'C': 'aaaba', 'D': 'aaabb', 'E': 'aabaa', 'F': 'aabab', 'G': 'aabba', 'H': 'aabbb', 'I': 'abaaa', 'J': 'abaab', 'K': 'ababa', 'L': 'ababb', 'M': 'abbaa', 'N': 'abbab', 'O': 'abbba', 'P': 'abbbb', 'Q': 'baaaa', 'R': 'baaab', 'S': 'baaba', 'T': 'baabb', 'U': 'babaa', 'V': 'babab', 'W': 'babba', 'X': 'babbb', 'Y': 'bbaaa', 'Z': 'bbaab'}

# --- LOGIC FUNCTIONS ---
def atbash_transform(data):
    res = ""
    for char in data:
        if char.isalpha():
            offset = ord('A') if char.isupper() else ord('a')
            res += chr(offset + (25 - (ord(char) - offset)))
        else: res += char
    return res

def base58_encode(data):
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    try:
        num = int.from_bytes(data.encode(), 'big')
        res = ""
        while num > 0:
            num, rem = divmod(num, 58)
            res = alphabet[rem] + res
        return res if res else "1"
    except: return "N/A"

def base58_decode(data):
    alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    try:
        num = 0
        for char in data:
            num = num * 58 + alphabet.index(char)
        return num.to_bytes((num.bit_length() + 7) // 8, 'big').decode('utf-8', errors='replace')
    except: return "[red]N/A[/red]"

def rot_brute_force(data):
    results = []
    for i in range(1, 26):
        shifted = ""
        for char in data:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                limit = ord('Z') if char.isupper() else ord('z')
                res = ord(char) + i
                if res > limit: res -= 26
                shifted += chr(res)
            else: shifted += char
        results.append((f"ROT{i}", shifted))
    return results

BANNER = """
[bold red]SHAPESHIFT PRO[/bold red] [white]| Ultra Edition[/white]
[cyan]Developed by og__arin[/cyan]
"""

def perform_encodings(data):
    table = Table(title="[bold cyan]ENCODING RESULTS[/bold cyan]", border_style="blue")
    table.add_column("METHOD", style="yellow")
    table.add_column("OUTPUT", style="white")
    
    table.add_row("Base64", base64.b64encode(data.encode()).decode())
    table.add_row("Base32", base64.b32encode(data.encode()).decode())
    table.add_row("Base85", base64.b85encode(data.encode()).decode())
    table.add_row("Base58", base58_encode(data))
    table.add_row("Hexadecimal", data.encode().hex())
    table.add_row("Binary", ' '.join(format(ord(x), '08b') for x in data))
    table.add_row("Decimal", ' '.join(str(ord(x)) for x in data))
    table.add_row("Atbash Cipher", atbash_transform(data))
    table.add_row("Morse Code", ' '.join(MORSE_DICT.get(c.upper(), '?') for c in data))
    table.add_row("Baconian", ' '.join(BACON_DICT.get(c.upper(), '') for c in data if c.isalpha()))
    
    console.print(table)

def perform_decodings(data):
    table = Table(title="[bold magenta]DECODING ATTEMPTS[/bold magenta]", border_style="red")
    table.add_column("METHOD", style="yellow")
    table.add_column("RESULT", style="green")

    try: table.add_row("Base64", base64.b64decode(data).decode('utf-8', errors='replace'))
    except: pass
    
    table.add_row("Base58", base58_decode(data))
    
    try:
        dec = "".join([chr(int(x)) for x in data.split()])
        table.add_row("Decimal->Text", dec)
    except: pass

    table.add_row("Atbash Decode", atbash_transform(data))
    for name, val in rot_brute_force(data):
        table.add_row(name, val)
    
    table.add_row("URL Decode", urllib.parse.unquote(data))
    console.print(table)

if __name__ == "__main__":
    console.print(BANNER)
    parser = argparse.ArgumentParser()
    parser.add_argument("data", help="Input string")
    parser.add_argument("-e", "--encode", action="store_true")
    parser.add_argument("-d", "--decode", action="store_true")
    args = parser.parse_args()

    if args.encode: perform_encodings(args.data)
    if args.decode: perform_decodings(args.data)
    if not args.encode and not args.decode:
        perform_encodings(args.data)
        perform_decodings(args.data)