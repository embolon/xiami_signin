This project is for xiami automatic signin using python and rainmeter interface
Requirement: python3x, python requests, rainmeter

该脚本利用python和rainmeter登陆虾米签到
需要 python3x，python库requests，和rainmeter

Usage:
	
	i. setup python3x, rainmeter, install python requests module
	安装python3x，rainmeter，和python库requests

	ii. change xiami.bat
	'''
	set prompt=[%computername%] $d$s$t$_$p$_$_$+$g
	@cd %~dp0
	python xiami.py your_username your_password
	pause
	'''
	your_username => your own username
	your_password => your own password
	把xiami.bat脚本里面的xiami.py后面的参数改为正确的登录邮箱和密码
	如果python脚本不能正确运行请先查看python environment设置是否正确
	
	iii. copy the directory to your rainmeter skin directory
	把该目录复制到rainmeter的皮肤目录内，然后按rainmeter运行即可     
