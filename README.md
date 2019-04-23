# Simple SHA512 Passwd Verifier

## Instructions

1. Write your password to `pass`
2. Write your hashed sha512 sha to `hash`
3. Run the command below. If it returns true, then the hash matches the password, else false

```bash
docker run -it bernadinm/sha512_verify $(cat pass) $(cat hash)
```
