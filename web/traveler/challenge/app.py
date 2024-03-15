from flask import Flask, abort

app = Flask(__name__)

# before delete the page 
page_content = "<h2>Webpage Might be Temporarily Down or it may Have Moved</h2>"

# page_content = "This page has been deleted"

@app.route('/flag')
def flag_page():
    return page_content

if __name__ == '__main__':
    app.run(debug=True)
