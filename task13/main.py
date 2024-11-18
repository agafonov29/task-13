class CaesarsCipher:
    def __init__(self):
        self.alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?."
        self.alphabet_len = len(self.alphabet)

    def encrypt(self, text: str, key: int) -> str:
        return ''.join(self.alphabet[(self.alphabet.index(char) + key) % self.alphabet_len]
                       if char in self.alphabet else char for char in text)

    def decrypt(self, text: str, key: int) -> str:
        return ''.join(self.alphabet[(self.alphabet.index(char) - key) % self.alphabet_len]
                       if char in self.alphabet else char for char in text)


if __name__ == "__main__":
    cipher = CaesarsCipher()
    message = "o3zR v..D0?yRA0R8FR8v47w0ER4.R1WdC!sLF5D"

    for key in range(len(cipher.alphabet)):
        decrypted_message = cipher.decrypt(message, key)
        print(f"{key}: {decrypted_message}")

        if "password" in decrypted_message.lower():
            print(f"Подобранный ключ: {key}. Расшифрованное сообщение: {decrypted_message}")

            file_path = input("Введите путь для сохранения результата: ")
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(f"Подобранный ключ: {key}\n")
                file.write(f"Расшифрованное сообщение: {decrypted_message}\n")
            break
