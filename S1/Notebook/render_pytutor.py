import urllib.parse
from IPython.display import IFrame

def render_pytutor():
    last_cell_run_text = _ih[-2]
    code_text = urllib.parse.quote(last_cell_run_text) 
    return IFrame(f"https://pythontutor.com/iframe-embed.html#code={code_text}&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=false&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false", width=1300, height=550)