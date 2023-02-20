import json

def ordCidade(c):
    return c['nome']

f = open("mapa.json", encoding="utf8")
data = json.load(f)

cidades = data['cidades']
cidades.sort(key=ordCidade)

def getNome(id):
    for c in cidades :
        if c['id'] == id :
            return c['nome']

ligacoes = data['ligações']

pagWeb = """
<!DOCTYPE html>
<html>
        <head>
            <title>Mapa Virtual</title>
            <meta charset="utf-8"/>
        </head>
        <body>
            <h1>Mapa Virtual</h1>
            <table>
                <tr>
                    <td width="30%" valign="top">
                        <h3>Índice</h3>
                        <a name="indice"/>
                        <!-- Lista com o índice -->
                        <ul>
"""

for c in cidades :
    pagWeb += f"""
        <li>
            <a href="#{c['id']}">{c['nome']}</a>
        </li>
    """

pagWeb += """
                        </ul>
                    </td>
                    <td width="70%">
                        <!-- Informação das cidades -->
"""

for c in cidades :
    pagWeb += f"""
                        <a name="{c['id']}"/>
                        <h3>{c['nome']}</h3>
                        <p><b>população:</b> {c['população']}</p>
                        <p><b>descrição:</b> {c['descrição']}</p>
                        <p><b>distrito:</b> {c['distrito']}</p>
                        <address>[<a href="#indice">Voltar ao índice</a>]</address>
                        <p><b>ligações:</b>
                            <ul>
    """

    for l in ligacoes :
        if l['origem'] == c['id'] :
            pagWeb += f"""
                                <li><a href="#{l['destino']}">{getNome(l['destino'])}</a>: {l['distância']}</li>
            """
        elif l['destino'] == c['id'] :
            pagWeb += f"""
                                <li><a href="#{l['origem']}">{getNome(l['origem'])}</a>: {l['distância']}</li>
            """

    pagWeb += """
                            </ul>
                        </p>
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

fw = open("pagGenerated.html", "w", encoding="utf8")
fw.write(pagWeb)
fw.close()