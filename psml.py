#!/usr/bin/python3
"""
LMFS PSML Compiler (Origin)
It's a free(libre) software
"""
from re import *
import os
try:
    from rlcompleter import*
except:
    print("\033[95;1mWarning\033[0m: Your python unsupport GNU Readline")
__version__="0.5.2.2"
__author__="<Lone_air_Use@outlook.com>"
import warnings,traceback
import flask
App=flask.Flask(__name__)
warnings.filterwarnings("ignore")
html=""
pages={}
pages_c=0
def getpage(branch):
    return pages[branch]
def nox(text,x):
    return text.strip(x)
def ignore(text,x):
    return "".join(text.split(x))
def isempty(text):
    text=ignore(text," ")
    text=ignore(text,"\t")
    return text==""
def lclean(l):
    last=[]
    while last!=l:
        last=l.copy()
        for i in range(len(l)):
            if isempty(l[i]): l.__delitem__(i)
    return l
def tohtml(code):
    code="&amp;".join(code.split("&"))
    code="&nbsp;".join(code.split(" "))
    code="&lt;".join(code.split("<"))
    code="&gt;".join(code.split(">"))
    return code
def fcompile(path,string,mode=1,werr=[]):
    html=compile(string,mode=mode,werr=[])
    if mode!=3:
        try:
            os.mkdir(path)
        except:pass
        for i in html.keys():
            if i in ("Nothing", "INSERT"): continue
            else:
                with open(os.path.join(path,i+".html"), "w") as f:
                    f.write(html[i])
    else:
        with open(path+".compiled.psml", "w") as f:
            f.write(html)
    return
def compile(string,mode=1,varpre={},nobe=0,werr=[],brc="index",brc_=1):
    global html, pages, pages_c
    routes=0
    html=""
    codes=string
    tpe=""
    ele=""
    head=""
    branch=brc
    bran=brc_
    if not nobe:
        head="<html"
    datas=""
    data=""
    codes=''.join(sub(r"[|]([\w\W]*?)[|]","",codes))
    codes=codes.split("\n")
    idx=0
    del_=0
    codes_=codes.copy()
    alload=[]
    for i in codes_:
        i=sub("\t","",i)
        i=sub(" ","",i)
        if(i==""):
            del codes[idx-del_]
            del_+=1
        idx+=1
    cpd=0
    dels=0
    wh=0
    var=varpre
    used=[]
    for i in codes:
        dei=i
        if "".join("".join(dei.split(" ")).split("\t"))=="":
            del codes[wh-dels]
            dels+=1
            continue
        if len(i)>0:
            if i[0]=="/":
                if len(i)>1:
                    if i[1]==">":
                        del codes[wh-dels]
                        dels+=1
                        continue
            if i[0]=="#":
                i=i.split("#")
                del i[0]
                i="#".join(i)
                n=findall(r"[<]([\w\W]*?)[>]",i)
                v=findall(r"(.*?)[<]",i)
                if len(v)>1:
                    if mode==2:
                        html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlsError: Only 1 control command"""
                        html+="</font></code>"
                        
                    else:
                        print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlsError: Only 1 control command""")
                    return html
                elif len(v)<1:
                    if mode==2:
                        html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlsError: Need 1 control command"""
                        html+="</font></code>"
                        
                    else:
                        print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlsError: Need 1 control command""")
                    return html
                v="".join(v[0].split(" "))
                if len(n)<1:
                    n=[""]
                n=n[0].split(",")
                if v in ("insert","title","encoding","goto","desb","js","css","html","ico","php"):
                    if v=="insert":
                        if len(n)>1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Only 1 argument need"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Only 1 argument need""")
                            return html
                        elif len(n)<1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Need 1 argument"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Need 1 argument""")
                            return html
                        n=os.path.realpath(",".join(n))
                        if n in alload:
                            if "repeated-insertion" in werr:
                                if mode==2:
                                    html+=f"""<code>PSML RAIED <font color="red">A FORCE ERROR</font><br>
MODULE <font color="green"><wh-dels+1><font><br>
<font color="orange">   {dei}</font><br>
<font color="red"> FileLoaderError: Duplicate reference to the same file '{n}'</font></code>"""
                                    return html
                                else:
                                    print(f"""PSML RAISED \033[91;1mA FORCE ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
FileLoaderError: Duplicate reference to the same file '{n}'""")
                                    return html
                            else:
                                if mode!=2:
                                    print(f"""PSML RAISED \033[95;1mA WARNING\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
FileLoaderWarning: Duplicate reference to the same file '{n}' [\033[95;1mrepeated-insertion\033[0m]""")
                                    read=""
                        else:
                            alload.append(n)
                            try:
                                read=open(n).read()
                            except:
                                if mode==2:
                                    html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
FileReaderError: Failed to read {repr(n)}"""
                                    html+="</font></code>"
                                
                                else:
                                    print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
FileReaderError: Failed to read {repr(n)}""")
                                return html
                        del codes[wh-dels]
                        read=read.split("\n")
                        read=["|INSERT|",*read]
                        cpd=0
                        for ist in read:
                            if "".join("".join(ist.split(" ")).split("\t"))=="":
                                continue
                            codes.insert(wh-dels+cpd,ist)
                            cpd+=1
                        if (wh-dels+cpd)<len(codes):
                            codes.insert(wh-dels+cpd,"!~*")
                    if v=="php":
                        if len(n)>1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Only 1 argument need"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Only 1 argument need""")
                            return html
                        elif len(n)<1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Need 1 argument"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Need 1 argument""")
                            return html
                        n=",".join(n)
                        try:
                            read=open(n).read()
                        except:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
