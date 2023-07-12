import csv
import os
from html import escape

# Change the working directory to the script directory
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Initialize the HTML components
title = os.path.basename(os.getcwd())
body = ''
body += f'<h1>{title}</h1>\n'  # Add title to body here

# Check if thumbnail.png exists, if so, add it to body
thumbnail_path = os.path.join(os.getcwd(), 'thumbnail.png')
if os.path.exists(thumbnail_path):
    body += f'<div class="div-img"><img src="thumbnail.png" alt="Image"></div>\n'

# CSVファイルを読み込む
with open('scenario.csv', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        command = row[0]
        content = row[1]

        if command == 'p':
            # Replace the newline character with <br> only for paragraphs
            content = content.replace('\n', '<br>')
            body += f'<div class="div-p"><p>{content}</p></div>\n'
        elif command == 'img':
            body += f'<div class="div-img"><h2>{escape(content)}</h2><img src="{escape(content)}" alt="Image"></div>\n'
        elif command == 'video':
            body += f'<div class="div-video"><h2>{escape(content)}</h2><video controls onmouseover="this.play()" onmouseout="this.pause();">\n<source src="{escape(content)}" type="video/mp4">\nYour browser does not support the video tag.\n</video></div>\n'
        elif command == 'code':
            body += f'<div class="div-code code-container"><button onclick="copyToClipboard(\'codeBlock\')">Copy to clipboard</button>\n<pre id="codeBlock"><code>{escape(content)}</code></pre></div>\n'
        elif command == 'question':
            # Replace the newline character with <br> for questions
            content = content.replace('\n', '<br>')
            body += f'<div class="div-question"><h3>Question:</h3><p>{content}</p></div>\n'
        elif command == 'answer':
            # Replace the newline character with <br> for answers
            content = content.replace('\n', '<br>')
            body += f'<div class="div-answer"><h3>Answer:</h3><p>{content}</p></div>\n'

# HTMLを出力
output_filename = os.path.basename(os.getcwd()) + '.html'
with open(output_filename, 'w', encoding='utf-8') as f:
    f.write(f"""<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <link rel="stylesheet" type="text/css" href="styles.css">
    <script>
    function copyToClipboard(elementId) {{
        var aux = document.createElement("textarea");
        aux.innerHTML = document.getElementById(elementId).textContent;
        document.body.appendChild(aux);
        aux.select();
        document.execCommand("copy");
        document.body.removeChild(aux);
    }}
    </script>
</head>
<body>
{body}
</body>
</html>""")
