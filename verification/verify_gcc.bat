set dir=%~dp0

type %~dpnx1 | %dir%parse_gcc.py env.txt > issues.txt
type issues.txt | %dir%sortby.py | %dir%create_report.py env.txt > report.html

if [%CI_SERVER%] == [] (
    start report.html
) else (
    %dir%send_email.py report.html issues.txt
)
