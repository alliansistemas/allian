from datetime import datetime

def ano_atual(request):
    return {'ano_atual': datetime.now().year}