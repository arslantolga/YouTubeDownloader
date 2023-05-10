import pytube

download_url = input("Enter your download url : ")
saving_path = ""

pytube.YouTube(download_url).streams.first().download(saving_path)
