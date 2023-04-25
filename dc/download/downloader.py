import os
import requests
import threading
from urllib.parse import urlparse

def download_file(url, dest_folder):
    response = requests.get(url, stream=True)
    file_size = int(response.headers.get("Content-Length", 0))
    filename = os.path.join(dest_folder, urlparse(url).path.split("/")[-1])

    with open(filename, "wb") as file:
        for data in response.iter_content(chunk_size=1024):
            file.write(data)

    print(f"{filename} downloaded.")

def threaded_download(urls, dest_folder, num_threads):
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    threads = []
    for i in range(num_threads):
        t = threading.Thread(target=download_file, args=(urls[i], dest_folder))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

if __name__ == "__main__":
    urls = [
        "https://example.com/file1.zip",
        "https://example.com/file2.zip",
        "https://example.com/file3.zip",
    ]
    dest_folder = "downloads"
    num_threads = len(urls)

    threaded_download(urls, dest_folder, num_threads)