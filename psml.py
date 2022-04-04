#!/usr/bin/python3
"""
LMFS PSML Compiler (Origin)
It's a free(libre) software
"""
from re import *
import os,sys
__version__="1.2.2"
__author__="<Lone_air_Use@outlook.com>"
import warnings,traceback
App=None
warnings.filterwarnings("ignore")
html=""
pages={}
pages_c=0
Routes=[]
sc="javascript"
st="text/css"

def _P_Help():
    sys.stderr.write(f"""LMFS 2021-2022 (C) PSML Compiler-Version: \033[92m{__version__}\033[0m
Usage: psml <files...> [targets...]

This is LMFS-PSML Compiler. It has a built-in staging server and can compile one psml file into many usable HTML pages.
It can reduce some of the development steps for you, so that you can complete the front-end development faster.
It is free(libre) software, open source under the GPL v2.0 license.

Options:
        -Werror-*           Make this warning an error for the psml compiler task
        -no-*               Causes the psml interpreter to ignore the command
        -keeponly=*         Only the page is output after compilation
        -script=*           Set the language of the script (default: javascript)
        -style=*            Set the format of style (default: text/css)
        -print=*            Print the results of the compilation
        -D*=*               Define variables in advance
        -c -compile         Only pretreatment psml code (same effect as '-mode=3')
        -q -quiet           Block output of any NOTE
        -o -output *        Compilation results are output to '*' ('*' is a directory name)
        -mode=1|2|3|4       Set the compilation mode
        -install            Install PSML to the directory where Python is located
        -online             Start psml_web
        -u -upgrade         Upgrade psml version
        -cv -check-version  Detect psml version update
        -man                Displays the PSML manual pages
        -h -help            Show help of psml
        -v -version         Show version of psml

Compile Mode:
             1: Normal compile mode
             2: Web Page Embedded Compiler Mode
             3: Run the preprocessor only (you can use the '-c' parameter directly)
             4: Compile without running the preprocessor

                                                                       \033[1m This compiler tool has a super \033[1;4;93mPlayability (XD)\033[0m

Thanks for using.
When you find bugs, you may report it to \033[92m{__author__}\033[0m\n""")

def change_script(new):
    global sc
    sc=new

def change_style(new):
    global st
    st=new

def initialize_server():
    global App, Routes
    import flask
    App=flask.Flask("PSML_DEV_SERVER")

def initialize_route(ROUTE: str, METHOD: list, ID: int, ARGS: list, CODE: str):
    global App, Routes
    initialize_server()
    Rc="@App.route(%s, methods=%s)\n"%(repr(ROUTE), str(METHOD))
    Rc+="def r%d(%s):\n"%(ID, ", ".join(ARGS))
    CODE=CODE.split("\n")
    for RCCC in CODE:
        Rc+="    "+RCCC+"\n"
    exec(Rc)
    Routes.append(Rc)

def initialize_page(branch, html="", head="<html", NewP_N=None, nobe=0):
    global pages_c,pages
    html="\n".join(html.split("\\n"))
    html=PS2NS(html)
    pages[branch]=head+">\n"+html+"</html>" if not nobe else html
    branch=NewP_N if NewP_N!=None else "Page"+str(pages_c)
    pages[branch]=""
    pages_c+=1

def endpage(branch, html="", head="", nobe=0):
    global pages
    html="\n".join(html.split("\\n"))
    html=PS2NS(html)
    pages[branch]=head+">\n"+html+"</html>" if not nobe else html

def run_server(host="localhost", port=8080):
    global App, Routes
    initialize_server()
    exec('\n\n'.join(Routes))
    App.run(host=host, port=port)

def del_page(page_name: str):
    global pages
    del pages[page_name]

def ERR(text):
    if text[-1]!="\n": text+="\n"
    sys.stderr.write(text)

def PS2NS(psml):
    psml="\n".join(psml.split("\\n"))
    psml="{".join(psml.split("&BBBBBBBBKKKUKNISSSs&"))
    psml="}".join(psml.split("&BBBBBBBBKKKUKNISSSe&"))
    psml="[".join(psml.split("&MMMMMMMMKKKKUKNISSSs&"))
    psml="]".join(psml.split("&MMMMMMMMKKKKUKNISSSe&"))
    psml="(".join(psml.split("&SSSSUKNEEEEs&"))
    psml=")".join(psml.split("&SSSSUKNEEEEe&"))
    psml=";".join(psml.split("&SSSSUKNEEEEp&"))
    psml=":".join(psml.split("&INNNISSSNNXTTTT&"))
    psml="-".join(psml.split("&HHHSSSPINNNUKN&"))
    psml="!~*".join(psml.split("&THSSENDDDD&"))
    psml="\n".join(psml.split("&BBBBBBBBKKKUKNISSSLKLNEUNXXXXX&"))
    psml="|".join(psml.split("&ANNNIDDDNTTTER&"))
    psml=" ".join(psml.split("&NOTHHHH&"))
    psml="#".join(psml.split("&ORDJJJJ&"))
    psml=">".join(psml.split("&VAROFFFFF&"))
    psml="<".join(psml.split("&VARONNNN&"))
    psml="$".join(psml.split("&VARUSEEEDDD&"))
    psml="/".join(psml.split("&CODDDSPPP&"))
    return psml

