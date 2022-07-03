import regex

link = input("Enter your drive link: ")

download_link = link.replace("file/d/", "uc?id=").replace("/view?usp=sharing", "&export=download")

print(download_link)