FileReaderError: Failed to read {repr(n)}"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
FileReaderError: Failed to read {repr(n)}""")
                            return html
                        del codes[wh-dels]
                        read=read.split("\n")
                        read=["|INSERT PHP|","php{","[",*read,"]","}"]
                        cpd=0
                        for ist in read:
                            if "".join("".join(ist.split(" ")).split("\t"))=="":
                                continue
                            codes.insert(wh-dels+cpd,ist)
                            cpd+=1
                        if (wh-dels+cpd)<len(codes):
                            codes.insert(wh-dels+cpd,"!~*")
                    elif v=="js":
                        if len(n)>1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Only 1 argument need"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Only 1 argument need""")
                            return html
                        elif len(n)<1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Need 1 argument"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Need 1 argument""")
                            return html
                        n=",".join(n)
                        del codes[wh-dels]
                        read=["|JavaScript|","html","{","[<script language='javascript' src="+repr(n)+">]","}"]
                        cpd=0
                        for ist in read:
                            if "".join("".join(ist.split(" ")).split("\t"))=="":
                                continue
                            codes.insert(wh-dels+cpd,ist)
                            cpd+=1
                        if (wh-dels+cpd)<len(codes):
                            codes.insert(wh-dels+cpd,"!~*")
                    elif v=="html":
                        if len(n)>1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Only 1 argument need"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Only 1 argument need""")
                            return html
                        elif len(n)<1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Need 1 argument"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Need 1 argument""")
                            return html
                        n=",".join(n)
                        if n not in("4.01","5","x"):
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
LookUpError: Unknown version {n}"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
LookUpError: Unknown version {n}""")
                            return html
                        del codes[wh-dels]
                        if n=="4.01":
                            ins="""HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
"http://www.w3.org/TR/html4/loose.dtd"
"""
                        elif n=="5":
                            ins="html"
                        elif n=="x":
                            ins="""html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd"
"""
                        read=["|DOCUMENT TYPE OF HTML|","doc","{",ins,"}"]
                        for ist in read:
                            if "".join("".join(ist.split(" ")).split("\t"))=="":
                                continue
                            codes.insert(wh-dels+cpd,ist)
                            cpd+=1
                        if (wh-dels+cpd)<len(codes):
                            codes.insert(wh-dels+cpd,"!~*")
                    elif v=="css":
                        if len(n)>1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Only 1 argument need"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Only 1 argument need""")
                            return html
                        elif len(n)<1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Need 1 argument"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Need 1 argument""")
                            return html
                        n=",".join(n)
                        del codes[wh-dels]
                        read=["|CSS|","html","{","[<link rel='stylesheet' type='text/css' href="+repr(n)+">]","}"]
                        cpd=0
                        for ist in read:
                            if "".join("".join(ist.split(" ")).split("\t"))=="":
                                continue
                            codes.insert(wh-dels+cpd,ist)
                            cpd+=1
                        if (wh-dels+cpd)<len(codes):
                            codes.insert(wh-dels+cpd,"!~*")
                    elif v=="ico":
                        if len(n)>1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Only 1 argument need"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Only 1 argument need""")
                            return html
                        elif len(n)<1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Need 1 argument"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Need 1 argument""")
                            return html
                        n=",".join(n)
                        del codes[wh-dels]
                        read=["|ICO|","html","{","[<link rel='Shortcut Icon' type='image/x-icon' href="+repr(n)+">]","}"]
                        cpd=0
                        for ist in read:
                            if "".join("".join(ist.split(" ")).split("\t"))=="":
                                continue
                            codes.insert(wh-dels+cpd,ist)
                            cpd+=1
                        if (wh-dels+cpd)<len(codes):
                            codes.insert(wh-dels+cpd,"!~*")
                    elif v=="title":
                        if len(n)>1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Only 1 argument need"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Only 1 argument need""")
                            return html
                        elif len(n)<1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Need 1 argument"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Need 1 argument""")
                            return html
                        n=",".join(n)
                        del codes[wh-dels]
                        read=["title","{",f"    inner:[{n}]","    end:true","}"]
                        read=["|HTML TITLE|",*read]
                        cpd=0
                        for ist in read:
                            if "".join("".join(ist.split(" ")).split("\t"))=="":
                                continue
                            codes.insert(wh-dels+cpd,ist)
                            cpd+=1
                        if (wh-dels+cpd)<len(codes):
                            codes.insert(wh-dels+cpd,"!~*")
                    elif v=="encoding":
                        if len(n)>1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Only 1 argument need"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Only 1 argument need""")
                            return html
                        elif len(n)<1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Need 1 argument"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Need 1 argument""")
                            return html
                        n=",".join(n)
                        del codes[wh-dels]
                        read=["meta","{",f"    charset:[{n}]","}"]
                        read=["|HTML ENCODING|",*read]
                        cpd=0
                        for ist in read:
                            if "".join("".join(ist.split(" ")).split("\t"))=="":
                                continue
                            codes.insert(wh-dels+cpd,ist)
                            cpd+=1
                        if (wh-dels+cpd)<len(codes):
                            codes.insert(wh-dels+cpd,"!~*")
                    if v=="goto":
                        if len(n)>2:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Only 1 argument need"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Only 1 argument need""")
                            return html
                        elif len(n)==1:
                            n.append("0")
                        elif len(n)<1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Need 1 argument"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Need 1 argument""")
                            return html
                        try:
                            float(n[1])
                        except:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Time must be a number"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Time must be a number""")
                        del codes[wh-dels]
                        read=["meta","{","    http-equiv:refresh",f"    content:[{n[1]};url={n[0]}]","}"]
                        read=["|GOTO|",*read]
                        cpd=0
                        for ist in read:
                            if "".join("".join(ist.split(" ")).split("\t"))=="":
                                continue
                            codes.insert(wh-dels+cpd,ist)
                            cpd+=1
                        if (wh-dels+cpd)<len(codes):
                            codes.insert(wh-dels+cpd,"!~*")
                    if v=="desb":
                        if len(n)==1:
                            n.append("")
                        elif len(n)<1:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlArgumentsError: Need 1 argument"""
                                html+="</font></code>"
                                
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlArgumentsError: Need 1 argument""")
                            return html
                        kb=n[0]
                        del n[0]
                        n=",".join(n)
                        del codes[wh-dels]
                        read=["meta","{",f"    name:[{kb}]",f"    content:[{n}]","}"]
                        read=["|DESCRIBE|",*read]
                        cpd=0
                        for ist in read:
                            if "".join("".join(ist.split(" ")).split("\t"))=="":
                                continue
                            codes.insert(wh-dels+cpd,ist)
                            cpd+=1
                        if (wh-dels+cpd)<len(codes):
                            codes.insert(wh-dels+cpd,"!~*")
                else:
                    if mode==2:
                        html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh-dels+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(dei)}</font><br><font color="red">
