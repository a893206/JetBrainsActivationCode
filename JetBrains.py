import subprocess
import zipfile
from io import BytesIO

import requests

if __name__ == '__main__':
    # 通用
    # url = 'http://idea.medeming.com/jets/images/jihuoma.zip'
    # IDEA
    url = 'http://idea.medeming.com/a/jihuoma1.zip'
    # PyCharm
    # url = 'http://idea.medeming.com/a/jihuoma2.zip'
    # WebStrom
    # url = 'http://idea.medeming.com/a/jihuoma3.zip'

    request = requests.get(url)
    zipFile = zipfile.ZipFile(BytesIO(request.content))
    for fileName in zipFile.namelist():
        if '2018.2' in fileName:
            process = subprocess.Popen('pbcopy', stdin=subprocess.PIPE)
            process.communicate(zipFile.read(fileName))
            break
    zipFile.close()
