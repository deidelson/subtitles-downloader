import bash


def getUrl(url):
    return bash.execute("curl " + url)

def get(url, headers, params):
    return getUrl(url)

result, error = get("www.google.com", "", "")

print(result)
