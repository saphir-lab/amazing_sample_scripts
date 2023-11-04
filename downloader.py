# You may use download software to download photos or videos from the internet, but now you can create your own downloader using the Python IDM module.

# Python Downloader
# pip install internetdownloadmanager
import internetdownloadmanager as idm
def Downloader(url, output):
    pydownloader = idm.Downloader(worker=20,
                                part_size=1024*1024*10,
                                resumable=True,)
    
# Sample
# Downloader("Link url", "image.jpg")
# Downloader("Link url", "video.mp4")