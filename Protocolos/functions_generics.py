from datetime import datetime


def date_formating(date):
    time = datetime.fromtimestamp(date)
    result = time.strftime("%d/%m/%Y, %H:%M:%S")
    return result


def decode_utf(payload):
    return payload.decode('utf-8')
