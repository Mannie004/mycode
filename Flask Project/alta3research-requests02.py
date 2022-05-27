import requests
# import yaml

url = 'http://127.0.0.1:5000/product'
def main():
    resp = requests.get(url)

    data = resp.json()
    
    # convert to YAML
    # text =  yaml.dump(data)
    # print(text)
    for x in data:
        text = f"{x['name']}\nshows that {x['description']}\nand has a price of ${x['price']}\n{x['qty']} units available\n"
        print(text)



if __name__ == '__main__':
    main()