import requests
import xml.etree.ElementTree as ET

# ── CONFIG ────────────────────────────────────────────────────────────────────
SITEMAP_URLS = [
    "https://www.xzone.cz/1_sitemapproducts.xml",
    "https://www.smarty.cz/Feed/Sitemap/Products",
    # sem přidej další XML sitemapy
]

SEARCH_SUBSTRINGS = [
    "tomb-raider-legacy-of-atlantis-deluxe-edition",
    # sem přidej další substrings
]
# ─────────────────────────────────────────────────────────────────────────────

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "cs-CZ,cs;q=0.9,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.google.com/",
    "Connection": "keep-alive",
}


def check_sitemap(sitemap_url, substrings):
    print(f"\nProhledávám: {sitemap_url}")
    try:
        session = requests.Session()
        domain = "/".join(sitemap_url.split("/")[:3])
        session.get(domain, headers=HEADERS, timeout=15)
        response = session.get(sitemap_url, headers=HEADERS, timeout=15)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"  CHYBA při stahování: {e}")
        return

    try:
        root = ET.fromstring(response.content)
    except ET.ParseError as e:
        print(f"  CHYBA při parsování XML: {e}")
        return

    all_locs = [
        el.text
        for el in root.iter()
        if (el.tag == "loc" or el.tag.endswith("}loc")) and el.text
    ]

    for substring in substrings:
        found_urls = [loc for loc in all_locs if substring.lower() in loc.lower()]
        if found_urls:
            print(f"  NALEZENO \"{substring}\" ({len(found_urls)} URL):")
            for url in found_urls:
                print(f"    {url}")
        else:
            print(f"  Nenalezeno: \"{substring}\"")


if __name__ == "__main__":
    print(f"Hledám {len(SEARCH_SUBSTRINGS)} substring(ů)...")
    for sitemap_url in SITEMAP_URLS:
        check_sitemap(sitemap_url, SEARCH_SUBSTRINGS)
    print("\nHotovo.")
