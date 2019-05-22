# Simple SHA512 Passwd Verifier

## Instructions

*Note*: You need to use sinlge quotes to avoid bash evaluation of the text

```bash
docker run -it bernadinm/sha512_verify 'nothing' '$6$rounds=656000$pMnbaHNOFFqKKc0Q$.VncwqI9aIqM3ecrPbL2rMzJW0.GzgoD54A/ZWIwuwYS20Q3lvSinPvl76.7ILn7nQoazS9TlsiV9TV63MITK.'
```

#### Alternative Method

If you dont want your password to show on your console for any reason, you can run it in files below:

1. Write your password to `pass`
```bash
vi pass
```

2. Write your hashed sha512 sha to `hash`
```bash
vi hash
```

3. Run the command below. If it returns true, then the hash matches the password, else false

```bash
docker run -it bernadinm/sha512_verify "$(cat pass)" "$(cat hash)"
```

## Generate Password hash

If you wanted to generate your password hash, you follow the instructions here: https://github.com/bernadinm/sha512-crypt
