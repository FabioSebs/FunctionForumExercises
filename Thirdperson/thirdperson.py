def makeForms(verb:str):
    if verb.endswith('sh') or verb.endswith('ch'):
        return verb+"es"
    
    return {
        'y': verb.replace('y','ies'),
        'o': verb + "es",
        's': verb + "es",
        'x': verb + "es",
        'z': verb + "es"
    }.get(verb[-1], verb +"s")