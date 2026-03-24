from Crypto.Cipher import AES
import os


def AES_PRF(açar, məlumat):
    şifrə = AES.new(açar, AES.MODE_ECB)
    return şifrə.encrypt(məlumat)


def şifrələ(açar, mətn):
    mətn = mətn.encode()           
    təsadüfi = os.urandom(16)               
    şifrələnmiş = b""
    
   
    for j in range(0, len(mətn), 16):
        blok = mətn[j:j+16]
      
        prf_giriş = təsadüfi + j.to_bytes(16, "big")
        açar_axını = AES_PRF(açar, prf_giriş)[:len(blok)]
        şifrə_bloku = bytes([b ^ k for b, k in zip(blok, açar_axını)])
        şifrələnmiş += şifrə_bloku
    
    return təsadüfi + şifrələnmiş            

def deşifrə(açar, şifrələnmiş):
    təsadüfi = şifrələnmiş[:16]
    tək_şifrə = şifrələnmiş[16:]
    deşifrə_olunmuş = b""
    
    for j in range(0, len(tək_şifrə), 16):
        blok = tək_şifrə[j:j+16]
        prf_giriş = təsadüfi + j.to_bytes(16, "big")
        açar_axını = AES_PRF(açar, prf_giriş)[:len(blok)]
        deşifrə_bloku = bytes([c ^ k for c, k in zip(blok, açar_axını)])
        deşifrə_olunmuş += deşifrə_bloku
    
    return deşifrə_olunmuş.decode()

açar = os.urandom(16)  
mətn = "Hello world"

şifrələnmiş = şifrələ(açar, mətn)
print("Şifrələnmiş (hex):", şifrələnmiş.hex())

deşifrə_olunmuş = deşifrə(açar, şifrələnmiş)
print("Deşifrə olunmuş:", deşifrə_olunmuş)