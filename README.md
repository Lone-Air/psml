# PSML - Python server markup language
---
0.4.4: <br>
1. Added compiler parameter -Werror-\*: Causes the PSML compiler to think this warning should be an error
2. The psml compiler deliberately prevents the 'insert' command from repeatedly inserting the same file, causing an endless loop.
---
New: <br>
1. Added the 'route' method, which can be used to access the target by the built-in server
2. New 'Command' option, an element with no parameters and a second special element to perform some built-in services
3. New py 'method' to execute code at compile time or define some function
---
1. How to install: <code>python install.py</code>
---
2. How to compile:<br>
<code>psml &lt;file&gt;</code><br>
or<br>
<code>psml &lt;file&gt; &lt;output&gt;</code>
---
3. Feedback: 2991600190@qq.com
