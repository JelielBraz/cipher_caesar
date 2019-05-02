import hashlib
import json
import string
import requests


def requisicao():
    response = requests.get('https://api.codenation.dev/v1/challenge/dev-ps/generate-data?token'
                            '=e95082eeb8f8ee218cea54184e5f0a2a1c2af66b')
    jason = response.json()
    return jason


def cifrador(texto, nr):
    letras = string.ascii_lowercase

    nova_palavra = ''
    texto = texto.lower()

    for i in texto:
        if i not in letras:
            nova_palavra += i
        else:
            pos = letras.find(i)
            pos_letra_determinada = pos - nr + 1
            while pos_letra_determinada > 26:
                pos_letra_determinada -= 26
            nova_palavra += letras[pos_letra_determinada - 1]
    return nova_palavra


def write_in_file(jazao):
    file = open("answer.json", 'w')
    json.dump(jazao, file)
    file.close()


def tester():
    print(cifrador("tovsov", 10))
    print(cifrador("AAA", 1))
    print(cifrador("kfmjfm csba", 1))
    print(cifrador("kfmjfm.csba", 1))
    print(cifrador("kfmjfm 123", 1))


def main():
    jazao = requisicao()
    nr_casas = jazao.get("numero_casas")
    cifrado = jazao.get("cifrado")
    palavra = cifrador(cifrado, nr_casas)
    jazao['decifrado'] = palavra
    criptografia = hashlib.sha1(str(palavra).encode('utf-8'))
    jazao['resumo_criptografico'] = criptografia.hexdigest()
    write_in_file(jazao)
    requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=e95082 '
                  'eeb8f8ee218cea54184e5f0a2a1c2af66b', )



if __name__ == '__main__':
    main()