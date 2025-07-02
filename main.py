from fasthtml.common import *

app = FastHTML(exts='ws')
rt = app.route

@rt('/')
def get():
    cts = Div(
        Div(id='notifications'),
        Form(Input(id='msg'), id='form', ws_send=True),
        hx_ext='ws', ws_connect='/ws')
    return Titled('Websocket Test', cts)

@app.ws('/ws')
async def ws(msg:str, send):
    await send(Div('Hello ' + msg, id='notifications'))

serve()