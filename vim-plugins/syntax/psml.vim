" Vim syntax file
" Language:	psml
" Maintainer:   Laman28 <Lone_air_Use@outlook.com>
" Last Change:	2021 Nov 28
" Credits:  Laman28 <Lone_air_Use@outlook.com>
if exists("b:current_syntax")
    finish
endif

let s:cpo_save=&cpo
set cpo&vim

if exists("psml_no_doctest_highlight")
    let psml_no_doctest_highlight=1
endif

"if exists("psml_highlight_all")
"  if exists("psml_no_builtin_highlight")
"    unlet psml_no_builtin_highlight
"  endif
"  if exists("psml_no_doctest_code_highlight")
"    unlet psml_no_doctest_code_highlight
"  endif
"  if exists("psml_no_doctest_highlight")
"    unlet psml_no_doctest_highlight
"  endif
"  if exists("psml_no_exception_highlight")
"    unlet psml_no_exception_highlight
"  endif
"  if exists("psml_no_number_highlight")
"    unlet psml_no_number_highlight
"  endif
"  let psml_space_error_highlight = 1
"endif

syn keyword psmlBool true false
syn keyword psmlStatment php doc html java title style script
syn keyword psmlInnerELEM br end word-wrap
syn keyword psmlSYN inner var
" syn keyword psmlSymbols &Bs& &Be& &Ms& &Me& &Se& &Ss& &sp& &is& &in& &or& &no& &ord& &voff& &von& &vuse& $< >

syn region psmlSYM start=/&/ end=/&/ skip=/\\&/
syn region psmlSTR start=/\[/ end=/\]/ skip=/\\\]/
syn region psmlELEMENT start=/(.*?):/ end=/:/ skip=/\\:/
syn region psmlATT start=/|/ end=/|/ skip=/\\|a/
syn region psmlPCOM start=/#/ end=/\n/ skip=/\\>/
syn region psmlPVAR start=/\$</ end=/>/ 
syn region psmlEType start=/(/ end=/)/
syn region psmlLATT start=/\/>/ end=/\n/
" syn match psmlPCOMARGS '[<]([\w\W]*?)[>]' contained

hi psmlStatment guifg=#ff3838
hi psmlBool guifg=#4870e0
hi psmlInnerELEM guifg=#3ae077
hi psmlSYN guifg=#b8822c
hi psmlSYM guifg=#ac27b8
hi psmlSTR guifg=#778500
hi psmlELEMENT guifg=#1fcc2d
hi psmlATT guifg=#474747
hi psmlLATT guifg=#474747
hi psmlPCOM guifg=#37bf84
hi psmlPVAR guifg=#00ffff
hi psmlEType guifg=#2a87a3
"hi psmlPCOMARGS guifg=#aebf28

