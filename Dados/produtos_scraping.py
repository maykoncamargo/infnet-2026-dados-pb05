import requests
from bs4 import BeautifulSoup
import csv

def scraping_produtos():
    URL = "https://pedrovncs.github.io/lindosprecos/produtos.html"
    response = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    produtos = []

    for card in soup.find_all("div", class_="card-body"):
        # Nome via atributo data-nome
        h5 = card.find("h5")
        nome = h5.get("data-nome", "").strip() if h5 else ""

        # Preço: pega só os números (ex: "R$&nbsp;6,59" → "6.59")
        preco_tag = card.find("p", class_="card-price")
        preco_raw = preco_tag.get("data-preco", "") if preco_tag else ""
        preco = preco_raw.replace("R$\xa0", "").replace("R$", "").replace(",", ".").strip()

        # Quantidade: pega só o número do atributo data-qtd
        qtd_tag = card.find("p", attrs={"data-qtd": True})
        quantidade = qtd_tag.get("data-qtd", "").strip() if qtd_tag else ""

        produtos.append({
            "nome": nome,
            "quantidade": quantidade,
            "preco": preco
        })

    for p in produtos:
        print(p)

    with open("Dados/produtos.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["nome", "quantidade", "preco"])
        writer.writeheader()
        writer.writerows(produtos)

    print(f"\n✅ {len(produtos)} produtos salvos em Dados/produtos.csv")


scraping_produtos()