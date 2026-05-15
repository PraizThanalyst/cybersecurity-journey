# Week 1 — ECB Mode Attacks

## What I did this week

I encrypted a tux-image with python using AES-ECB (Electronic Codebook) to understand and visualize why ECB is broken.

## What ECB is and why it's broken

ECB (Electronic Codebook) is a mode that encrypts blocks independently. It's broken because each identical plaintext block produces identical ciphertext blocks.

## What I observed in the lab

I used python to encrypt a tux.bmp image (python script can be found in the file section) with AES-ECB and i opened the encrypted file. The colors changed but the tux shape could still be seen clearly.

The shape survived because ECB encrypts each block independently and from the tux.bmp image the pixel blocks were identical so it produced identical ciphertext. The colors changed but the shape is still visible asl.

## Takeaways

Before this I never knew modes like this existed but during my research I decided to study on it. I encrypted a BMP image with ECB and could see Tux's outline in the encrypted file — proof that ECB is broken because identical plaintext blocks produce identical ciphertext. No one should ever use ECB as a mode in encryption. It's technically been deprecated for years but still shows up in legacy systems and tutorials, which is why it's worth recognizing in the wild.

## Lab setup

- **Tool:** pycryptodome (Python)
- **Image:** Tux Linux mascot, converted from SVG to BMP with ImageMagick
- **Mode:** AES-128 in ECB mode
- **Key:** `YELLOW SUBMARINE` (16 bytes, CryptoPals tradition)
- **OS:** Kali Linux

## Files

- `ecb_penguin.py` — encryption script
- `tux.bmp` — original image
- `tux_ecb.bmp` — ECB-encrypted output (Tux outline still visible)
- `tux.svg` — source SVG before BMP conversion
