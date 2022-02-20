#  (2022-02-20)

fix: Correct an error in help.

#  (2022-02-20)

fix: Fix the problem of using 'route' without importing 'flask' and reporting an error.
feat: Internal elements are no longer case-limited; 'init' commands are added to initialize some functions in advance (example: command(init server)); The 'fcompile' in 'keeponly' mode outputs a 'error' if it encounters a page that does not exist, but it is not a 'fatal error', so it does not exit the compiler; New 'del' command to remove duplicate pages when compiling multiple psml files at once (example: command(del page TEST)).
changed: The psml compiler does not start with 'psml <input> {output}' as a directed output, replaced by the '-o' option (example: psml a.psml -o b); the psml compiler is no longer restricted to compiling a single file at a time, it can compile multiple files at a time, and it can output HTML at the same time.

#  (2022-02-19)

fix: Fix a line of code on the web side that may cause Python to report an error.
feat: Add the '-keeponly=*' compilation parameter to control the pages that are reserved only after compilation is completed ('all' means all pages are reserved, use ',' split page name)
changed: The server function component is no longer loaded when psml is started, and the server function is initialized when the server function is called (refer to the function: initialize_server(/)).

#  (2022-02-12)

fix: Fixed case where quiet compilation mode does not work in fcompile.

#  (2022-02-12)

feat: Preprocessing commands and single-line comments no longer require top-cell writing.

#  (2022-02-11)

feat: Added '-quiet' compilation parameter to prevent all NOTE output during compilation.

#  (2022-02-11)

fix: Fix the problem that the front-end command directly compiles the file and reports an error, and fix the element attribute combiner.

#  (2022-02-09)

fix: Fix case where 'psml' internal property returns are combined with 'Command(End)'.

#  (2022-02-09)

fix: Fix werror cannot be used in fcompile.
feat: Added -no-*, which can be used to ignore a Command-formatted code, example: psml pages.psml -no-server.

#  (2022-02-05)

fix: Correct an incorrect symbol in the code.

#  (2022-01-18)

fix: Fix terminal input code compilation error.

#  (2022-01-18)

feat: New -c --compile option, you can pretreatment the psml then code save as in xxx.compiled.psml or put the code on screen.

