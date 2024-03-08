# Docker testing
Vasicek cap priced on Docker. 
Packages are not installed on the local machine and the code runs at least once and
asks the user for some input parameters to compute the calculations.

### Docker general tips...
- When asking for user input remember to include -i, -t --> docker run -i -t <image_name> so 
that it does not throw an error.
- If you have issues with ports not being "available" --> docker run -p 808**1**:808**0** fastapitutorial
- When you need to run on a specific port you need to specify it in the Dockerfile:
  - CMD ["uvicorn","app.main:app",**_"--host","0.0.0.0","--port","80"_**]
  but also when you run the docker --> docker run **_-p 80:80_** fastapitutorial

### Inside the container
##### ls
app  requirements.txt
#### cs ..
/bin/sh: 2: cs: not found
#### cd ..
#### ls
bin  boot  code  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var


