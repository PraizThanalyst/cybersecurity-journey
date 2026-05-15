# Foundations — Encoding & Hashing

## What this covers

This script covers the basics of encoding.. we used base64 to encode the text SilentPayload and decoded it back to the original... it shows that encoding is mainly for representation.

It also covers hashing — converting an input to a fixed size string that can't be reversed, unlike encryption (reversible with a key) or encoding (reversible by anyone). The hash algorithm decides the length of the hash. In the script we used md5 (less secure now) and sha256. Hashes also have the avalanche effect — changing one character (like SilentPayload vs silentPayload) produces a completely different hash.

We also looked at salting — adding a random string before hashing. Without a salt, the same input always produces the same hash, meaning attackers can use pre-computed rainbow tables to look up common passwords instantly. Salt makes each hash unique so rainbow tables don't work. Run the script twice and notice the salted output gives a different result each time.

## Files

- `encoding-hashing.py` — demos for base64, hex, MD5, SHA256, and salted hashing
