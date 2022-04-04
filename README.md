# PSML - Python server markup language

This is LMFS-PSML Compiler. It has a built-in staging server and can compile one psml file into many usable HTML pages.
It can reduce some of the development steps for you, so that you can complete the front-end development faster.
It is free(libre) software, open source under the GPL v2.0 license.

---

1. How to install:<code>$ sudo python3 setup.py install</code>

---

2. How to compile:<br>
<code>psml &lt;file&gt; {targets...}</code><br>
Example: <br>
<code>
$ cat &gt; test.psml &lt;&lt; "EOF"<br>
> text{<br>
> &nbsp;&nbsp;&nbsp;&nbsp;inner: Hello-World! <br>
> }<br>
> command(end)<br>
> EOF<br>
$ psml test.psml -o TEST<br>
$ ls TEST<br>
index.html
</code><br>

---

3. Feedback: Lone_air_Use@outlook.com
