import pyshorteners as ps

url = "https://docs.djangoproject.com/en/3.1/intro/tutorial02/"

u = ps.Shortener().tinyurl.short(url)
print(u)
