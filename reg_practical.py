import re, urllib
try:
    import urllib.request
except:
    pass
sites = 'google yahoo cnn msn'.split()
comp = re.compile(r'<title>+.*</title>+',re.I|re.M )
for s in sites:
    print("Searching: "+ s)
    try:
        u = urllib.urlopen('http://'+s+'.com')
    except:
        u = urllib.request.urlopen('http://'+ s + '.com')
    text = u.read()
    title = re.findall(comp, str(text))
    print(title[0])



"""
print(re.split(r'\s*','here are some words'))
print(re.split(r'\d', 'pimple saudagar 234 main road 232 st.nfnjbjab'))
print(re.findall(r'\d', 'pimple saudagar 234 main road 232 st.nfnjbjab'))
print(re.findall(r'\d{1,5}\s\w+\.', 'pimple saudagar 234 main road 232 st.nfnjbjab'))
"""