ControlNameError: Unknown key {repr(v)}"""
                        html+="</font></code>"
                        
                    else:
                        print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh-dels+1}\033[0m
    \033[93m{dei}\033[0m
ControlNameError: Unknown key {repr(v)}""")
                    return html
        wh+=1
    dels=0
    wh=0
    for obj in codes:
        if len(obj)>=2:
            if obj[0]+obj[1]=="/>":
                del codes[wh-dels]
                dels+=1
        if "".join("".join(obj.split(" ")).split("\t"))=="":
            del codes[wh-dels]
            dels+=1
        if obj=="!~*":
            if wh-dels==len(codes)-1:
                del codes[wh-dels]
                dels+=1
        wh+=1
    codes="\n".join(codes)
    tmps=findall(r"[[]([\w\W]*?)[]]",codes)
    codes="".join(codes)
    if 1:
        codes="&Bs&".join(codes.split("\\{"))
        codes="&Be&".join(codes.split("\\}"))
        codes="&Ms&".join(codes.split("\\["))
        codes="&Me&".join(codes.split("\\]"))
        codes="&Se&".join(codes.split("\\)"))
        codes="&Ss&".join(codes.split("\\("))
        codes="&sp&".join(codes.split("\\;"))
        codes="&is&".join(codes.split("\\:"))
        codes="&in&".join(codes.split("\\-"))
        codes="&or&".join(codes.split("\\|"))
        codes="&no&".join(codes.split("\\ "))
        codes="&ord&".join(codes.split("\\#"))
        codes="&voff&".join(codes.split("\\>"))
        codes="&von&".join(codes.split("\\<"))
        codes="&vuse&".join(codes.split("\\$"))
        codes="&cod&".join(codes.split("\\`"))
    for i in tmps:
        dfl=i
        i="&Bs&".join(i.split("{"))
        i="&Be&".join(i.split("}"))
        i="&Ms&".join(i.split("["))
        i="&Me&".join(i.split("]"))
        i="&Se&".join(i.split(")"))
        i="&Ss&".join(i.split("("))
        i="&sp&".join(i.split(";"))
        i="&is&".join(i.split(":"))
        i="&in&".join(i.split("-"))
        i="&-&".join(i.split("!~*"))
        i="&end&".join(i.split("\n"))
        i="&or&".join(i.split("|"))
        i="&no&".join(i.split(" "))
        i="&ord&".join(i.split("#"))
        i="&voff&".join(i.split(">"))
        i="&von&".join(i.split("<"))
        i="&vuse&".join(i.split("$"))
        i="&cod&".join(i.split("`"))
        codes=i.join(codes.split("["+dfl+"]"))
    tmps=findall(r"[`]([\w\W]*?)[`]",codes)
    codes="".join(codes)
    if 1:
        codes="&Bs&".join(codes.split("\\{"))
        codes="&Be&".join(codes.split("\\}"))
        codes="&Ms&".join(codes.split("\\["))
        codes="&Me&".join(codes.split("\\]"))
        codes="&Se&".join(codes.split("\\)"))
        codes="&Ss&".join(codes.split("\\("))
        codes="&sp&".join(codes.split("\\;"))
        codes="&is&".join(codes.split("\\:"))
        codes="&in&".join(codes.split("\\-"))
        codes="&or&".join(codes.split("\\|"))
        codes="&no&".join(codes.split("\\ "))
        codes="&ord&".join(codes.split("\\#"))
        codes="&voff&".join(codes.split("\\>"))
        codes="&von&".join(codes.split("\\<"))
        codes="&vuse&".join(codes.split("\\$"))
        codes="&cod&".join(codes.split("\\`"))
    for i in tmps:
        dfl=i
        i="&Bs&".join(i.split("{"))
        i="&Be&".join(i.split("}"))
        i="&Ms&".join(i.split("["))
        i="&Me&".join(i.split("]"))
        i="&Se&".join(i.split(")"))
        i="&Ss&".join(i.split("("))
        i="&sp&".join(i.split(";"))
        i="&is&".join(i.split(":"))
        i="&in&".join(i.split("-"))
        i="&-&".join(i.split("!~*"))
        i="&end&".join(i.split("\n"))
        i="&or&".join(i.split("|"))
        i="&no&".join(i.split(" "))
        i="&ord&".join(i.split("#"))
        i="&voff&".join(i.split(">"))
        i="&von&".join(i.split("<"))
        i="&vuse&".join(i.split("$"))
        i="&cod&".join(i.split("`"))
        codes=i.join(codes.split("`"+dfl+"`"))


    codes=''.join(sub(r"[|]([\w\W]*?)[|]","",codes))
    codes=";".join(codes.split('\n'))
    codes="}!~*;".join(codes.split("}"))
    codes=")!~*;".join(codes.split(");"))
    if mode==3:
        return codes
    tmps=codes.split("!~*;").copy()
    tmpc=[]
    for i in tmps:
        if sub(" ",'',''.join(i.split("!~*")))=="":
            continue
        if sub(";",'',''.join(i.split("!~*")))=="":
            continue
        if sub("\t","","".join(i.split("!~*")))=="":
            continue
        ist=i.split("!~*")
        for j in ist:
            tmpc.append(j)
    for wh in range(len(tmpc)):
        i=tmpc[wh]
        if i=="":
            continue
        ele=findall(r'(.*?)[(]',i)
        if len(ele)<1:
            syn="}"
            ele=findall(r'(.*?)[{]',i)
            if len(ele)<1:
                ele=[i]
            elif len(ele)>1:
                if mode==2:
                    html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
SyntaxError: Invalid Syntax (Element only 1)"""
                    html+="</font></code>"
                    
                else:
                    print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
SyntaxError: Invalid Syntax (Element only 1)""")
                return html
        elec=ele.copy()
        for el in range(len(elec)):
            obj=ele[el]
            obj="".join(obj.split(" "))
            obj="".join(obj.split("\t"))
            ele[el]=obj
        tpe=findall(r'[(](.*?)[)]',i)
        tpen=tpe.copy()
        tpe=[]
        for nosep in tpen:
            tpe.append("".join(nosep.split(";")))
        if len(tpe)<1:
            tpe.append("/")
        elif len(tpe)>1:
            if 1:
                if mode==2:
                    html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
