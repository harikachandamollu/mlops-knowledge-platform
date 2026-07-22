from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup
import requests


def crawl(config):

    seed_url = config["seed_url"]

    allowed_paths = config["allowed_paths"]

    max_pages = config["max_pages"]


    visited = set()
    queue = [seed_url]

    urls = []


    while queue and len(urls) < max_pages:

        url = queue.pop(0)

        if url in visited:
            continue


        visited.add(url)


        try:

            response = requests.get(
                url,
                timeout=10
            )

            response.raise_for_status()


            urls.append(url)


            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )


            for link in soup.find_all("a", href=True):

                next_url = urljoin(
                    url,
                    link["href"]
                )


                parsed = urlparse(next_url)


                if any(
                    parsed.path.startswith(path)
                    for path in allowed_paths
                ):

                    if next_url not in visited:
                        queue.append(next_url)



        except Exception as e:

            print(
                f"Crawl failed {url}: {e}"
            )


    return urls