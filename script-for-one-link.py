# First You need to import regex (Download it if you haven't yet)
import regex

link = input("Enter your drive link: ")

download_link = link.replace("file/d/", "uc?id=").replace("/view?usp=sharing", "&export=download")

print("Oop, here is your download link: ", download_link)
