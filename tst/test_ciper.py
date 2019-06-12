from aes_sha1prng import AESCiper


ciper = AESCiper('34xerl*XX||wwwR&%^')


def test_aes_encrypt():
    assert ciper.encrypt_to_hex('123456') == 'E2C59377E27E93EADE52A1722F9525B8'
    assert ciper.encrypt_to_hex('管理员') == '2E6EA8DD31C523851E36FB37C38251F7'


def test_aes_decrypt():
    assert ciper.decrypt_from_hex('E2C59377E27E93EADE52A1722F9525B8') == '123456'
    assert ciper.decrypt_from_hex('2E6EA8DD31C523851E36FB37C38251F7') == '管理员'
