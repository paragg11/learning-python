24 JUNE 2022

## FIRST HALF

- 🚧 CSCI Lecture 8 completed. 
- 🚧 Demo given on Passbook APIs

## VIDEOS

- 🚫 No videos

## ASSIGNMENT

- 🚧 [Passbook](https://github.com/sp18-interns/django-passbook)

## DOUBTS

- No doubts for now 

## LINKS

- [Lecture 8 — Tuples, Modules, Images](https://www.cs.rpi.edu/~sibel/csci1100/fall2017/lecture_notes/lec08_modules_images.html)

## SECOND HALF

- ✅ [Hackerrank solving one problem.]
- 🚧 Understanding concept of authentication and authorization.
```
JWT(JSON Web Token)

Structure of JWT
JSON web token consists of three parts:-
1) Header
2) Payload
3) Signature
and each part is separated by the dot.

header.payload.signature

Header

The header consists of two parts:

1. Which signing algorithm to be used, and

2. The type of token(JWT).

Basically, signing can be done on the basis of a secret key or 
a public and private key.

Payload

{
"sub": "123456789
"name": "Jack",
"admin": true
}

The Payload part consists of the claims. Claims are the statements 
about the user and some additional data

Signature

For the Signature part, what we want is the Header and payload in the encoded form, 
secret and we get the Signature in the following manner.

HMACSHA256(base64UrlEncode(header) + “.” + base64UrlEncode(payload), secret)

By combining all the three “header, payload, and the signature”, we get a JWT token

```

## VIDEOS

- 🚫 No videos

## ASSIGNMENT

- [Passbook](https://github.com/sp18-interns/django-passbook)

## DOUBTS

- Not a exact understanding of tokens and JWT

## LINKS

- [What is JWT (JSON Web Token)?](https://medium.com/@knoldus/what-is-jwt-json-web-token-44386e309fed)
- [JSON Web Token](https://en.wikipedia.org/wiki/JSON_Web_Token)
- [JWT (JSON Web Tokens) Are Better Than Session Cookies](https://dzone.com/articles/jwtjson-web-tokens-are-better-than-session-cookies)
- [What is JSON Web Token?](https://jwt.io/introduction/)
- [Understanding JSON Web Token Authentication](https://blog.bitsrc.io/understanding-json-web-token-authentication-a1febf0e15)

