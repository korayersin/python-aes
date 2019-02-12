#Python AES Crypto


##Requirements
- pycrypto `pip install pycrypto`

##Usage
`aes = AESCrypto("username", "value_of")`
`crypted_password = aes.encrypt("password")`
`print(crypted_password, aes.decrypt(crypted_password))`