def NS2PS(NS, mode=1):
    if mode==1:
        i=NS
        i="&BBBBBBBBKKKUKNISSSs&".join(i.split("{"))
        i="&BBBBBBBBKKKUKNISSSe&".join(i.split("}"))
        i="&MMMMMMMMKKKKUKNISSSs&".join(i.split("["))
        i="&MMMMMMMMKKKKUKNISSSe&".join(i.split("]"))
        i="&SSSSUKNEEEEe&".join(i.split(")"))
        i="&SSSSUKNEEEEs&".join(i.split("("))
        i="&SSSSUKNEEEEp&".join(i.split(";"))
        i="&INNNISSSNNXTTTT&".join(i.split(":"))
        i="&HHHSSSPINNNUKN&".join(i.split("-"))
        i="&THSSENDDDD&".join(i.split("!~*"))
        i="&BBBBBBBBKKKUKNISSSLKLNEUNXXXXX&".join(i.split("\n"))
        i="&ANNNIDDDNTTTER&".join(i.split("|"))
        i="&NOTHHHH&".join(i.split(" "))
        i="&ORDJJJJ&".join(i.split("#"))
        i="&VAROFFFFF&".join(i.split(">"))
        i="&VARONNNN&".join(i.split("<"))
        i="&VARUSEEEDDD&".join(i.split("$"))
        i="&CODDDSPPP&".join(i.split("`"))
        NS=i
    if mode==2:
        codes=NS
        codes="&BBBBBBBBKKKUKNISSSs&".join(codes.split("\\{"))
        codes="&BBBBBBBBKKKUKNISSSe&".join(codes.split("\\}"))
        codes="&MMMMMMMMKKKKUKNISSSs&".join(codes.split("\\["))
        codes="&MMMMMMMMKKKKUKNISSSe&".join(codes.split("\\]"))
        codes="&SSSSUKNEEEEe&".join(codes.split("\\)"))
        codes="&SSSSUKNEEEEs&".join(codes.split("\\("))
        codes="&SSSSUKNEEEEp&".join(codes.split("\\;"))
        codes="&INNNISSSNNXTTTT&".join(codes.split("\\:"))
        codes="&HHHSSSPINNNUKN&".join(codes.split("\\-"))
        codes="&ANNNIDDDNTTTER&".join(codes.split("\\|"))
        codes="&NOTHHHH&".join(codes.split("\\ "))
        codes="&ORDJJJJ&".join(codes.split("\\#"))
        codes="&VAROFFFFF&".join(codes.split("\\>"))
        codes="&VARONNNN&".join(codes.split("\\<"))
        codes="&VARUSEEEDDD&".join(codes.split("\\$"))
        codes="&CODDDSPPP&".join(codes.split("\\`"))
        NS=codes
    return NS

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
def fcompile(path,string,mode=1,werr=[],no=[],quiet=False,keeponly="all",varpre={}):
    html=compile(string,mode=mode,werr=werr,no=no,quiet=quiet,varpre=varpre)
    if mode!=3:
        try:
            os.mkdir(path)
        except:pass
        if keeponly!="all":
            for i in keeponly:
                if i in list(html.keys()):
                    with open(os.path.join(path,i+".html"), "w") as f:
                        f.write(html[i])
                else:
                    sys.stderr.write(f"\033[91merror\033[0m: {repr(i)} isn't in pages\n")
        else:
            for i in html.keys():
                if i in ("Nothing", "INSERT"): continue
                else:
                    with open(os.path.join(path,i+".html"), "w") as f:
                        f.write(html[i])
    else:
        with open(path+".compiled.psml", "w") as f:
            f.write(html)
    return
def compile(string,mode=1,varpre={},nobe=0,werr=[],brc="index",brc_=1,no=[],quiet=False, al_=[]):
    global html, pages, pages_c, sc, st
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
    codes=codes.split("\n")
    idx=0
    del_=0
    codes_=codes.copy()
    alload=al_.copy()
    if mode!=4:
        for i in codes_:
            i=sub("\t","",i)
            i=sub(" ","",i)
            if(i==""):
                del codes[idx-del_]
                del_+=1
            idx+=1
        for i in range(len(codes)):
            codes[i]=codes[i].strip()
    cpd=0
    dels=0
    wh=0
    var=varpre
    used=[]
    for i in codes:
        if mode==4: break
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
        wh+=1
    dels=0
    wh=0
    cpd=0
    for obj in codes:
        if mode==4: break
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


    # This is the part that cannot be ignored, otherwise it will not compile properly!!!
    if mode==4:
        dels=0
        wh=0
        for obj in codes:
            if "".join("".join(obj.split(" ")).split("\t"))=="":
                try:
                    del codes[wh-dels+1]
                    dels+=1
                except Exception:pass
    # end


    codes="\n".join(codes)
    if mode!=4:
        tmps=findall(r"[[]([\w\W]*?)[]]",codes)
        codes="".join(codes)
        codes=NS2PS(codes, mode=2)
        for i in tmps:
            dfl=i
            i=NS2PS(i)
            codes=i.join(codes.split("["+dfl+"]"))
        tmps=findall(r"[`]([\w\W]*?)[`]",codes)
        codes="".join(codes)
        codes=NS2PS(codes, mode=2)
        for i in tmps:
            dfl=i
            i=NS2PS(i)
            codes=i.join(codes.split("`"+dfl+"`"))

    if mode!=4:
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
                    html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
SyntaxError: Invalid Syntax (Element only 1)"""
                    html+="</font></code>"

                else:
                    ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
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
            if mode==2:
                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
SyntaxError: Invalid Syntax (Type of element only one or zero)"""
                html+="</font></code>"

            else:
                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
SyntaxError: Invalid Syntax (Type of element only one or zero)""")
            return html
        if len(tpe)!=len(ele):
            if mode==2:
                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ReadyCompilingError: The length of types isn't equal to the length of elements"""
                html+="</font></code>"

            else:
                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ReadyCompilingError: The length of types isn't equal to the length of elements""")
            return html
        butn=("script", "style", "html", "java", "php", "doc", "var", "begin", "route", "command")
        special=("begin", "route")
        noarg=("command",)
        for count in ele:
            count=sub(" ",'',str(count))
            defcnt=count
            count=sub(";","",str(count))
            countf=count
            count="".join(count.split('\t')).lower()
            if count=="":
                if mode==2:
                    html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
