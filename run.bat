
    
@echo off

CALL env\Scripts\activate

set FLASK_APP=app.py
set FLASK_DEBUG=1
python -m flask run