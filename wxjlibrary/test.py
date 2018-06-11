def application(env, start_response):
    start_response('200 OK', [('Content-Type','text/html')])
    return [b"Hello World"]   #Python 3.x 需要 返回字节字符串