SyntaxError: Invalid Syntax (Need an element)"""
                    html+="</font></code>"
                else:
                    ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
SyntaxError: Invalid Syntax (Need an element)""")
                return html
            if tpe[ele.index(defcnt)] not in ("/",""):
                if not count in butn:
                    if count=="doc":
                        pass
                    else:
                        html+=f"<{countf} type={repr(tpe[ele.index(defcnt)])}"
            else:
                if not count in butn:
                    html+=f"<{countf}"
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
                    if mode==1 and not quiet:
                        ERR(f"""PSML THREW \033[96;1mA NOTE\033[0m
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
                            tmp=var[VARFR]["value"].join(tmp.split(f"$<{VARFR}>"))
                            used.append(VARFR)
                        else:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
VariableError: {repr(VARFR)} was not declared in this scope"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
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
                            html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ELEMENT.DATAS.NAMEERROR: LENGTH OF DATA HAS SMALLER THAN 1"""
                            html+="</font></code>"

                        else:
                            ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
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
                    if count=="command":tmp="";break
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
                        if tpe[ele.index(defcnt)] not in ("", "/"):
                            _ST=st
                            st=tpe[ele.index(defcnt)]
                        style="\n".join(data)
                        dats.append(f"""<style type={repr(st)}>
{style}
</style>""")
                        if tpe[ele.index(defcnt)] not in ("", "/"):
                            st=_ST
                        break
                    elif count=='script':
                        if not "inner" in elem:
                            elem.append("inner")
                        if tpe[ele.index(defcnt)] not in ("", "/"):
                            _SC=sc
                            sc=tpe[ele.index(defcnt)]
                        script="\n".join(data)
                        dats.append(f"""<script language={repr(sc)}>
{script}
</script>""")
                        if tpe[ele.index(defcnt)] not in ("", "/"):
                            sc=_SC
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
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
PythonCodeExecError: Python threw a fatal error"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
PythonCodeExecError: Python threw a fatal error""")
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
                            VARN=VARN.strip(" ")
                            VARN=VARN.strip("\t")
                            VARN=ignore(VARN, "\t")
                            if("".join("".join(VARN.split(" ")).split("\t"))==""):
                                continue
                            VARFD=findall(r"\$\<(.*?)\>",VARV)
                            for VARFR in VARFD:
                                if(VARFR in list(var.keys())):
                                    VARV=var[VARFR]["value"].join(VARV.split(f"$<{VARFR}>"))
                                else:
                                    if mode==2:
                                        html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
VariableError: {repr(VARFR)} was not declared in this scope"""
                                        html+="</font></code>"

                                    else:
                                        ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
VariableError: \033[91;1;4m{repr(VARFR)}\033[0m was not declared in this scope""")
                                    return html
                            VARN=VARN.split(" ")
                            VTYPE="normal"
                            if(len(VARN)>1):
                                if(VARN[0]=="const"):
                                    VTYPE="const"
                                    del VARN[0]
                            VARN=" ".join(VARN)
                            if VARN not in var.keys():
                                var[VARN]={"value": VARV, "type": VTYPE}
                            else:
                                if var[VARN]["type"]=="normal":
                                    var[VARN]["value"]=VARV
                                else:
                                    if mode==2:
                                        html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
TypeError: {repr(VARN)} was a constant variable"""
                                        html+="</font></code>"

                                    else:
                                        ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
TypeError: \033[91;1;4m{repr(VARN)}\033[0m was a constant variable""")
                                    return html
                        break
                    elif count=="route":
                        if "server" in no:
                            if mode==1:
                                ERR(f"""PSML \033[90;1mIgnored this route\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
Ignored""")
                            break
                        else:
                            initialize_server()
                            args=tpe[ele.index(defcnt)]
                            argl=args.split("~")
                            argl=lclean(argl)
                            r_data=[]
                            r_argl=[]
                            if(len(argl)<2):
                                if mode==2:
                                    html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
RouteError: Cannot get the route"""
                                    html+="</font></code>"

                                else:
                                    ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
RouteError: Cannot get the route""")
                                return html
                            for psml in argl:
                                psml="\n".join(psml.split("\\n"))
                                psml=PS2NS(psml)
                                r_argl.append(psml)
                            for psml in data:
                                psml="\n".join(psml.split("\\n"))
                                psml=PS2NS(psml)
                                r_data.append(psml)
                            RC=""
                            for Rcode in r_data:
                                RC+=Rcode+"\n"
                            try:
                                initialize_route(r_argl[0], r_argl[1], routes, argl[2:],RC)
                            except:
                                traceback.print_exc()
                                if mode==2:
                                    html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
RouteError: Python threw a fatal error"""
                                    html+="</font></code>"

                                else:
                                    ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
RouteError: Python threw a fatal error""")
                                return html
                            routes+=1
                            break
                    html+=tmp
                if count.lower()=="command":
                    cmd=lclean(tpe[ele.index(defcnt)].split(" "))
                    if len(cmd)<1:
                        if mode==2:
                            html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
CommandError: No command got"""
                            html+="</font></code>"

                        else:
                            ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
CommandError: No command got""")
                            return html
                    if cmd[0].lower()=="run":
                        if len(cmd)<2:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Argument weren't enough"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Argument weren't enough""")
                            return html
                        if cmd[1].lower()=="server":
                            if "server" in no:
                                if mode==1:
                                    ERR(f"""PSML \033[90;1mIgnored this command\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
Ignored""")
                            elif len(cmd)<3:
                                initialize_server()
                                try:
                                    run_server()
                                except:
                                    traceback.print_exc()
                                    if mode==2:
                                        html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
RunServerError: Python threw a fatal error"""
                                        html+="</font></code>"

                                    else:
                                        ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
RunServerError: Python threw a fatal error""")
                                        return html
                            else:
                                initialize_server()
                                stat=cmd[2].split(":")
                                host=stat[0]
                                port=stat[1]
                                try:
                                    run_server(host, port)
                                except:
                                    traceback.print_exc()
                                    if mode==2:
                                        html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
RunServerError: Python threw a fatal error"""
                                        html+="</font></code>"

                                    else:
                                        ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
RunServerError: Python threw a fatal error""")
                                    return html
                        else:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: No such argument"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: No such argument""")
                            return html
                    elif cmd[0].lower()=="set":
                        if len(cmd)<3:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Arguments weren't enough (need 2)"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Arguments weren't enough (need 2)""")
                            return html
                        if cmd[1].lower()=="script":
                            change_script(cmd[2])
                        elif cmd[1].lower()=="style":
                            change_style(cmd[2])
                        if cmd[1].lower()=="nobegin":
                            if cmd[2].lower()=="yes":
                                nobe=1
                            else:
                                nobe=0
                        else:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: No such argument"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: No such argument""")
                            return html
                    elif cmd[0].lower()=="init":
                        if len(cmd)<2:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Arguments weren't enough"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Arguments weren't enough""")
                            return html
                        if cmd[1].lower()=="server":
                            if "server" in no:
                                if mode==1:
                                    ERR(f"""PSML \033[90;1mIgnored this command\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
Ignored""")
                            initialize_server()
                        else:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: No such argument"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: No such argument""")
                            return html
                    elif cmd[0].lower()=="del":
                        if len(cmd)<2:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Arguments weren't enough"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Arguments weren't enough""")
                        if cmd[1].lower()=="page":
                            if len(cmd)<3:
                                if mode==2:
                                    html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Arguments weren't enough"""
                                    html+="</font></code>"

                                else:
                                    ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Arguments weren't enough""")
                            if cmd[2] in pages.keys():
                                del_page(cmd[2])
                            else:
                                if mode==2:
                                    html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
DeletePageError: Nonexistent page <text color='purple'><b><u>'{cmd[2]}'</u></b></text>"""
                                    html+="</font></code>"

                                else:
                                    ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
DeletePageError: Nonexistent page \033[95;1;4m'{cmd[2]}'\033[0m""")
                        else:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: No such argument"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: No such argument""")
                            return html
                    elif cmd[0].lower()=="new":
                        if len(cmd)<2:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Arguments weren't enough"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Arguments weren't enough""")
                            return html
                        if cmd[1].lower()=="page":
                            OLD=branch
                            if len(cmd)<3:
                                branch="Page"+str(pages_c)
                            else:
                                branch=cmd[2]
                            initialize_page(OLD, html=html, head=head, NewP_N=branch, nobe=nobe)
                            html=""
                            head="" if nobe else "<html"
                            bran=1
                        else:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: No such argument"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: No such argument""")
                            return html
                    elif cmd[0].lower()=="end":
                        if bran==0:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
