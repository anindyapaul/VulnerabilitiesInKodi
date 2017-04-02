
def unicode_safe_file_read(file_path):
    """Unicode Safe File Read, Returns data"""
    with io.open(file_path, mode='r', encoding="utf8", errors="ignore") as file_ptr:
        return file_ptr.read()
        

data = unicode_safe_file_read("./kodi-webinterface.js")
beautified_data = jsbeautifier.beautify(data)
lines = beautified_data.splitlines()
f = open("./kodi-webinterface_beautified.js", 'w')
for line in enumerate(lines):
    f.write(str(line[1]))
    f.write('\n')
f.close()
