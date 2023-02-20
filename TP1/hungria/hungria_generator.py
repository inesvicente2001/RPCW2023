import json


f = open("hungria.json", encoding="utf8")
data = json.load(f)
sec = data['secções']

def getNome(id):
    for s in sec :
        if s['id'] == id :
            return s['nome']


pagWeb = """
<!DOCTYPE html>
<html>
        <head>
            <title>Hungria</title>
            <meta charset="utf-8"/>
        </head>
        <body>
            <h1>Hungria</h1>
            <table>
                <tr>
                    <td width="30%" valign="top">
                        <h3>Conteúdo</h3>
                        <a name="indice"/>
                        <!-- Lista com o índice -->
                        <ul>
"""

for s in sec :
    pagWeb += f"""
        <li>
            <a href="#{s['id']}">{s['nome']}</a>
    """
    if s['subsecções'] != [] :
        pagWeb += "<ul>"
        for ss in s['subsecções'] :
            pagWeb += f"""
                <li>
                    <a href="#{ss['id']}">{ss['nome']}</a>
                </li>
            """
        pagWeb += "</ul>" 
    pagWeb += "</li>"

pagWeb += """
                        </ul>
                    </td>
                    <td width="70%">
"""

for s in sec :
    pagWeb += f"""
                        <a name="{s['id']}"/>
                        <h3>{s['nome']}</h3>
    """

    for p in s['conteúdo'] :
        pagWeb += f"<p>{p}</p>"

    for ss in s['subsecções'] :
        pagWeb += f"""
                <a name="{ss['id']}"/>
                <h4>{ss['nome']}</h4>
        """
        for p in ss['conteúdo'] :
            pagWeb += f"<p>{p}</p>"

    pagWeb += """
                        <center>
                            <hr width="80%"/>
                        </center>
    """

pagWeb += """
                    </td>
                </tr>
            </table>
        </body>
</html>
"""

fw = open("hungriaGenerated.html", "w", encoding="utf8")
fw.write(pagWeb)
fw.close()