BranchError: No branch"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
BranchError: No branch""")
                            return html
                        if(len(cmd)<2):
                            endpage(branch, html=html, head=head, nobe=nobe)
                            branch="Nothing"
                            bran=0
                            html=""
                            head="" if nobe else "<html"
                        else:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: No argument"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: No argument""")
                            return html
                    elif cmd[0].lower()=="instext":
                        if len(cmd)<2:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Arguments weren't enough"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Arguments weren't enough""")
                            return html
                        else:
                            fn=' '.join(cmd[1:])
                            n=fn
                            if os.path.exists(fn):
                                try:
                                    _IN=getcont(fn)
                                except:
                                    if mode==2:
                                        html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
UnableToReadFile"""
                                        html+="</font></code>"

                                    else:
                                        ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
UnableToReadFile""")
                                    return html
                                html+=_IN
                            else:
                                if mode==2:
                                    html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
FileNotFoundError: {repr(fn)} no such file"""
                                    html+="</font></code>"

                                else:
                                    ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
FileNotFoundError: {repr(fn)} no such file""")
                                return html
                    elif cmd[0].lower()=="insert":
                        if len(cmd)<2:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Arguments weren't enough"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Arguments weren't enough""")
                            return html
                        else:
                            fn=' '.join(cmd[1:])
                            n=fn
                            if n in alload:
                                if "repeated-insertion" in werr:
                                    if mode==2:
                                        html+=f"""<code>PSML RAIED <font color="red">A FORCE ERROR</font><br>
MODULE <font color="green"><wh+1><font><br>
<font color="orange">   {i}</font><br>
<font color="red"> FileLoaderError: Duplicate reference to the same file '{n}'</font></code>"""
                                        return html
                                    else:
                                        ERR(f"""PSML THREW \033[91;1mA FORCE ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
FileLoaderError: Duplicate reference to the same file '{n}'""")
                                        return html
                                else:
                                    if mode!=2:
                                        ERR(f"""PSML THREW \033[95;1mA WARNING\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
FileLoaderWarning: Duplicate reference to the same file '{n}' [\033[95;1mrepeated-insertion\033[0m]""")
                            else:
                                alload.append(n)
                                if os.path.exists(fn):
                                    try:
                                        _IN=getcont(fn)
                                    except:
                                        if mode==2:
                                            html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
UnableToReadFile"""
                                            html+="</font></code>"

                                        else:
                                            ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
UnableToReadFile""")
                                        return html
                                    oh=html
                                    psml=_IN+";!~*\nCommand(End)"
                                    res=compile(psml, mode=mode, varpre=var, nobe=1, brc="INSERT", brc_=bran, werr=werr, no=no, al_=alload.copy())
                                    html=oh+res["INSERT"]
                                else:
                                    if mode==2:
                                        html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
FileNotFoundError: {repr(fn)} no such file"""
                                        html+="</font></code>"

                                    else:
                                        ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
FileNotFoundError: {repr(fn)} no such file""")
                                    return html
                    elif cmd[0].lower()=="title":
                        _TL=" ".join(cmd[1:])
                        html+="<title>"+_TL+"</title>"
                    elif cmd[0].lower()=="encoding":
                        html+=f"<meta charset={repr(' '.join(cmd[1:]))}>"
                    elif cmd[0].lower()=="goto":
                        if len(cmd)<3:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Arguments weren't enough (need 2)"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Arguments weren't enough (need 2)""")
                            return html
                        _SL=cmd[1]
                        _LNK=cmd[2:]
                        html+=f"<meta http-equiv='refresh' content='{_SL};url={' '.join(_LNK)}'>"
                    elif cmd[0].lower()=="describe":
                        if len(cmd)<3:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Arguments weren't enough (need 2)"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Arguments weren't enough (need 2)""")
                            return html
                        _NM=cmd[1]
                        _DES=" ".join(cmd[2:])
                        html+=f"<meta name={repr(_NM)} content={repr(_DES)}>"
                    elif cmd[0].lower()=="icon":
                        html+=f"<link rel='Shortcut Icon' type='image/x-icon' href={repr(' '.join(cmd[1:]))}>"
                    elif cmd[0].lower()=="css":
                        html+=f"<link rel='stylesheet' type='text/css' href={repr(' '.join(cmd[1:]))}>"
                    elif cmd[0].lower()=="script":
                        html+=f"<script language={repr(sc)} src={repr(' '.join(cmd[1:]))}></script>"
                    elif cmd[0].lower()=="php":
                        if len(cmd)<2:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: Arguments weren't enough"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: Arguments weren't enough""")
                            return html
                        else:
                            fn=' '.join(cmd[1:])
                            n=fn
                            if os.path.exists(fn):
                                try:
                                    _IN=getcont(fn)
                                except:
                                    if mode==2:
                                        html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
UnableToReadFile"""
                                        html+="</font></code>"

                                    else:
                                        ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
UnableToReadFile""")
                                    return html
                                html+=f"<?php\n{_IN}\n?>"
                            else:
                                if mode==2:
                                    html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
FileNotFoundError: {repr(fn)} no such file"""
                                    html+="</font></code>"

                                else:
                                    ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
FileNotFoundError: {repr(fn)} no such file""")
                                return html
                    elif cmd[0].lower()=="html":
                        if len(cmd)!=2:
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
ArgumentError: It just taking an argument"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
ArgumentError: It just taking an argument""")
                            return html
                        n=cmd[1]
                        if n not in("4.01","5","x"):
                            if mode==2:
                                html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
