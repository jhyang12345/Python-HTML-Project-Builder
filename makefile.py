import sys, os

#사용법 python makefile.py --directory-name

#print('Number of arguments: ' + str(len(sys.argv)) + ' arguments.')
#print('Argument List: ' + str(sys.argv))


filename = sys.argv[1]

print("Making HTML project folder... with name " + filename)

cwd = os.getcwd()
directory = cwd + "/" + filename

if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir(directory)

os.makedirs("./js")
os.makedirs("./css")

indextext = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <script src="js/main.js" ></script>
    <link href="css/main.css" rel="stylesheet" type="text/css" />

  </head>
  <body>

  </body>
</html>
"""

jstext = """
document.addEventListener("DOMContentLoaded", function(event) {
  console.log("DOM fully loaded and parsed");

});

"""

with open("index.html", "w") as f:
    f.write(indextext)

os.chdir("./js")
with open("main.js", "w") as f:
    f.write(jstext)

os.chdir("..")
os.chdir("./css")

with open("main.css", "w") as f:
    f.write("")
