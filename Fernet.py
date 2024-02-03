from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

token = f.encrypt(b"<a>")
print(token)

des = f.decrypt(token)
print(des)

f= Fernet(b'FlSjjZKpfmrUvbeNLqkdEs1vB5umbbyyO1b64tw5aws=')

tokend = f.decrypt(b'gAAAAABluwmnLs_084sanFKl6WWltcHgRdm8opf-AFnmSs9CGpNDOaCe84m0U6oxxk1Z3OhqvBRo3zN-e3H6Re9EHTaPYzHwTX_esVkMHpahECEWoqHlhUIAYbofu928zwFEvaqA_1LRV4v1-DuO7hJJC5Bl_kPboEMprcL1ujoQjbeKSnDrgR11qk3M4cWvF48oIdJd2rL-YjDV-V0-9fKv_FEeqeZ0fIpFLXB83Xe9gT_JtXrSqH-djC4r9vlbDkaEp6qo6CZUV44yfNoRUPIqv65uxnqBMQ==')
print(tokend)