SyntaxError: Invalid Syntax (Type of element only one or zero)"""
                    html+="</font></code>"
                    
                else:
                    print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
SyntaxError: Invalid Syntax (Type of element only one or zero)""")
            return html
        if len(tpe)!=len(ele):
            if 1:
                if mode==2:
                    html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ReadyCompilingError: The length of types isn't equal to the length of elements"""
                    html+="</font></code>"
                    
                else:
                    print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ReadyCompilingError: The length of types isn't equal to the length of elements""")
                return html
        butn=("script", "style", "html", "java", "php", "doc", "var", "begin", "route", "Command")
        special=("begin", "route")
        noarg=("Command",)
        for count in ele:
            count=sub(" ",'',str(count))
            defcnt=count
            count=sub(";","",str(count))
            count="".join(count.split('\t'))
            if count=="":
                if mode==2:
                    html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
SyntaxError: Invalid Syntax (Need an element)"""
                    html+="</font></code>"
                else:
                    print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
SyntaxError: Invalid Syntax (Need an element)""")
                return html
            if tpe[ele.index(defcnt)] not in ("/",""):
                if not count in butn:
                    if count=="doc":
                        pass
                    else:
                        html+=f"<{count} type={repr(tpe[ele.index(defcnt)])}"
            else:
                if not count in butn:
                    html+=f"<{count}"
            if len(findall(r'[{](.*?)[}]',i))>0 or count in noarg:
                inner=True
                data=findall(r'[{](.*?)[}]',i)
                datan=data.copy()
                data=[]
                for apd in datan:
                    ists="".join(apd.split(" "))
                    ists="".join(ists.split(";"))
                    ists="".join(ists.split("\t"))
                    if ists!="":
                        data.append(apd)
                if data==[] and count not in noarg:
                    if mode==1:
                        print(f"""PSML RAISED \033[96;1mA NOTE\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
Element.dat: No data get""")
                elem=[]
                dats=[]
                dts=data.copy()
                data=[]
                tmp=""
                for a in dts:
                    a=a.split(";")
                    for b in a:
                        data.append(b)
                for j in data:
                    if not j:
                        continue
                    if not count in butn or count in special:
                        tmp=sub(" ",'',str(j))
                        tmp="".join(tmp.split('\t'))
                    VARF=findall("\$\<(.*?)\>",tmp)
                    for VARFR in VARF:
                        if(VARFR) in var.keys():
                            tmp=var[VARFR].join(tmp.split(f"$<{VARFR}>"))
                            used.append(VARFR)
                        else:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
VariableError: {repr(VARFR)} was not declared in this scope"""
                                html+="</font></code>"
                    
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
VariableError: \033[91;1;4m{repr(VARFR)}\033[0m was not declared in this scope""")
                            return html
                    tmp=tmp.split(":")
                    elem.append(tmp[0])
                    try:
                        datele=tmp[0]
                    except:
                        if mode==2:
                            html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ELEMENT.DATAS.NAMEERROR: LENGTH OF DATA HAS SMALLER THAN 1"""
                            html+="</font></code>"
                            
                        else:
                            print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ELEMENT.DATAS.NAMEERROR: LENGTH OF DATA HAS SMALLER THAN 1""")
                        return html
                    del tmp[0]
                    tmp=":".join(tmp)
                    dats.append(tmp)
                    dat=tmp
                    datele=sub(";","",datele)
                    if dat!="" or ":" in j:
                        tmp=(" "+datele+"="+repr(dat))
                    else:
                        tmp=(" "+datele)
                    if datele=="inner" or datele=="psml":
                        continue
                    elif datele=="br":
                        continue
                    elif datele=="end":
                        continue
                    elif datele=="word-wrap":
                        continue
                    if count=="Command":tmp="";break
                    elif count=="begin":
                        if not nobe:
                            head+=tmp
                        else:
                            break
                        continue
                    elif count=="doc":
                        if not "inner" in elem:
                            elem.append("inner")
                        datan=data.copy()
                        while 1:
                            try:
                                del datan[datan.index("")]
                            except:
                                break
                        doctype="\n".join(datan)
                        dats.append("")
                        head=f"<!DOCTYPE {doctype}>\n"+head
                        break
                    elif (datele=="source") and (count.lower() in ("audio","video")):
                        if count.lower()=="audio":
                            if not "inner" in elem:
                                elem.append("inner")
                            dats.append(f"<source src={repr(dat)} type='audio/mpeg'>\n")
                        if count.lower()=="video":
                            if not "inner" in elem:
                                elem.append("inner")
                            dats.append(f"<source src={repr(dat)} type='video/mp4'>\n")
                        continue
                    elif count=='style':
                        if not "inner" in elem:
                            elem.append("inner")
                        style="\n".join(data)
                        dats.append(f"""<style type='text/css'>
{style}
</style>""")
                        break
                    elif count=='script':
                        if not "inner" in elem:
                            elem.append("inner")
                        script="\n".join(data)
                        dats.append(f"""<script language="javascript">
{script}
</script>""")
                        break
                    elif count=='java':
                        if not "inner" in elem:
                            elem.append("inner")
                        jsp="\n".join(data)
                        dats.append(f"""<%
{jsp}
%>""")
                        break
                    elif count=='php':
                        if not "inner" in elem:
                            elem.append("inner")
                        php="\n".join(data)
                        dats.append(f"""<?php
{php}
?>""")
                        break
                    elif count=="py":
                        if not 'inner' in elem:
                            elem.append("inner")
                        py_=[]
                        for Pcode in data:
                            py_.append(nosem(Pcode))
                        py_="\n".join(py_)
                        try:
                            exec(py_)
                        except:
                            traceback.print_exc()
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
PythonCodeExecError: Python raised a fatal error"""
                                html+="</font></code>"
                
                            else:
                                 print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
PythonCodeExecError: Python raised a fatal error""")
                            return html
                    elif count=='html':
                        if not "inner" in elem:
                            elem.append("inner")
                        inner="\n".join(data)
                        dats.append(f"""{inner}""")
                        break
                    elif count=="var":
                        for VAR in data:
                            VARN=VAR.split(":")[0]
                            VARV=":".join(VAR.split(":")[1:])
                            VARV="".join(VARV.split(" "))
                            VARV="".join(VARV.split("\t"))
                            VARN="".join(VARN.split(" "))
                            VARN="".join(VARN.split("\t"))
                            if("".join("".join(VARN.split(" ")).split("\t"))==""):
                                continue
                            VARFD=findall(r"\$\<(.*?)\>",VARV)
                            for VARFR in VARFD:
                                if(VARFR in list(var.keys())):
                                    VARV=var[VARFR].join(VARV.split(f"$<{VARFR}>"))
                                else:
                                    if mode==2:
                                        html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
