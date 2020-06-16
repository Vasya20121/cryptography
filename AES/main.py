import AES128
#task 1.1
input_bytes = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
key = 'Dopusk' # метод KeyExpansion() перетворює кожен символ в int(0...255) за допомогою ord() і відповідно записує результати
#якщо не довжини 16, то заповнюю 0x01 в інші комірки
cipher = AES128.encrypt(input_bytes, key)
message = AES128.decrypt(cipher, key)
print("Plaintext: [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]")
print("encrypt")
print(cipher) #[130, 0, 3, 29, 218, 141, 240, 80, 207, 255, 98, 57, 23, 39, 112, 16]
print("decrypt")
print(message) #[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

#task 1.2
"""В-дь: повністю міняється"""
input_bytes = [1<<1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
key = 'Dopusk'
cipher = AES128.encrypt(input_bytes, key)
message = AES128.decrypt(cipher, key)
print("Plaintext: [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]")
print("encrypt")
print(cipher) #[130, 0, 3, 29, 218, 141, 240, 80, 207, 255, 98, 57, 23, 39, 112, 16]
print("decrypt")
print(message) #[2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
