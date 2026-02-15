▄▄ █▀▄ █▀▀ █▀▀ █▀█ █▀▄ █▀▀
█▄█ █▄▀ ██▄ █▄▄ █▄█ █▄▀ ██▄
ShapeShift Pro: The Universal Data Transformer
Developed by: og__arin

ShapeShift Pro is a powerful, cross-platform CLI tool designed for security researchers, CTF players, and developers. Inspired by platforms like dCode.fr and CyberChef, it provides a streamlined interface to encode, decode, and brute-force various data formats directly from your terminal.

🚀 Key Features
Comprehensive Base Variants: Support for Base64, Base32, Base85, and Base58 (Bitcoin encoding).

Classical Ciphers: Includes Atbash Cipher, Morse Code, and Baconian Cipher.

ROT Brute-Force: Automatically tests all possible Caesar Cipher shifts from ROT1 to ROT25.

Numerical Transformations: Convert data between Binary, Octal, Decimal, and Hexadecimal.

Web Utilities: Built-in URL Encoding and Decoding.

Cross-Platform Compatibility: Native support for both Windows and Linux (Black-OS).

🛠️ Installation
ShapeShift Pro comes with an automated installer that handles dependencies and system path configuration.

Clone the Repository:

Bash
git clone https://github.com/yourusername/ShapeShift.git
cd ShapeShift
Run the Installer:

On Windows (PowerShell/CMD):

PowerShell
python install.py
On Linux (Black-OS):

Bash
sudo python3 install.py
💻 Usage Examples
Once installed, the shapeshift command becomes available globally in your terminal.

Full Transformation (Default):

Bash
shapeshift "YourSecretData"
Encode Mode Only:

Bash
shapeshift "hello" --encode
Decode/Brute-Force Mode:

Bash
shapeshift "UzVpZGVyR29k" --decode
📂 Project Structure
Shapeshift.py: The core engine containing all transformation logic.

install.py: The automated setup script for OS detection and global command registration.

README.md: Documentation and usage guide.

🛠️ Dependencies
This tool utilizes the rich library for its advanced CLI interface. While the installer handles this automatically, you can install it manually via:

Bash
pip install rich
