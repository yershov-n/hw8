
def list_rec2html_br(param):
    return '<br/>'.join(str(elem) for elem in param)


def milliseconds_conv(value):
    from datetime import timedelta
    return f'{str(timedelta(milliseconds=value))}'[:-3]
