import httpcore


def format_request_headers(request: httpcore.Request, http2: bool = False) -> str:
    version = "HTTP/2" if http2 else "HTTP/1.1"
    headers = [
        (name.lower() if http2 else name, value) for name, value in request.headers
    ]
    method = request.method.decode("ascii")
    target = request.url.target.decode("ascii")
    lines = [f"{method} {target} {version}"] + [
        f"{name.decode('ascii')}: {value.decode('ascii')}" for name, value in headers
    ]
    return "\n".join(lines)

     #0   #1   #2
l = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
     'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = 923142
def translate(a: list, n: int) -> str:
    s = ""
    while n > 0:
        s = a[n % len(a)] + s
        n //= len(a)
    return s

print(translate(l, num))
