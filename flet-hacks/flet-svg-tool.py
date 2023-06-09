# flet hacks - convert svg to png for use in flet
# by hololeo
import flet
from flet import Page, Text, Column, Row, Container, alignment, colors
from flet import TextField, ElevatedButton, Image
import cairosvg # https://cairosvg.org/ (see dependencies!)
import base64 

def svg_paste_box (page):
  # make textfield to paste in svg code
  global flet_svg_logo

  control = TextField (
    value = flet_svg_logo,
    width= 1000,
    min_lines = 10,
    max_lines = 10,
    multiline = True,
    border_width= 2,
    color = "white",
    text_size = 16

  )
  control.page  = page
  column = Column ()
  column.tf = control
  column.controls.append (control)
  return column


def makeButton (page):
  # make a convert to png button
  def on_click_btn (e):
    print ("clicked to png button")
    e.control.page.svgToPng (e.control.page)

  btn = ElevatedButton ("to png", on_click = on_click_btn)
  return btn

def makeImageViewer (page):
  container = Container (
    width = 1000,
    height = 300,
    bgcolor = "blue400",
    border_radius = 5,
    padding = 10,
    content = Text ("paste svg above and click to png to view here")
  )
  return container

def svgToPng (page):
  # outputs png to assets/output.png
  outputFile = 'assets/output.png'
  svgData = page.tf.controls[0].value
  cairosvg.svg2png( bytestring=svgData, write_to=f"assets/output.png")
  on_complete_svgToPng (page, outputFile)

def on_complete_svgToPng (page, img_file_path):
  with open(img_file_path, "rb") as img_file:
      b64_string = base64.b64encode(img_file.read())
      b64_string = b64_string.decode ('utf-8')
  #print (b64_string)
  png = Image (
    #src = img_file
    src_base64 = b64_string
  )
  page.image_viewer.clean()
  page.image_viewer.content =  png
  page.update()

def main(page: Page):
  page.title = "Flet Svg Tool by HoloLeo"
  page.window_always_on_top = True  
  page.vertical_aligment = "start"
  page.scroll = "auto"
  page.tf  = svg_paste_box (page)
  page.btn = makeButton (page)
  page.image_viewer = makeImageViewer (page)
  page.svgToPng = svgToPng
  page.add (page.tf)
  page.add (page.btn)
  page.add (page.image_viewer)
  page.update()


flet_svg_logo = """
<svg xmlns="http://www.w3.org/2000/svg" xml:space="preserve" width="759px" height="266px" version="1.1" shape-rendering="geometricPrecision" text-rendering="geometricPrecision" image-rendering="optimizeQuality" fill-rule="evenodd" clip-rule="evenodd"
viewBox="0 0 446.47 156.41"
 xmlns:xlink="http://www.w3.org/1999/xlink">
 <g id="Layer_x0020_1">
  <metadata id="CorelCorpID_0Corel-Layer"/>
  <path fill="#EE3167" d="M0.35 78.6c-0.54,-0.96 -0.41,-1.65 0.07,-2.62 19.9,-36.97 49.93,-59.65 87.77,-75.86 1.29,-0.55 3.19,0.96 2.73,2.31 -5.64,16.41 -9.62,32.39 -11.93,49.56 -2.1,15.82 -2.68,32.18 -0.55,49.27 2.26,19.39 6.89,35.48 12.47,52.82 0.62,1.93 -1.35,2.81 -2.86,2.07 -39.4,-19.4 -69.26,-44.76 -87.7,-77.55z"/>
  <path fill="#0098DA" fill-opacity="0.639216" d="M117.72 112.72c-21.78,-6.83 -41.27,-18.41 -58.54,-33.71 -1.15,-1.02 -1.02,-2.45 0.02,-3.44 17.15,-16.4 36.61,-29.27 58.13,-38.37 1.89,-0.81 3.45,0.76 2.89,2.92 -6.1,23.39 -7.44,46.5 0.08,69.67 0.62,1.93 -0.94,3.44 -2.58,2.93z"/>
  <path fill="#5ABAE7" d="M117.72 112.72c-14.34,-4.5 -27.69,-11.06 -40.06,-19.37 -0.86,-13.25 -0.93,-19.14 0.46,-33.75 12.16,-9.01 25.25,-16.5 39.21,-22.4 1.89,-0.81 3.45,0.76 2.89,2.92 -6.1,23.39 -7.44,46.5 0.08,69.67 0.62,1.93 -0.94,3.44 -2.58,2.93z"/>
  <polygon fill="#4B4B4D" fill-rule="nonzero" points="188.97,143.43 173.38,143.43 173.38,19.56 249.15,19.56 249.15,33.12 188.97,33.12 188.97,72.3 238.75,72.3 238.75,84.74 188.97,84.74 "/>
  <polygon id="1" fill="#4B4B4D" fill-rule="nonzero" points="280.5,143.43 266.39,143.43 266.39,19.56 280.5,19.56 "/>
  <path id="2" fill="#4B4B4D" fill-rule="nonzero" d="M369.64 116.31l13.19 2.73c-2.42,7.8 -7.15,14.24 -14.15,19.34 -7.02,5.11 -15.29,7.65 -24.79,7.65 -12.54,0 -22.66,-4.4 -30.42,-13.22 -7.74,-8.82 -11.61,-20.36 -11.61,-34.66 0,-14.58 4.02,-26.41 12.07,-35.38 8.05,-9.01 18.14,-13.5 30.3,-13.5 11.95,0 21.61,4.15 28.88,12.48 7.27,8.29 11.02,20.73 11.2,37.29l-66.67 0c0,13.84 2.91,23.19 8.73,28.05 5.85,4.83 12.01,7.24 18.51,7.24 11.7,0 19.97,-6.01 24.76,-18.02zm-0.93 -27.85c-0.12,-5.17 -0.95,-9.75 -2.53,-13.74 -1.58,-4.03 -4.27,-7.43 -8.02,-10.25 -3.78,-2.82 -8.3,-4.24 -13.56,-4.24 -7.12,0 -13.12,2.54 -18.07,7.64 -4.96,5.11 -7.71,11.95 -8.33,20.59l50.51 0z"/>
  <path id="3" fill="#4B4B4D" fill-rule="nonzero" d="M446.47 133.77l0 11.33c-5.05,0.62 -9.41,0.93 -13.1,0.93 -17.76,0 -26.65,-9.26 -26.65,-27.8l0 -55.21 -16.15 0 0 -11.15 16.15 0 0.56 -23.06 13.56 -1.27 0 24.33 20.43 0 0 11.15 -20.43 0 0 57.54c0,9.44 4.86,14.14 14.61,14.14 3.25,0 6.93,-0.31 11.02,-0.93z"/>
 </g>
</svg>
""".strip()

# flet.app(target=main, assets_dir="assets")
flet.app(target=main, view=flet.WEB_BROWSER, port=8080, assets_dir="assets")
