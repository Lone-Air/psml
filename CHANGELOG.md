#  (2022-02-12)

fix: Fixed case where quiet compilation mode does not work in fcompile

#  (2022-02-12)

feat: Preprocessing commands and single-line comments no longer require top-cell writing

#  (2022-02-11)

feat: Added '-quiet' compilation parameter to prevent all NOTE output during compilation

#  (2022-02-11)

fix: Fix the problem that the front-end command directly compiles the file and reports an error, and fix the element attribute combiner

#  (2022-02-09)

fix: Fix case where 'psml' internal property returns are combined with 'Command(End)'

#  (2022-02-09)

fix: Fix werror cannot be used in fcompile
feat: Added -no-*, which can be used to ignore a Command-formatted code, example: psml pages.psml -no-server

#  (2022-02-05)

fix: Correct an incorrect symbol in the code

#  (2022-01-18)

fix: Fix terminal input code compilation error

#  (2022-01-18)

feat: New -c --compile option, you can pretreatment the psml then code save as in xxx.compiled.psml or put the code on screen

