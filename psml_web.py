#!/usr/bin/env python3
from bottle import *
import bottle
from PSML import compile
from os import remove,path
from beaker.middleware import *
from beaker import *

session_opts = {
    'session.type':'file',
    'session.cookei_expires':float("inf"),
    'session.data_dir':os.path.join(os.path.dirname(__file__),"data"),
    'sessioni.auto':True
}

    
@route('/script/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=os.path.dirname(__file__))

@route('/bin/<filepath:path>')
def bin(filepath):
    return static_file(filepath, root=os.path.join(os.path.dirname(__file__),"obj"))


@route("/")
def main():
    dat=request.environ.get("beaker.session")
    if dat.get("code",None)==None:
        try:
            dat["code"]=open(os.path.dirname(__file__)+"/test.psml","r").read()
        except:
            dat["code"]="/> Write your code here\n"
        dat.save()
        code=dat.get("code",None)
    else:
        code=dat.get("code",None)
    return template(f"""<!doctype html>
<html>
<head>
<meta charset="utf8">
<title>PSML</title>
<script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="/script/auto.js"></script>
<link href="bin/__init__.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<form action="/change" method="post">
<center>
<div autoHeight style="display:block;height:400px">
<div style="height:396px;width:49%;border:1px solid green;font-family:Monospace;float:left"><code><span><code>PSML CODE</code></span><br><hr color="green"><textarea id="code" name="codes" style="height:90%;width:98%;border:1px solid green;resize:none;word-wrap:break-word;outline:none;">{code}</textarea></div>
<div name="html" autoHeight style="height:399px;width:49%;border:1px solid red;display:inline;font-family:Monospace;float:left"><span><code>View</code></span><br><hr color="red"></div>
</div>
<button type="submit" style="border:0;background-color:blue;outline: none;color:white">Compile</button>
</center>
</form>
</body>
</html>
""")

@route("/change",method=["GET","POST"])
def change():
    form=form=FormsDict(bottle.request.POST).decode("utf8")
    try:
        codes=''.join(form.get("codes").split("\r"))
        codes="&lt;".join(codes.split("<"))
        codes="&gt;".join(codes.split(">"))
        dat=request.environ.get("beaker.session")
        dat["code"]=codes
        dat.save()
        codes="<".join(codes.split("&lt;"))
        codes=">".join(codes.split("&gt;"))
        html=compile(codes,mode=2)
        if type(html)==dict:
            html=html["index"]
        htmlELE="&lt;".join(html.split("<"))
        htmlELE="&gt;".join(htmlELE.split(">"))
        htmlELE="&nbsp".join(htmlELE.split(" "))
        return template(f"""<!doctype html>
<html>
<head>
<meta charset="utf8">
<title>PSML</title>
<script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="/script/auto.js"></script>
<link href="bin/__init__.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<form action="/change" method="post">
<div autoHeight style="display:block;height:400px">
<div style="height:396px;width:49%;border:1px solid green;float:left"><code><span><center><code>PSML CODE</code></center></span><br><hr color="green"><textarea id="code" name="codes" style="height:85%;width:98.5%;border:1px solid green;resize:none;word-wrap:break-word;outline:none;">{codes}</textarea></div>
<div name="html" autoHeight style="height:398px;width:50%;border:1px solid red;float:left"><div style="height:49%;width:99.55%;border:1px solid red;word-wrap:break-word"><span><code><center>View</center></code></span><br><hr color="red"><div style="font-family:Default">{html}</div></div>
<div name="htmlELE" autoHeight style="height:50%;width:99.6%;border:1px solid blue;"><!--<span><center><code>HTML ELEMENTS</code></center></span><hr color="blue"></center>--><textarea rows=10 readonly=true style="height:98%;width:99%;resize:none;word-wrap:break-word;outline:none;border:0">{htmlELE}</textarea></div>
</div></div>
<center><button type="submit" style="border:0;background-color:blue;outline:none;color:white">Compile</button></center>
</form>
</body>
</html>
""")
    except Exception as err:
        form=form=FormsDict(bottle.request.POST).decode("utf8")
        codes=''.join(form.get("codes").split("\r"))
        codes="&lt;".join(codes.split("<"))
        codes="&gt;".join(codes.split(">"))
        dat=request.environ.get("beaker.session")
        dat["code"]=codes
        dat.save()
        codes="<".join(codes.split("&lt;"))
        codes=">".join(codes.split("&gt;"))
        raise
        return template(f"""<!doctype html>
<html>
<head>
<meta charset="utf8">
<title>PSML</title>
<script src="http://apps.bdimg.com/libs/jquery/2.1.1/jquery.min.js"></script>
<script src="/script/auto.js"></script>
<link href="bin/__init__.css" rel="stylesheet" type="text/css"/>
</head>
<body>
<form action="/change" method="post">
<center>
<div autoHeight style="display:block;height:400px">
<div autoHeight style="height:396px;width:49%;border:1px solid green;font-family:Monospace;float:left"><code><span><code>PSML CODE</code></span><br><hr color="green"><textarea id="code" name="codes" style="height:90.2%;width:98%;border:1px solid green;resize:none;word-wrap:break-word;outline:none;">{codes}</textarea></div>
<div name="html" autoHeight style="height:398px;width:49%;border:1px solid red;font-family:Monospace;float:left;word-wrap:break-word"><code><span><code>View</code></span><br><hr color="red"><font color="red">Exception: {err}</font>
</code></div><br>
</div>
<button type="submit" style="border:0;background-color:blue;outline: none;color:white">Compile</button>
</center>
</form>
</body>
</html>
""")

app=default_app()
app=SessionMiddleware(app, session_opts)
if __name__=="__main__":
    run_server()

def run_server():
    run(app=app,host="127.0.0.1")
