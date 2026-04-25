import hashlib

def codificar(txt):
    hash_obj = hashlib.sha256(txt.encode('utf-8'))
    return hash_obj.hexdigest()

def validar_senha(senha):
    caracteres_especiais = set('!@#$%¨&*()')

    conta_erro = 0
    
    if not 3 < len(senha) <= 10:
        conta_erro += 1
        
    if not any(character in caracteres_especiais for character in senha):
        conta_erro += 1
    
    if not any(character.isdigit() for character in senha):
        conta_erro += 1

    if not any(character.isalpha() for character in senha):
        conta_erro += 1

    if conta_erro == 0:
        return True
    else:
        return False