from passlib.hash import sha512_crypt
import sys

print (sha512_crypt.verify(sys.argv[1], sys.argv[2]))
