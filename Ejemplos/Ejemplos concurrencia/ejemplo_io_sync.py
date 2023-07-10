import requests
import time


def download_site(url, session):
    with session.get(url) as response:
        # print(response.content)
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(sites):
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)


if __name__ == "__main__":
    sites = [
        "https://acaducr.ucr.ac.cr/",
        "https://www.python.org/",
    ] * 8
    start_time = time.time()
    # download_all_sites(["https://acaducr.ucr.ac.cr/"])
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")