VariableError: {repr(VARFR)} was not declared in this scope"""
                                        html+="</font></code>"
                    
                                    else:
                                        print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
VariableError: \033[91;1;4m{repr(VARFR)}\033[0m was not declared in this scope""")
                                    return html
                            var[VARN]=VARV
                        break
                    elif count=="route":
                        args=tpe[ele.index(defcnt)]
                        argl=args.split("~")
                        argl=lclean(argl)
                        r_data=[]
                        r_argl=[]
                        if(len(argl)<2):
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
RouteError: Cannot get the route"""
                                html+="</font></code>"
                    
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
RouteError: Cannot get the route""")
                            return html
                        for psml in argl:
                            psml="\n".join(psml.split("\\n"))
                            psml="{".join(psml.split("&Bs&"))
                            psml="}".join(psml.split("&Be&"))
                            psml="[".join(psml.split("&Ms&"))
                            psml="]".join(psml.split("&Me&"))
                            psml="(".join(psml.split("&Ss&"))
                            psml=")".join(psml.split("&Se&"))
                            psml=";".join(psml.split("&sp&"))
                            psml=":".join(psml.split("&is&"))
                            psml="-".join(psml.split("&in&"))
                            psml="!~*".join(psml.split("&-&"))
                            psml="\n".join(psml.split("&end&"))
                            psml="|".join(psml.split("&or&"))
                            psml=" ".join(psml.split("&no&"))
                            psml="#".join(psml.split("&ord&"))
                            psml=">".join(psml.split("&voff&"))
                            psml="<".join(psml.split("&von&"))
                            psml="$".join(psml.split("&vuse&"))
                            psml="/".join(psml.split("&cod&"))
                            r_argl.append(psml)
                        for psml in data:
                            psml="\n".join(psml.split("\\n"))
                            psml="{".join(psml.split("&Bs&"))
                            psml="}".join(psml.split("&Be&"))
                            psml="[".join(psml.split("&Ms&"))
                            psml="]".join(psml.split("&Me&"))
                            psml="(".join(psml.split("&Ss&"))
                            psml=")".join(psml.split("&Se&"))
                            psml=";".join(psml.split("&sp&"))
                            psml=":".join(psml.split("&is&"))
                            psml="-".join(psml.split("&in&"))
                            psml="!~*".join(psml.split("&-&"))
                            psml="\n".join(psml.split("&end&"))
                            psml="|".join(psml.split("&or&"))
                            psml=" ".join(psml.split("&no&"))
                            psml="#".join(psml.split("&ord&"))
                            psml=">".join(psml.split("&voff&"))
                            psml="<".join(psml.split("&von&"))
                            psml="$".join(psml.split("&vuse&"))
                            psml="/".join(psml.split("&cod&"))
                            r_data.append(psml)
                        Rc="@App.route(%s, methods=%s)\n"%(repr(r_argl[0]), r_argl[1])
                        Rc+="def r%d(%s):\n"%(routes,", ".join(r_argl[2:]))
                        for Rcode in r_data:
                            Rc+="    "+Rcode+"\n"
                        try:
                            exec(Rc)
                        except:
                            traceback.print_exc()
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
RouteError: Python raised a fatal error"""
                                html+="</font></code>"
                
                            else:
                                 print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
RouteError: Python raised a fatal error""")
                            return html
                        routes+=1
                        break
                if count=="Command":
                    cmd=lclean(tpe[ele.index(defcnt)].split(" "))
                    if len(cmd)<1:
                        if mode==2:
                            html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
CommandError: No command got"""
                            html+="</font></code>"
                
                        else:
                            print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
CommandError: No command got""")
                            return html
                    if cmd[0]=="Run":
                        if len(cmd)<2:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Argument weren't enough"""
                                html+="</font></code>"
                
                            else:
                                 print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Argument weren't enough""")
                            return html
                        if cmd[1]=="Server":
                            if len(cmd)<3:
                                try:
                                    App.run()
                                except:
                                    traceback.print_exc()
                                    if mode==2:
                                        html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
RunServerError: Python raised a fatal error"""
                                        html+="</font></code>"
                
                                    else:
                                        print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
RunServerError: Python raised a fatal error""")
                                        return html
                            else:
                                host=(stat:=cmd[2].split(":"))[0]
                                port=stat[1]
                                try:
                                    App.run(host=host, port=port)
                                except:
                                    traceback.print_exc()
                                    if mode==2:
                                        html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
