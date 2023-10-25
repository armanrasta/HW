import requests

records = 0 

def url_getter(url):
    response = requests.get(url)
    return response.json()

def processer(data):
    pass

# def x(data):
#     nonlocal records
#     records += len(data)

def main():
    url = "https://my-json-server.typicode.com/armanrasta/json"
    p = url_getter(url)
    print (p)
    
if __name__ == "__main__":
    main()