LookUpError: Unknown version {n}"""
                                html+="</font></code>"

                            else:
                                ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{w+1}\033[M 8h0m
    \033[93m{i}\033[0m
LookUpError: Unknown version {n}""")
                            return html
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
                        head=f"<!DOCTYPE {ins}>\n"+head
                    else:
                        if mode==2:
                            html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
CommandError: No such command"""
                            html+="</font></code>"
                        else:
                            ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
\033[93m{i}\033[0m
CommandError: No such command""")
                        return html
                    html+=tmp
                if "psml" in elem:
                    old_html=html
                    if countf not in butn:
                        if "end" in elem:
                            if dats[elem.index("end")].lower()=="true":
                                psml=dats[elem.index("psml")]
                                psml="\n".join(psml.split("\\n"))
                                psml=PS2NS(psml)
                                psml+=";!~*\nCommand(End)"
                                result=compile(psml,mode=mode,varpre=var,nobe=1,brc="INSERT",brc_=bran,werr=werr,no=no,al_=alload)
                                if(type(result)!=dict):
                                    if mode==2:
                                        html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
PsmlInsertThrewError"""
                                        html+="</font></code>"

                                    else:
                                        ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
PsmlInsertThrewError""")
                                    return html
                                else:
                                    old_html+=">"+result["INSERT"]
                                html=old_html
                            else:
                                #if dats[elem.index("end")].lower()=="true":
                                psml=dats[elem.index("psml")]
                                psml="\n".join(psml.split("\\n"))
                                psml=PS2NS(psml)
                                psml+=";!~*\nCommand(End)"
                                result=compile(psml,mode=mode,varpre=var,nobe=1,brc="INSERT",brc_=bran,werr=werr,no=no,al_=alload)
                                if(type(result)!=dict):
                                    if mode==2:
                                        html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
PsmlInsertThrewError"""
                                        html+="</font></code>"

                                    else:
                                        ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
PsmlInsertThrewError""")
                                    return html
                                else:
                                    old_html+=result["INSERT"]
                                html=old_html
                        else:
                            psml=dats[elem.index("psml")]
                            psml="\n".join(psml.split("\\n"))
                            psml=PS2NS(psml)
                            psml+=";!~*\nCommand(End)"
                            result=compile(psml,mode=mode,varpre=var,nobe=1,brc="INSERT",brc_=bran,no=no,werr=werr,al_=alload)
                            if(type(result)!=dict):
                                if mode==2:
                                    html=f"""<code>PSML THREW <font color="red">AN ERROR</font><br>
MODULE <font color="green">{wh+1}</font><br>
<font color="orange">&nbsp;&nbsp;&nbsp;&nbsp;{tohtml(i)}</font><br><font color="red">
PsmlInsertThrewError"""
                                    html+="</font></code>"

                                else:
                                    ERR(f"""PSML THREW \033[91;1mAN ERROR\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
PsmlInsertThrewError""")
                                return html
                            else:
                                old_html+=">"+result["INSERT"]
                            html=old_html
                    html=old_html
                if "inner" in elem:
                    if not count in butn and "psml" not in elem:
                        if "end" in elem:
                            if dats[elem.index("end")].lower()=="true":
                                html+=f">{dats[elem.index('inner')]}</{countf}>\n"
                            else:
                                html+=">%s"%dats[elem.index('inner')]
                        else:
                            html+=f">{dats[elem.index('inner')]}"
                    else:
                        if "end" in elem:
                            if dats[elem.index("end")].lower()=="true":
                                html+=f"{dats[elem.index('inner')]}</{countf}>\n"
                            else:
                                html+="%s"%dats[elem.index('inner')]
                        else:
                            html+=f"{dats[elem.index('inner')]}"
                else:
                    if not count in butn and "psml" not in elem:
                        if "end" in elem:
                            if dats[elem.index("end")].lower()=="true":
                                html+=f"></{countf}>\n"
                            else:
                                html+=">\n"
                        else:
                            html+=">\n"
                    else:
                        if "end" in elem:
                            if dats[elem.index("end")].lower()=="true":
                                html+=f"</{countf}>\n"
                if "br" in elem:
                    if dats[elem.index("br")].lower()=="true":
                        html+="<br/>\n"
                if "word-wrap" in elem:
                    if dats[elem.index("word-wrap")].lower()=="true":
                        html+="&BBBBBBBBKKKUKNISSSLKLNEUNXXXXX&"
            else:
                html+=">\n"
                if mode==1 and not quiet:
                    ERR(f"""PSML THREW \033[96;1mA NOTE\033[0m
MODULE \033[95;1m{wh+1}\033[0m
    \033[93m{i}\033[0m
Element.dats: No data get""")
    for i in var.keys():
        if(i not in used):
            if i=="psmlver": continue
            if "unused-variables" in werr:
                if mode==2:
                    html+=f"""<code>PSML RAIED <font color="red">A FORCE ERROR</font><br>
MODULE <font color="green">{i}<font><br>
<font color="orange">   i:&nbsp;{var[i]}</font><br>
<font color="red">VariablesError: {repr(i)} never use in this scope</font></code>"""
                    return html
                else:
                    ERR(f"""PSML THREW \033[91;1mA FORCE ERROR\033[0m
VARIABLE \033[95;1m{i}\033[0m
    \033[93m{i}: {var[i]}\033[0m
VariablesError: \033[91;1;4m{repr(i)}\033[0m never use in this scope""")
                    return html
            else:
                if(mode==1):
                    ERR(f"""PSML THREW \033[95;1mA WARNING\033[0m
VARIABLE \033[95;1m{i}\033[0m
    \033[93m{i}: {var[i]}\033[0m
VariablesWarning: \033[95;1;4m{repr(i)}\033[0m never use in this scope [\033[95;1munused-variables\033[0m]""")
    html="\n".join(html.split("\\n"))
    html=PS2NS(html)
    if bran:
        endpage(branch, html=html, head=head, nobe=nobe)
    return pages

def mkgz(f):
    import gzip
    with open(f, mode="rb") as _F:
        CONTENT=gzip.compress(_F.read())
    with open(f+".gz", mode="wb") as _F:
        _F.write(CONTENT)

def __install__():
    import os
    os.system("sh install.sh -quiet")
    return

