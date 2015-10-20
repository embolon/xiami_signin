This project is for xiami automatic signin using rainmeter interface

requirement python3x, python requests, rainmeter

The main contributor is embolon@gmail.com

Usage:
	setup python3x, rainmeter, install python requests module

	change xiami.bat
	'''
	set prompt=[%computername%] $d$s$t$_$p$_$_$+$g
	@cd %~dp0
	python xiami.py your_username your_password
	pause
	'''
	your_username => your own username
	your_password => your own password
	
	copy the directory to your rainmeter skin directory