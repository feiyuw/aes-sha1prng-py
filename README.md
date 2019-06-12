AES encrypt/decrypt library with java SHA1PRNG algorithm for python3

## Example:

```python

from aes_sha1prng import AESCiper


ciper = AESCiper('34xerl*XX||wwwR&%^')

# encrypt
print(ciper.encrypt_to_hex('123456'))  # E2C59377E27E93EADE52A1722F9525B8
print(ciper.encrypt_to_hex('管理员'))  # 2E6EA8DD31C523851E36FB37C38251F7

# decrypt
print(ciper.decrypt_from_hex('E2C59377E27E93EADE52A1722F9525B8'))  # '123456'
print(ciper.decrypt_from_hex('2E6EA8DD31C523851E36FB37C38251F7'))  # '管理员'
```
