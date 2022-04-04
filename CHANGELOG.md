## 1.2.3 - 2022-04-04

### Fixed

* Fixed dependences

## 1.2.2 - 2022-04-04

### Fixed

* Fixed a error in Help Document

## 1.2.1 - 2022-04-04

### Fixed

* Repaired: -upgrade

## 1.2.0 - 2022-04-04

### Changed

* Switch to the new official Python installation
* Use install.sh instead of install.py

### Removed

* Removed cmd-line argument: -uninstall

## 1.1.2 - 2022-04-03

### Fixed

* Fix ArgumentError reported by psml insert attribute

## 1.1.1 - 2022-03-23

### Fixed

* Fix Update Check Unavailable Problem

## 1.1 - 2022-03-23

### Changed

* Non-internal element names will no longer be all lowercase

## 1.0.3 - 2022-03-10

### Feature

* Added insert plain text file command: instext

## 1.0.2 - 2022-03-09

### Changed

* Change all hard coding to prevent repetition of English words

## 1.0.1 - 2022-03-09

### Fixed

* Fix alload unable to recurse

## 1.0 - 2022-03-08

### Removed

* Preprocessing command (command element instead)

### Refactored

* The psml.py is no longer copied directly to psml as the psml compiler command (the same applies to psmlweb)

## 0.8.2 - 2022-03-08

### Changed

* Remove comments added by preprocessing command

## 0.8.1.7 - 2022-03-06

### Feature

* Uninstall and install additional tips, uninstall more secure

## 0.8.1.6 - 2022-03-06

### Changed

* The installation now recognizes the psml-master directory

## 0.8.1.5 - 2022-03-06

### Fixed

* Fixed a fatal error in psml.py

## 0.8.1.4 - 2022-03-06

### Fixed

* Fixed a fatal error in psml.py

## 0.8.1.3 - 2022-03-06

### Fixed

* Fixed a fatal error in psml.py

## 0.8.1.2 - 2022-03-06

### Fixed

* Fixed a fatal error in psml.py

## 0.8.1.1 - 2022-03-06

### Fixed

* Fixed a fatal error in psml.py

## 0.8.1 - 2022-03-06

### Feature

* Added '-uninstall' to uninstall psml

### Fixed

* Fixed some text details

## 0.8 - 2022-03-06

### Feature

* Added a variable type that cannot be changed (syntax: const variable_name: value)
* Added -D*=* to predefine a const variable
* All options after the '--' option are treated as file names
* Add the function of style selection format (use -style=*, default is 'text/css')

### Changed

* Run the psml program directly, and move the front-end parameter processing to the _start function

## 0.7.5 - 2022-03-05

### Feature

* Added the set nobegin command, which is used to close the beginning and end of the compilation output page.

### Changed

* Remove the use of ':=' syntax for compatibility with older versions of python

## 0.7.4 - 2022-03-05

### Feature

* Added '-print=*' option
* Add the function of script selection language (the foreground can use -script = * to set (* is the language name))

### Fixed

* Fix install does not recognize directories

## 0.7.3.3 - 2022-03-04

### Fixed

* Fixed a fatal error

## 0.7.3.2 - 2022-03-04

### Fixed

* Fixed __online__ function

## 0.7.3.1 - 2022-03-04

### Fixed

* fixed a fatal error

## 0.7.3 - 2022-03-03

### Feature

* Added online option to launch psml web editor

### Fixed

* Fix psml compiler referencing itself

## 0.7.2 - 2022-03-03

### Feature

* Added manual page for psml for reference

## 0.7.1.1 - 2022-02-28

### Fixed

* Fix for not prompting for GNU ReadLine

## 0.7.1 - 2022-02-28

### Feature

* '-upgrade' to upgrade psml
* '-check-version' to check psml version

## 0.7.1d - 2022-02-28

### Fixed

* Fix some bugs

## 0.7 1c - 2022-02-28

### Fixed

* Fix some bugs

## 0.7.1b - 2022-02-28

### Fixed

* Fix fatal bugs

## 0.7.1a - 2022-02-28

### Feature

* Added update psml function and detection version update function

## 0.7 - 2022-02-26

### Changed

* Server function, paging function, delete page function, conversion between PSML string and normal string, and backslash escape character are all divided into separate functions as the API interface provided by the PSML compiler.

## 0.6.1.6 - 2022-02-26

### Fixed

* Fix comment syntax in strings being parsed.

## 0.6.1.5 - 2022-02-25

### Changed

* Have better help information and error information.

## 0.6.1.4 - 2022-02-24

### Changed

* Have better help information.
* The description in the README.md is copied into ABOUT.

## 0.6.1.3 - 2022-02-22

### Feature

* Added an feature (XD).

### Refactored

* The format of CHANGELOG.md is improved.
* The psml compiler help information now exists as a separate function.

#  (2022-02-21)

fix: Fix a code that will throws an error.
changed: Change all raised in the psml error text to throws.

#  (2022-02-21)

fix: Fix element error generation problem in '4' mode.

#  (2022-02-21)

fix: Fix the problem that the preprocessing mode cannot run normally; fix the problem that the command line reference compiler reports an error.
feat: Added '-mode' option to set the compilation mode for foreground compilation; added skip preprocessor operation mode (mode id: 4).
changed: Modify the '-c' parameter processing logic.
removed: The rest of the criteria for not using the 'comp' variable as a preprocessing mode.

#  (2022-02-20)

fix: Fix not truncating loop when route is ignored.

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

