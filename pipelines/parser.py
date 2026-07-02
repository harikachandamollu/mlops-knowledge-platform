from bs4 import BeautifulSoup

def extract_text(html:str) -> str:
    soup = BeautifulSoup(html, "lxml")

    # remove noise
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    article = soup.find("article")

    if article:
        return article.get_text("\n", strip=True)
    
    return soup.get_text("\n", strip=True)