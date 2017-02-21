#' % Installing Python 3.X on mac
#' % CyBu
#' % Jan 31, 2017

#+ echo= False
import pweave
# pweave.publish('/Users/cybu/Desktop/courses/Installing_Python/IDE.py')

#' -----------------------------------------------------------------------
#' # download

#' [download link for python 3](https://www.python.org/downloads/)

#' It will install the standard IDE which is one on the simplest form of IDE,
#' if you don't want to go through emacs (aquamacs is pretty good on mac
#' though), pyCharm and the likes.

#' -----------------------------------------------------------------------
#' # modules

#' The version above comes standard with a few pre-installed modules.
#' Typing: 
#+ evaluate= False
help()

#' will give you:

#+ evaluate= False, results= 'verbatim'

Welcome to Python 3.5's help utility!

If this is your first time using Python, you should definitely check
out
the tutorial on the Internet at http://docs.python.org/3.5/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility
and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose
name
or summary contain a given string such as "spam", type "modules spam".

#' Then type:
#+ evaluate= False, results= 'verbatim'
help> modules
Please wait a moment while I gather a list of all available modules...

#' Amongst the myriad of package you will see, you should see that
#' you have at least:
#'
#+ evaluate=False, results= 'verbatim'
matplotlib, pandas, numpy, scipy.

#' -----------------------------------------------------------------------
#' # adding more modules
#' Since we are not using anaconda, we'll need to customize our system to
#' be able to install and update modules.  
#' The prefered way for computer people is generally to use the pip.
#' However Python 2.7 comes pre-installed in mac because mac itself uses
#' python.  But you do not want to interfere with what is already installed
#' as it may affect native dependencies. For that reason the pre-installed
#' Python 2.7 doesnot have a pip.
#' We'll need to install pip for python 3.x.  This can be done by running a
#' special python program that will do it for us.
#'
#' To install pip:  
#' > - securely download [get-pip.py](https://bootstrap.pypa.io/get-pip.py)  
#' > - open a terminal window  
#' > - run the following in the terminal window:  
#+ evaluate=False, results= 'verbatim'
python3 get-pip.py

#' This will install pip specifically for python 3.x.
#'
#' -----------------------------------------------------------------------
#' From now on, every time you will need to upgrade a module or make
#' a new module installation, you will do the same:
#' > - open a terminal window
#' > - for new install
#+ evaluate=False, results= 'verbatim'
pip install <name_of_the_package>

#' > - for update install:
#+ evaluate=False, results= 'verbatim'
pip install <name_of_the_package> --upgrade



