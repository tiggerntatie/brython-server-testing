from browser import window, document

def onload(window):
    canvas = window.document.createElement('canvas')
    canvas.setAttribute('width','800')
    canvas.setAttribute('height','500')
    canvas.setAttribute('style','border:1px solid #000000;')
    window.document.body.appendChild(canvas)
    

w = window.open("", "")
w.onload = onload(w)


print("Testing Graphics")

