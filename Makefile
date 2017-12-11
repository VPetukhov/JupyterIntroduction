default: data-science-handbook

data-science-handbook:
	test ! -f ./PythonDataScienceHandbook || git clone https://github.com/jakevdp/PythonDataScienceHandbook.git