RunServerError: Python raised a fatal error"""
                                        html+="</font></code>"
                
                                    else:
                                        print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
RunServerError: Python raised a fatal error""")
                                    return html
                        else:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: No such argument"""
                                html+="</font></code>"
                    
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: No such argument""")
                            return html
                    elif cmd[0]=="New":
                        if len(cmd)<2:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Argument weren't enough"""
                                html+="</font></code>"
                
                            else:
                                 print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Argument weren't enough""")
                            return html
                        if cmd[1]=="Page":
                            if len(cmd)<3:
                                html="\n".join(html.split("\\n"))
                                html="{".join(html.split("&Bs&"))
                                html="}".join(html.split("&Be&"))
                                html="[".join(html.split("&Ms&"))
                                html="]".join(html.split("&Me&"))
                                html="(".join(html.split("&Ss&"))
                                html=")".join(html.split("&Se&"))
                                html=";".join(html.split("&sp&"))
                                html=":".join(html.split("&is&"))
                                html="-".join(html.split("&in&"))
                                html="!~*".join(html.split("&-&"))
                                html="\n".join(html.split("&end&"))
                                html="|".join(html.split("&or&"))
                                html=" ".join(html.split("&no&"))
                                html="#".join(html.split("&ord&"))
                                html=">".join(html.split("&voff&"))
                                html="<".join(html.split("&von&"))
                                html="$".join(html.split("&vuse&"))
                                html="/".join(html.split("&cod&"))
                                pages[branch]=head+">\n"+html+"</html>" if not nobe else html
                                branch="Page"+str(pages_c)
                            else:
                                html="{".join(html.split("&Bs&"))
                                html="}".join(html.split("&Be&"))
                                html="[".join(html.split("&Ms&"))
                                html="]".join(html.split("&Me&"))
                                html="(".join(html.split("&Ss&"))
                                html=")".join(html.split("&Se&"))
                                html=";".join(html.split("&sp&"))
                                html=":".join(html.split("&is&"))
                                html="-".join(html.split("&in&"))
                                html="!~*".join(html.split("&-&"))
                                html="\n".join(html.split("&end&"))
                                html="|".join(html.split("&or&"))
                                html=" ".join(html.split("&no&"))
                                html="#".join(html.split("&ord&"))
                                html=">".join(html.split("&voff&"))
                                html="<".join(html.split("&von&"))
                                html="$".join(html.split("&vuse&"))
                                html="/".join(html.split("&cod&"))
                                pages[branch]=head+">\n"+html+"</html>" if not nobe else html
                                branch=cmd[2]
                            html=""
                            head="" if nobe else "<html"
                            pages_c+=1
                            bran=1
                        else:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: No such argument"""
                                html+="</font></code>"
                    
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: No such argument""")
                            return html
                    elif cmd[0]=="End":
                        if bran==0:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
BranchError: No branch"""
                                html+="</font></code>"
                    
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
BranchError: No branch""")
                            return html
                        if(len(cmd)<2):
                            html="{".join(html.split("&Bs&"))
                            html="}".join(html.split("&Be&"))
                            html="[".join(html.split("&Ms&"))
                            html="]".join(html.split("&Me&"))
                            html="(".join(html.split("&Ss&"))
                            html=")".join(html.split("&Se&"))
                            html=";".join(html.split("&sp&"))
                            html=":".join(html.split("&is&"))
                            html="-".join(html.split("&in&"))
                            html="!~*".join(html.split("&-&"))
                            html="\n".join(html.split("&end&"))
                            html="|".join(html.split("&or&"))
                            html=" ".join(html.split("&no&"))
                            html="#".join(html.split("&ord&"))
                            html=">".join(html.split("&voff&"))
                            html="<".join(html.split("&von&"))
                            html="$".join(html.split("&vuse&"))
                            html="/".join(html.split("&cod&"))
                            pages[branch]=head+">\n"+html+"</html>" if not nobe else html
                            branch="Nothing"
                            bran=0
                            html=""
                            head="" if nobe else "<html"
                        else:
                            if mode==2:
                                html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: No argument"""
                                html+="</font></code>"
                    
                            else:
                                print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: No argument""")
                            return html
                    else:
                        if mode==2:
                            html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
CommandError: No such command"""
                            html+="</font></code>"
                    
                        else:
                            print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
CommandError: No such command""")
                        return html
                    html+=tmp
                if "psml" in elem:
                    old_html=html
                    if not count in butn:
                        if "end" in elem:
                            if dats[elem.index("end")].lower()=="true":
                                psml=dats[elem.index("psml")]
                                psml="\n".join(psml.split("\\n"))
                                psml="{".join(psml.split("&Bs&"))
                                psml="}".join(psml.split("&Be&"))
                                psml="[".join(psml.split("&Ms&"))
                                psml="]".join(psml.split("&Me&"))
                                psml="(".join(psml.split("&Ss&"))
                                psml=")".join(psml.split("&Se&"))
                                psml=";".join(psml.split("&sp&"))
                                psml=":".join(psml.split("&is&"))
                                psml="-".join(psml.split("&in&"))
                                psml="!~*".join(psml.split("&-&"))
                                psml="\n".join(psml.split("&end&"))
                                psml="|".join(psml.split("&or&"))
                                psml=" ".join(psml.split("&no&"))
                                psml="#".join(psml.split("&ord&"))
                                psml=">".join(psml.split("&voff&"))
                                psml="<".join(psml.split("&von&"))
                                psml="$".join(psml.split("&vuse&"))
                                psml="`".join(psml.split("&cod&"))
                                psml+="\nCommand(End)"
                                result=compile(psml,mode=mode,varpre=var,nobe=1,brc="INSERT",brc_=bran)
                                if(type(result)!=dict):
                                    if mode==2:
                                        html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
PsmlInserRaisedError"""
                                        html+="</font></code>"
                    
                                    else:
                                        print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
PsmlInsertRaisedError""")
                                    return html
                                else:
                                    old_html+=">"+result["INSERT"]
                                html=old_html
                            else:
                            #if dats[elem.index("end")].lower()=="true":
                                psml=dats[elem.index("psml")]
                                psml="\n".join(psml.split("\\n"))
                                psml="{".join(psml.split("&Bs&"))
                                psml="}".join(psml.split("&Be&"))
                                psml="[".join(psml.split("&Ms&"))
                                psml="]".join(psml.split("&Me&"))
                                psml="(".join(psml.split("&Ss&"))
                                psml=")".join(psml.split("&Se&"))
                                psml=";".join(psml.split("&sp&"))
                                psml=":".join(psml.split("&is&"))
                                psml="-".join(psml.split("&in&"))
                                psml="!~*".join(psml.split("&-&"))
                                psml="\n".join(psml.split("&end&"))
                                psml="|".join(psml.split("&or&"))
                                psml=" ".join(psml.split("&no&"))
                                psml="#".join(psml.split("&ord&"))
                                psml=">".join(psml.split("&voff&"))
                                psml="<".join(psml.split("&von&"))
                                psml="$".join(psml.split("&vuse&"))
                                psml="`".join(psml.split("&cod&"))
                                psml+="\nCommand(End)"
                                result=compile(psml,mode=mode,varpre=var,nobe=1,brc="INSERT",brc_=bran)
                                if(type(result)!=dict):
                                    if mode==2:
                                        html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
