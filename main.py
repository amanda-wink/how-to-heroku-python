from flask import Flask

pagehtml = """
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>The Schooner</title>
  <meta name="description" content="The Schooner">
  <meta name="author" content="Kristofer">

<style>
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  line-height: 1.6;
  color: #303030;
  max-width: 40rem;
  padding: 2rem;
  margin: auto;
  background: #FEF4FF;
}
img {
  max-width: 100%;
}
a {
  color: #2ECC40;
}
h1, h2, strong {
  color: #303030;
}
</style>
</head>

<body>
  <h2>The Schooner</h2>
  <p><img src="http://www.marinemodelartist.com/Mary_Taylor/Mary_Taylor_files/shapeimage_4.png"</p>
<p>This is a schooner.</p>

<p>
A schooner (/ˈskuːnər/) is a type of sailing vessel defined by its 
rig: fore-and-aft rigged on all of 2 or more masts and, in the case 
of a 2 masted schooner, the foremast generally being shorter than 
the mainmast. A common variant, the topsail schooner also has a 
square topsail on the foremast, to which may be added a topgallant 
and other square sails, but not a fore course, as that would 
make the vessel a brigantine. Many schooners are gaff-rigged, but 
other examples include Bermuda rig and the staysail schooner.
</p>
<h2>The Origins of the Type and the Name</h2>
<p>
The origins of schooner rigged vessels is obscure, but there is 
good evidence of them from the early 17th century in paintings by 
Dutch marine artists. The name "schooner" first appeared in eastern 
North America in the early 1700s. The name may be related to a 
Scots language word meaning to skip over water, or to skip stones.
</p>
<a href="/more">{{ USS Hannah }}</a>
</body>
</html>
"""

second_page = """
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>USS Hannah</title>
  <meta name="description" content="USS Hannah">
  <meta name="author" content="Amanda">

<style>
body {
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
  line-height: 1.6;
  color: #303030;
  max-width: 40rem;
  padding: 2rem;
  margin: auto;
  background: #FEF4FF;
}
img {
  max-width: 100%;
}
a {
  color: #2ECC40;
}
h1, h2, strong {
  color: #303030;
}
</style>
</head>

<body>
  <h2>USS Hannah - Brief History</h2>

<p>
The USS Hannah was a schooner and the first armed American Naval vessel. The USS Hannah was commissioned
on September 2, 1775 by George Washington. She set sail on September 5, 1775 from Beverly Massachusetts.
After having some interaction with British ships, she ran aground on October 10, 1775. Though the USS 
Hannah only sailed for about a month, it is claimed as the founding vessel of the United States Navy.
</p>
<p>Source: https://military.wikia.org/wiki/USS_Hannah</p>
</body>
</html>
"""
app = Flask(__name__)

@app.route("/")
def hello():
    return pagehtml

@app.route("/more")
def more():
    return second_page
