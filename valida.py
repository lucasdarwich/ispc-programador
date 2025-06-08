import re

#valida que el cuit ingresado tenga el formato correcto y sea valido

# \d → dígito del 0 al 9
#{2} → exactamente 2 repeticiones
#- → el carácter guion
#{8} → exactamente 8 dígitos
#{1} o simplemente \d → un solo dígito al fina

def valida_cuit(cuit):
    # Validar formato: 99-99999999-9
    if not re.fullmatch(r"\d{2}-\d{8}-\d", cuit):
        return False

    # Sacar los guiones y lo deja como numero 

    cuitNum = cuit.replace("-", "")
    if len(cuitNum) != 11 or not cuitNum.isdigit():
        return False
    else:
        return cuitNum

 
# v^[\w\.-]+ → empieza con letras, números, guiones o puntos
# @ → debe tener arroba
# [\w\.-]+ → dominio (por ejemplo gmail, hotmail)
# \.\w{2,} → extensión del dominio: .com, .ar, .org, etc.

def valida_mail(email):
    # Verifica que no esté vacío y no supere 50 caracteres
    if not email or len(email) > 50:
        return False

    # Patrón básico de email válido
    patron = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    
    # Validamos contra el patrón
    if re.fullmatch(patron, email):
        return True
    else:
        return False
