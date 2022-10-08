*** Settings ***
Resource    keywords.resource
Suite Setup    Start
Suite Teardown    Run Keyword And Ignore Error    Close

*** Test Cases ***
Registering default user
    Register User With Default Creds


Checking default user board
    Login With Default Creds


Trying to Register the same user
    Register User With Default Creds
    Catch Same User Alert    


Trying to login with wrong creds
    Login With Wrong Creds


Registering custom user 
    Register User With Custom Creds    Juli@    1111    Gulia    09878909    Julia


Checking custom user board
    Login With Custom Creds    Juli@    1111    Gulia    09878909    Julia


Trying to Register the same custom user
    Register User With Custom Creds    Juli@    1111    Gulia    09878909    Julia
    Catch Same User Alert


Trying to login with custom wrong creds
    Login With Custom Wrong Creds    Juli@    2222