PsmlInserRaisedError"""
                                        html+="</font></code>"
                    
                                    else:
                                        print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
PsmlInsertRaisedError""")
                                    return html
                                else:
                                    old_html+=result["INSERT"]
                                html=old_html
                        else:
                            if 1:
                                psml=dats[elem.index("psml")]
                                psml="\n".join(psml.split("\\n"))
                                psml="{".join(psml.split("&Bs&"))
                                psml="}".join(psml.split("&Be&"))
                                psml="[".join(psml.split("&Ms&"))
                                psml="]".join(psml.split("&Me&"))
                                psml="(".join(psml.split("&Ss&"))
                                psml=")".join(psml.split("&Se&"))
                                psml=";".join(psml.split("&sp&"))
                                psml=":".join(psml.split("&is&"))
                                psml="-".join(psml.split("&in&"))
                                psml="!~*".join(psml.split("&-&"))
                                psml="\n".join(psml.split("&end&"))
                                psml="|".join(psml.split("&or&"))
                                psml=" ".join(psml.split("&no&"))
                                psml="#".join(psml.split("&ord&"))
                                psml=">".join(psml.split("&voff&"))
                                psml="<".join(psml.split("&von&"))
                                psml="$".join(psml.split("&vuse&"))
                                psml="`".join(psml.split("&cod&"))
                                psml+="\nCommand(End)"
                                result=compile(psml,mode=mode,varpre=var,nobe=1,brc="INSERT",brc_=bran)
                                if(type(result)!=dict):
                                    if mode==2:
                                        html=f"""<code>PSML RAISED <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
PsmlInserRaisedError"""
                                        html+="</font></code>"
                    
                                    else:
                                        print(f"""PSML RAISED \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
PsmlInsertRaisedError""")
                                    return html
                                else:
                                    old_html+=">"+result["INSERT"]
                                html=old_html
                    html=old_html
                if "inner" in elem:
                    if not count in butn and "psml" not in elem:
                        if "end" in elem:
                            if dats[elem.index("end")].lower()=="true":
                                html+=f">{dats[elem.index('inner')]}</{count}>\n"
                            else:
                                html+=">%s"%dats[elem.index('inner')]
                        else:
                            html+=f">{dats[elem.index('inner')]}"
                    else:
                        if "end" in elem:
                            if dats[elem.index("end")].lower()=="true":
                                html+=f"{dats[elem.index('inner')]}</{count}>\n"
                            else:
                                html+="%s"%dats[elem.index('inner')]
                        else:
                            html+=f"{dats[elem.index('inner')]}"
                else:
                    if not count in butn and "psml" not in elem:
                        if "end" in elem:
                            if dats[elem.index("end")].lower()=="true":
                                html+=f"></{count}>\n"
                            else:
                                html+=">\n"
                        else:
                            html+=">\n"
                    else:
                        if "end" in elem:
                            if dats[elem.index("end")].lower()=="true":
                                html+=f"</{count}>\n"
                if "br" in elem:
                    if dats[elem.index("br")].lower()=="true":
                        html+="<br/>\n"
                if "word-wrap" in elem:
                    if dats[elem.index("word-wrap")].lower()=="true":
                        html+="&end&"
            else:
                html+=">\n"
                if mode==1:
                    print(f"""PSML RAISED \033[96;1mA NOTE\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
Element.dats: No data get""")
    for i in var.keys():
        if(i not in used):
            if "unused-variables" in werr:
                if mode==2:
                    html+=f"""<code>PSML RAIED <font color="red">A FORCE ERROR</font><br>
MODULE <font color="green">{i}<font><br>
<font color="orange">   i:&nbsp;{var[i]}</font><br>
<font color="red">VariablesError: {repr(i)} never use in this scope</font></code>"""
                    return html
                else:
                    print(f"""PSML RAISED \033[91;1mA FORCE ERROR\033[0m
VARIABLE \033[95;1m{i}\033[0m
    \033[93m{i}: {var[i]}\033[0m
VariablesError: \033[91;1;4m{repr(i)}\033[0m never use in this scope""")
                    return html
            else:
                if(mode==1):
                    print(f"""PSML RAISED \033[95;1mA WARNING\033[0m
VARIABLE \033[95;1m{i}\033[0m
    \033[93m{i}: {var[i]}\033[0m
VariablesWarning: \033[95;1;4m{repr(i)}\033[0m never use in this scope [\033[95;1munused-variables\033[0m]""")
    if not nobe and bran:
        html=head+">\n"+html
        html+="</html>"
    html="\n".join(html.split("\\n"))
    html="{".join(html.split("&Bs&"))
    html="}".join(html.split("&Be&"))
    html="[".join(html.split("&Ms&"))
    html="]".join(html.split("&Me&"))
    html="(".join(html.split("&Ss&"))
    html=")".join(html.split("&Se&"))
    html=";".join(html.split("&sp&"))
    html=":".join(html.split("&is&"))
    html="-".join(html.split("&in&"))
    html="!~*".join(html.split("&-&"))
    html="\n".join(html.split("&end&"))
    html="|".join(html.split("&or&"))
    html=" ".join(html.split("&no&"))
    html="#".join(html.split("&ord&"))
    html=">".join(html.split("&voff&"))
    html="<".join(html.split("&von&"))
    html="$".join(html.split("&vuse&"))
    html="`".join(html.split("&cod&"))
    if bran:
        pages[branch]=html
    return pages
def __install__():
    import sys,shutil,os
    path=sys.path.copy()
    for i in path:
        if len(i.split(".zip"))>1:
            del path[path.index(i)]
    shutil.copyfile(__file__,os.path.join(path[1],"PSML.py"))
    shutil.copyfile(os.path.join(os.path.dirname(__file__),"psml_web.py"),os.path.join(path[1],"psml_web.py"))
    shutil.copyfile(os.path.join(os.path.dirname(__file__),"test.psml"),os.path.join(path[1],"test.psml"))
    open(os.path.join(os.path.dirname(sys.executable),"psml"),"w").write("""#!%s
%s"""%(sys.executable,open(__file__).read()))
    shutil.copy(os.path.join(os.path.dirname(__file__),"psml_web.py"),os.path.join(os.path.dirname(sys.executable),"psmlweb"))
    os.chmod(os.path.join(os.path.dirname(sys.executable),"psml"),0o777)
    os.chmod(os.path.join(os.path.dirname(sys.executable),"psmlweb"),0o777)
    return