def upgrade():
    import sys,os,shutil
    VER=_check_ver()
    VER=ignore(VER, "\n")
    if VER=="ERR!":
        ERR("\033[91mUpgrade fail\033[0m")
        return
    elif VER=="-": return
    else:
        wr_git=find_exe("git")
        if wr_git==[]:
            ERR("\033[91mfatal error\033[0m: git not found")
            return
        import os,shutil
        os.chdir("temp")
        os.system(wr_git[0]+" clone git@github.com:Lone-Air/PSML psml")
        try: os.chdir("psml")
        except:
            ERR("\033[91mfatal error\033[0m: unable to clone the repository of psml")
            return
        os.system("sh install.sh")
        os.chdir("..")
        while 1:
            try:
                shutil.rmtree("psml")
                break
            except:pass
        os.chdir("..")
        print("\033[92msuccess\033[0m: successfully upgraded psml")

def _check_ver():
    import os, shutil
    try: os.mkdir("temp")
    except: pass
    try: os.chdir("temp")
    except:
        ERR("\033[91mfatal error\033[0m: unable to switch working directory to 'temp/'")
        return "ERR"
    import urllib.request, ssl
    req=urllib.request.Request("https://raw.github.com/Lone-Air/PSML/master/VERSION", headers={"User-Agent": 'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)'})
    context=ssl._create_unverified_context()
    try:
        _VER=urllib.request.urlopen(req, context=context)
        VER=VER.read().decode("utf8")
        VER=ignore(VER, "\n")
        if VER==__version__:
            print("\033[92mIt's the latest version\033[0m")
            os.chdir("..")
            return "-"
        else:
            print("\033[93mNew Version: %s\033[0m"%VER)
            os.chdir("..")
            return VER
    except:
        print("\033[93mwarning\033[0m: Unable to get the version file from the raw.github.com, git will be used to get the repository to determine the version")
        wr_git=find_exe("git")
        if wr_git==[]:
            ERR("\033[91mfatal error\033[0m: git not found")
            os.chdir("..")
            return "ERR"
        os.system(wr_git[0]+" clone git@github.com:Lone-Air/PSML psml")
        try:
            os.chdir("psml")
        except:
            ERR("\033[91mfatal error\033[0m: unable to clone the repository of psml")
            os.chdir("..")
            return "ERR"
        VER=getcont("VERSION")
        VER=ignore(VER, "\n")
        if VER==__version__:
            print("\033[92mIt's the latest edition\033[0m")
            os.chdir("..")
            while 1:
                try:
                    shutil.rmtree("psml")
                    break
                except: pass
            os.chdir("..")
            return "-"
        else:
            print("\033[93mNew Version: %s\033[0m"%VER)
            os.chdir("..")
            while 1:
                try:
                    shutil.rmtree("psml")
                    break
                except:pass
            os.chdir("..")
            return VER

def getcont(file):
    with open(file) as f:
        Content=f.read()
    return Content

def showman():
    wr_man=find_exe("man")
    if wr_man==[]:
        ERR("\033[91mfatal error\033[0m: man not found")
        return
    os.system(wr_man[0]+" psml")

def find_exe(name):
    import os
    pth=os.getenv("PATH")
    pth=pth.split(":" if os.name=="posix" else ";")
    res=[]
    for _pth in pth:
        if os.path.exists(os.path.join(_pth,name if os.name=="posix" else name+".exe")):
            res.append(os.path.join(_pth, name if os.name=="posix" else name+".exe"))
    return res

def __online__():
    import os,sys
    wr_psmlweb=find_exe("psmlweb")
    if os.path.exists(os.path.join(os.path.dirname(__file__),"psml_web.py")):
        os.system("%s %s"%(sys.executable,(os.path.join(os.path.dirname(__file__),"psml_web.py"))))
    elif wr_psmlweb!=[]:
        os.system("%s %s"%(sys.executable,wr_psmlweb[0]))
    else:
        ERR("\033[91mfatal error\033[0m: psmlweb not found")
    return

compile.__doc__="""This is help on psml syntax

string: code of psml-page
    ------
    Syntax:

        Element(type|/){
                    property:value

                    /> Inner property
                    end:true/false
                    br:true/false
                    word-wrap:true/false
                    /> End of Inner property

                    /> Some special elements
                    (
                               If Element=audio|video:
                                   source:src
                    )
                    (
                               If Element=script|style|html|java|php|doc|...:
                                   <inner code direct change to html code>
                    )
                    (
                               If Element=var:
                                   <Name of Variable>: <Value of Variable>
                                   ...
                    )
                    (
                               If Element=Command:
                                   example: Command(Init Server)
                    )
                }|(If it isn't the last element, you can write '!~*' before '}'(You don't have to write, unless it's an element with no type or attribute))|
------
    Annotation:

        |Annotation Information|
        /> Annotation Information
------
    Escape Identifier:

        &BBBBBBBBKKKUKNISSSs&={
        &BBBBBBBBKKKUKNISSSe&=}
        &MMMMMMMMKKKKUKNISSSs&=[
        &MMMMMMMMKKKKUKNISSSe&=]
        &SSSSUKNEEEEs&=(
        &SSSSUKNEEEEe&=)
        &SSSSUKNEEEEp&=;
        &ANNNIDDDNTTTER&=Annotation_identifier
        &BBBBBBBBKKKUKNISSSLKLNEUNXXXXX&=\\n
        &THSSENDDDD&=!~*
        &HHHSSSPINNNUKN&=-
        &INNNISSSNNXTTTT&=:
        &NOTHHHH&=<space>
        &ORDJJJJ&=#
        &VARONNNN&=<
        &VAROFFFFF&=>
        &VARUSEEEDDD&=$
        &CODDDSPPP&=/
------
    Compile Programming language:

        html(Hypertext Markup Language)
"""

fcompile.__doc__=compile.__doc__

__install__.__doc__="""Execute the install.sh"""
__online__.__doc__="""Run a online compile web project server for psml"""

