from backend.get_cuota import obtener_cuota


def validate_account(username: str, password: str) ->int:
    response= obtener_cuota(username , password)
    if  response.status_code ==200:
        return 1
    elif response.status_code ==500:
        return 2
    
    else :
        return 3
    

def validate_red():
    return True