def __uninstall__():
    import os
    os.remove(__file__)
    os.remove(os.path.join(os.path.dirname(__file__),"psml_web.py"))
    return
def __online__():
    import os,sys
    os.system("%s %s"%(sys.executable,(os.path.join(os.path.dirname(__file__),"psml_web.py"))))
    return

compile.__doc__="""This help for psml
    
string: psml code data
    ------
    Syntax:
                    
        Element(type|/){
                    property:value
                    end:true/false
                    br:true/false
                    word-wrap:true/false
                    (
                               If Element=audio|video:
                                   source:src
                    )
                    (
                               If Element=script|style|html|java|php|doc:
                                   <inner code direct change to html code>
                    )
                    (
                               If Element=var:
                                   <Name of Variable>: <Value of Variable>
                                   ...
                    )
                }(If it isn't the last element, you can write '!~*' before '}'(You don't have to write))
------
    Annotation:
                    
        |Annotation Information|
        /> Annotation Information
------
    Escape Identifier:
            
        &Bs&={
        &Be&=}
        &Ms&=[
        &Ss&=(
        &Se&=)
        &sp&=;
        &or&=Annotation_identifier
        &end&=\\n
        &-&=!~*
        &in&=-
        &is&=:   
        &no&=<space> 
        &ord&=#
        &von&=<
        &voff&=>
        &vuse&=$
        &cod&=/
------
    Compile Programming language:
            
        html(Hypertext Markup Language)
"""

fcompile.__doc__=compile.__doc__

__install__.__doc__="""Copy this .py file to python libraries install directory"""
__uninstall__.__doc__="""Remove this .py file from python libraries install direcotry"""
__online__.__doc__="""Run a online compile web project server for psml"""

if __name__=="__main__":
    import sys,os
    w2err=[]
    realargs=[]
    comp=0
    for i in sys.argv:
        if(i=="-h" or i=="--help"):
            sys.exit(f"""LMFS 2021-2022 (C) PSML Compiler-Version: {__version__}
Usage: psml <psml file> [output: directory name] [targets]
Argument:
    -Werror-*       Make this warning an error for the psml compiler task
    -c --compile    Only pretreatment psml code
    -h --help       Show help of psml
    -v --version    Show version of psml
If you find bugs, you can send to {__author__}""")
        elif(i=="-v" or i=="--version"):
            sys.exit("LMFS PSML Compiler %s"%__version__)
        elif(len(i)>1):
            if(len(i)>2):
                if i[0]+i[1]=="--":
                    temp=list(i)
                    del temp[0]
                    del temp[0]
                    temp="".join(temp)
                    temp=temp.split("-")
                    if temp[0]=="Werror":
                        w2err.append("-".join(temp[1:]))
                    elif temp[0]=="compile":
                        comp=1
                    else:
                        sys.stderr.write(f"\033[91mfatal error\033[0m: cannot find option (--): {repr(temp[0])}\n")
                elif i[0]=="-":
                    temp=list(i)
                    del temp[0]
                    temp="".join(temp)
                    temp=temp.split("-")
                    if temp[0]=="Werror":
                        w2err.append("-".join(temp[1:]))
                    elif temp[0]=="c":
                        comp=1
                    else:
                        sys.stderr.write(f"\033[91mfatal error\033[0m: cannot find option (-): {repr(temp[0])}\n")
                else:
                    realargs.append(i)
            else:
                if i[0]=="-":
                    temp=list(i)
                    del temp[0]
                    temp="".join(temp)
                    temp=temp.split("-")
                    if temp[0]=="Werror":
                        w2err.append("-".join(temp[1:]))
                    elif temp[0]=="c":
                        comp=1
                    else:
                        sys.stderr.write(f"\033[91mfatal error\033[0m: cannot find option (-): {repr(temp[0])}\n")
                else:
                    realargs.append(i)
        else:
            realargs.append(i)
    sys.argv=realargs.copy()
    if(sys.argv==[__file__]):
        code=""
        while(1):
            try:
                code+=input("P> ")+"\n"
            except EOFError:
                print("\r",end="",flush=1)
                sys.exit(compile(code,werr=w2err,mode=1 if not comp else 3))
            except:
                print("\r",end="",flush=1)
                sys.exit()
    if len(sys.argv)==2:
        if os.path.exists(os.path.join(os.getcwd(),sys.argv[1])):
            try:
                try:
                    code=open(os.path.join(os.getcwd(),sys.argv[1]),"rt").read()
                except:
                    sys.exit("\033[91mfatal error\033[0m: cannot read '%s'"%sys.argv[1])
                try:
                    ret=compile(code, werr=w2err,mode=1 if not comp else 3)
                    if ret!=None:
                        sys.exit(ret)
                except:
                    traceback.print_exc()
                    sys.exit("\033[91mfatal error\033[0m: compiling time error")
            except (KeyboardInterrupt,EOFError):
                sys.exit("\033[91mfatal error\033[0m: compile ** break")
        else:
            sys.exit("\033[91mfatal error\033[0m: cannot find '%s'"%sys.argv[1])
    if len(sys.argv)==3:
        if os.path.exists(os.path.join(os.getcwd(),sys.argv[1])):
            try:
                try:
                    code=open(os.path.join(os.getcwd(),sys.argv[1]),"rt").read()
                except:
                    sys.exit("\033[91mfatal error\033[0m: cannot read '%s'"%(sys.argv[1]))
                try:
                    fcompile(sys.argv[2],code,mode=1 if not comp else 3)
                except:
                    traceback.print_exc()
                    sys.exit("\033[91mfatal error\033[0m: compile failed with error")
            except (KeyboardInterrupt,EOFError):
                sys.exit("\033[91mfatal error\033[0m: compile ** break")
        else:
            sys.exit("\033[91mfatal error\033[0m: cannot find '%s'"%sys.argv[1])
