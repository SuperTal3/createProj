if exist %1% goto fail
@python C:\createProj\createProj.py %1%
@cd C:\Users\talke\source\repos
@mkdir .\%1%
@cd .\%1%
if %2%=="DNCWebsite" goto dotnetweb  
if %2%=="Python" goto pythonProj

:localGit
@git config --global user.email "yourEmail@emailProvider.com"
@git config --global user.name "SuperTal3"
@git init
@git add README.md
@git commit -m "Initial Commit"
@git remote add origin https://github.com/SuperTal3/%1%.git
@git push -u origin master
@code C:\Users\talke\source\repos\%1%

@echo "Git project created :) Happy coding!!"



:dotnetweb
@dotnet new webapp -lang C#
@dotnet restore
goto localGit
:pythonProj
@echo "#! python3" > main.py
goto localGit
:fail
@echo "You failed to specify a new project name"
@dir