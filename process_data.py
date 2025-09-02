import feedparser
import xml.etree.ElementTree as ET
from xml.dom import minidom

# Chaves de pesquisa
queries = ["Inteligência Artificial Piauí", "SIA Piauí"]

# URL base para o RSS do Google News (em português do Brasil)
base_url = "https://news.google.com/rss/search?q={}&hl=pt-BR&gl=BR&ceid=BR:pt"

# Lista para armazenar as notícias únicas (usando set para evitar duplicatas por link)
news_items = []
seen_links = set()

# Coletar notícias de cada query
for query in queries:
    rss_url = base_url.format(query.replace(" ", "+"))
    feed = feedparser.parse(rss_url)

    for entry in feed.entries:
        link = entry.link
        if link in seen_links:
            continue
        seen_links.add(link)

        title = entry.title
        # Usar a descrição nativa do feed RSS, se disponível
        description = entry.get('summary', 'Resumo não disponível') if 'summary' in entry else 'Resumo não disponível'

        news_items.append({
            "title": title,
            "link": link,
            "description": description
        })

        if len(news_items) >= 15:
            break

    if len(news_items) >= 15:
        break

# Limitar a 10-15 itens
news_items = news_items[:15]
if len(news_items) < 10:
    print("Aviso: Menos de 10 notícias encontradas.")

# Gerar o arquivo XML
root = ET.Element("news")

for item in news_items:
    news_elem = ET.SubElement(root, "item")
    ET.SubElement(news_elem, "title").text = item["title"]
    ET.SubElement(news_elem, "link").text = item["link"]
    ET.SubElement(news_elem, "description").text = item["description"]

# Pretty print o XML
xml_str = minidom.parseString(ET.tostring(root)).toprettyxml(indent="  ")

# Salvar em arquivo
with open("noticias.xml", "w", encoding="utf-8") as f:
    f.write(xml_str)

print("Arquivo 'noticias.xml' gerado com sucesso!")