def _start():
    import sys,os
    w2err=[]
    realargs=[]
    noc=[]
    qit=False
    _M=1
    keeponly="all"
    save="NO!"
    OM=False
    c=0
    justp="all"
    justp_stat=0
    p_var={"psmlver": {"value": __version__, "type": "const"}}
    ffile=0
    for i in sys.argv:
        c+=1
        if c==1: continue
        if ffile:
            realargs.append(i)
            continue
        if OM:
            if save!="NO!":
                sys.stderr.write("\033[91merror\033[0m: You can only export to one directory\n")
            else:
                save=i
            OM=False
            continue
        if(i=="-h" or i=="--help" or i=="-help"):
            _P_Help()
            exit()
        elif(i=="--"):
            ffile=1
        elif(i=="-v" or i=="--version" or i=="-version"):
            sys.stderr.write("LMFS PSML Compiler %s\n"%__version__)
            exit()
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
                    elif temp[0]=="no":
                        noc.append("-".join(temp[1:]))
                    elif temp[0]=="compile":
                        _M=3
                    elif temp[0]=="quiet":
                        qit=True
                    elif temp[0]=="man":
                        showman()
                        exit(0)
                    elif temp[0]=="upgrade" or temp[0]=="u":
                        upgrade()
                        exit(0)
                    elif '-'.join(temp[:2])=="check-version" or temp[0]=="cv" :
                        _check_ver()
                        exit(0)
                    elif temp[0]=="online":
                        __online__()
                        exit(0)
                    elif temp[0]=="install":
                        if(os.path.realpath(os.path.dirname(__file__)).split(os.sep)[-1] not in ("psml", "psml-master")):
                            ERR("\033[91mfatal error\033[0m: must run it in the psml source directory")
                            exit()
                        __install__()
                        exit()
                    elif temp[0].split("=")[0]=="keeponly":
                        keeponly='='.join(temp[0].split("=")[1:])
                        keeponly=keeponly.replace(" ",  "")
                        keeponly=keeponly.replace("\t", "")
                        keeponly=keeponly.split(",")
                        if "all" in keeponly: keeponly="all"
                    elif temp[0].split("=")[0]=="print":
                        justp='='.join(temp[0].split("=")[1:])
                        justp=justp.replace(" ",  "")
                        justp=justp.replace("\t", "")
                        justp=justp.split(",")
                        if "all" in justp: justp="all"
                        justp_stat=1
                    elif temp[0].split("=")[0]=="script":
                        _sc='='.join(temp[0].split("=")[1:])
                        _sc=_sc.replace(" ",  "")
                        _sc=_sc.replace("\t", "")
                        change_script(_sc)
                    elif temp[0].split("=")[0]=="style":
                        _st='='.join(temp[0].split("=")[1:])
                        _st=_st.replace(" ",  "")
                        _st=_st.replace("\t", "")
                        change_style(_st)
                    elif temp[0][:1]=="D":
                        _INN=temp[0][1:]
                        _INN=_INN.split("=")
                        if(len(_INN)<2):
                            ERR("\033[91merror\033[0m: invaild variable syntax")
                            continue
                        n=_INN[0]
                        v="=".join(_INN[1:])
                        n=ignore(n, " ")
                        n=ignore(n, "\t")
                        if n=="":
                            ERR("\033[91merror\033[0m: variable name cannot be empty")
                            continue
                        if(n in p_var.keys()):
                            ERR("\033[91merror\033[0m: cannot change a constant that already exists")
                            continue
                        p_var[n]={"value": v, "type": "const"}
                    elif temp[0].split("=")[0]=="mode":
                        _M='='.join(temp[0].split("=")[1:])
                        _M=_M.replace(" ",  "")
                        _M=_M.replace("\t", "")
                        try:
                            _M=int(_M)
                            if _M<1 or _M>4: raise ValueError("Must be a number from 1 to 4")
                        except:
                            sys.stderr.write(f"\033[91mfatal error\033[0m: compile mode must be a number from 1 to 4")
                            exit()
                    elif temp[0]=="output":
                        OM=True
                    else:
                        sys.stderr.write(f"\033[91mfatal error\033[0m: unrecognized option (--): {repr(temp[0])}\n")
                        exit()
                elif i[0]=="-":
                    temp=list(i)
                    del temp[0]
                    temp="".join(temp)
                    temp=temp.split("-")
                    if temp[0]=="Werror":
                        w2err.append("-".join(temp[1:]))
                    elif temp[0]=="no":
                        noc.append("-".join(temp[1:]))
                    elif temp[0]=="quiet" or temp[0]=="q":
                        qit=True
                    elif temp[0]=="c":
                        _M=3
                    elif temp[0]=="man":
                        showman()
                        exit(0)
                    elif temp[0]=="upgrade" or temp[0]=="u":
                        upgrade()
                        exit(0)
                    elif '-'.join(temp[:2])=="check-version" or temp[0]=="cv":
                        _check_ver()
                        exit(0)
                    elif temp[0]=="online":
                        __online__()
                        exit(0)
                    elif temp[0]=="install":
                        if(os.path.realpath(os.path.dirname(__file__)).split(os.sep)[-1] not in ("psml", "psml-master")):
                            ERR("\033[91mfatal error\033[0m: must run it in the psml source directory")
                            exit()
                        __install__()
                        exit()
                    elif temp[0].split("=")[0]=="keeponly":
                        keeponly='='.join(temp[0].split("=")[1:])
                        keeponly=keeponly.replace(" ",  "")
                        keeponly=keeponly.replace("\t", "")
                        keeponly=keeponly.split(",")
                        if "all" in keeponly: keeponly="all"
                    elif temp[0].split("=")[0]=="print":
                        justp='='.join(temp[0].split("=")[1:])
                        justp=justp.replace(" ",  "")
                        justp=justp.replace("\t", "")
                        justp=justp.split(",")
                        if "all" in justp: justp="all"
                        justp_stat=1
                    elif temp[0].split("=")[0]=="script":
                        _sc='='.join(temp[0].split("=")[1:])
                        _sc=_sc.replace(" ",  "")
                        _sc=_sc.replace("\t", "")
                        change_script(_sc)
                    elif temp[0].split("=")[0]=="style":
                        _st='='.join(temp[0].split("=")[1:])
                        _st=_st.replace(" ",  "")
                        _st=_st.replace("\t", "")
                        change_style(_st)
                    elif temp[0][:1]=="D":
                        _INN=temp[0][1:]
                        _INN=_INN.split("=")
                        if(len(_INN)<2):
                            ERR("\033[91merror\033[0m: invaild variable syntax")
                            continue
                        n=_INN[0]
                        v="=".join(_INN[1:])
                        n=ignore(n, " ")
                        n=ignore(n, "\t")
                        if n=="":
                            ERR("\033[91merror\033[0m: variable name cannot be empty")
                            continue
                        if(n in p_var.keys()):
                            ERR("\033[91merror\033[0m: cannot change a constant that already exists")
                            continue
                        p_var[n]={"value": v, "type": "const"}
                    elif temp[0].split("=")[0]=="mode":
                        _M='='.join(temp[0].split("=")[1:])
                        _M=_M.replace(" ",  "")
                        _M=_M.replace("\t", "")
                        try:
                            _M=int(_M)
                            if _M<1 or _M>4: raise ValueError("Must be a number from 1 to 4")
                        except:
                            sys.stderr.write(f"\033[91mfatal error\033[0m: compile mode must be a number from 1 to 4")
                            exit()
                    elif temp[0]=="o" or temp[0]=="output":
                        OM=True
                    else:
                        sys.stderr.write(f"\033[91mfatal error\033[0m: unrecognized option (-): {repr(temp[0])}\n")
                        sys.exit()
                else:
                    realargs.append(i)
            else:
                if i[0]=="-":
                    temp=list(i)
                    del temp[0]
                    temp="".join(temp)
                    temp=temp.split("-")
                    if temp[0]=="c":
                        _M=3
                    elif temp[0]=="q":
                        qit=True
                    elif temp[0]=="o":
                        OM=True
                    elif temp[0]=="u":
                        upgrade()
                        exit(0)
                    else:
                        sys.stderr.write(f"\033[91mfatal error\033[0m: unrecognized option (-): {repr(temp[0])}\n")
                        sys.exit()
                else:
                    realargs.append(i)
        else:
            realargs.append(i)
    sys.argv=realargs.copy()
    if(sys.argv==[]):
        code=""
        while(1):
            try:
                code+=input("PSML> ")+"\n"
            except EOFError:
                print("\r",end="",flush=1)
                if save=="NO!":
                    PG=compile(code,werr=w2err,mode=_M,no=noc,quiet=qit,varpre=p_var)
                    if keeponly!="all":
                        NPG={}
                        for P in keeponly:
                            if P in PG:
                                NPG[P]=PG[P]
                            else:
                                sys.stderr.write(f"\033[91merror\033[0m: {repr(P)} isn't in the pages\n")
                        PG=NPG.copy()
                    if not justp_stat:
                        sys.stdout.write(str(PG)+"\n")
                    else:
                        if justp=="all":
                            for i in PG.keys():
                                print(PG[i])
                        else:
                            for i in justp:
                                if i in PG.keys():
                                    print(PG[i])
                                else:
                                    ERR("\033[91mfatal error\033[0m: '%s' not in branch list"%i)
                    sys.exit()
                else:
                    try:
                        fcompile(save,code,mode=_M,no=noc,quiet=qit,keeponly=keeponly)
                    except Exception:
                        traceback.print_exc()
                        sys.exit("\033[91mfatal error\033[0m: compile failed with error")
                    except KeyboardInterrupt:
                        sys.exit("\033[91mfatal error\033[0m: compile ** break")
                sys.exit()
            except:
                print("\r",end="",flush=1)
                sys.exit()
    if save=="NO!":
        for PSMLC in sys.argv:
            if PSMLC==__file__: continue
            if os.path.exists(PSMLC):
                try:
                    try:
                        with open(os.path.join(os.getcwd(),PSMLC),"rt") as F:
                            code=F.read()
                    except Exception:
                        sys.stderr.write("\033[91mfatal error\033[0m: cannot read '%s'\n"%PSMLC)
                        sys.exit()
                    try:
                        ret=compile(code, werr=w2err,mode=_M,no=noc,quiet=qit,varpre=p_var)
                        if ret!=None:
                            if keeponly!="all" and _M!=3:
                                if type(ret)!=dict:
                                    sys.stdout.write(ret+"\n")
                                else:
                                    Nret={}
                                    for P in keeponly:
                                        if P in ret:
                                            Nret[P]=ret[P]
                                        else:
                                            sys.stderr.write(f"\033[91merror\033[0m: {repr(P)} isn't in the pages\n")
                                    ret=Nret.copy()
                                    if not justp_stat:
                                        sys.stdout.write(str(ret)+"\n")
                                    else:
                                        if justp=="all":
                                            for i in ret.keys():
                                                print(ret[i])
                                        else:
                                            for i in justp:
                                                if i in ret.keys():
                                                    print(ret[i])
                                                else:
                                                    ERR("\033[91mfatal error\033[0m: '%s' not in branch list"%i)
                            else:
                                if type(ret)==dict:
                                    if not justp_stat:
                                        sys.stdout.write(str(ret)+"\n")
                                    else:
                                        if justp=="all":
                                            for i in ret.keys():
                                                print(ret[i])
                                        else:
                                            for i in justp:
                                                if i in ret.keys():
                                                    print(ret[i])
                                                else:
                                                    ERR("\033[91mfatal error\033[0m: '%s' not in branch list"%i)
                                else:
                                    sys.stdout.write(ret+"\n")
                    except Exception:
                        traceback.print_exc()
                        sys.stderr.write("\033[91mfatal error\033[0m: an error occurred while compiling\n")
                        sys.exit()
                except (KeyboardInterrupt,EOFError):
                    sys.stderr.write("\033[91mfatal error\033[0m: compile ** break\n")
                    sys.exit()
            else:
                sys.stderr.write("\033[91mfatal error\033[0m: no such file or directory '%s'\n"%PSMLC)
                sys.exit()
    else:
        for PSMLC in sys.argv:
            if PSMLC==__file__: continue
            if os.path.exists(PSMLC):
                try:
                    try:
                        with open(os.path.join(os.getcwd(),PSMLC),"rt") as F:
                            code=F.read()
                    except Exception:
                        sys.stderr.write("\033[91mfatal error\033[0m: cannot read '%s'"%(PSMLC))
                        sys.exit()
                    try:
                        fcompile(save,code,mode=_M,no=noc,quiet=qit,keeponly=keeponly,varpre=p_var)
                    except Exception:
                        traceback.print_exc()
                        sys.stderr.write("\033[91mfatal error\033[0m: an error occurred while compiling\n")
                        sys.exit()
                except (KeyboardInterrupt,EOFError):
                    sys.stderr.write("\033[91mfatal error\033[0m: compile ** break\n")
                    sys.exit()
            else:
                sys.stderr.write("\033[91mfatal error\033[0m: no such file or directory '%s'\n"%PSMLC)
                sys.exit()

if __name__=="__main__":
    try:
        from rlcompleter import *
        import readline
    except:
        print("\033[95;1mWarning\033[0m: Your python unsupport GNU Readline")
    _start()
    exit()
