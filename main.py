from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

# Генерация пары ключей RSA (приватный и публичный ключи)
private_key = rsa.generate_private_key(
    public_exponent=65537,  # Рекомендуемый стандартный экспонент
    key_size=2048,  # Рекомендуемый размер ключа
)

# Получение публичного ключа из приватного
public_key = private_key.public_key()

# Создание сообщения, которое нужно подписать
message = b"Hello, world!"

# Создание подписи
signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

# Проверка подписи
try:
    public_key.verify(
        signature,
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    print("Подпись верна. Сообщение не было изменено.")
except cryptography.exceptions.InvalidSignature:
    print("Подпись недействительна. Сообщение было изменено или ключи не совпадают.")
