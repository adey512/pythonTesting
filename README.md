README:
•	Framework used – Python, Selenium and Pytest Framework
•	Prerequisites prior to running test-

1.	Check python is installed in cmd using:
C:\Users\Ankita>python --version
Python 3.11.4
If not install python in your system and add the path to your system environment variables
2.	Install selenium for python using:
C:\Users\Ankita>pip install selenium
C:\Users\Ankita>pip show selenium
Name: selenium
Version: 4.19.0
3.	Chrome driver version: 123 
Download link: https://storage.googleapis.com/chrome-for-testing-public/123.0.6312.122/win64/chromedriver-win64.zip
(used chrome, but code can be changed to incorporate different browser such as firebox, Edge etc.)
4.	Install pytest : C:\Users\Ankita>pip install pytest
C:\Users\Ankita>pytest --version
pytest 8.1.1
5.	Install pytest-html:  C:\Users\Ankita>pip install pytest-html

•	Once above packages are installed 
Run pytest using:  py.test --html=report.html

•	Code in GitHub Path: https://github.com/adey512/pythonTesting. For the below test cases please refer to test file test_T001.py, test_T002.py, test_T003.py, test_T004.py, test_T005.py, test_T006.py, test_T007.py and there are sub test cases under the files as mentioned in the document

•	View reports in report.html file

