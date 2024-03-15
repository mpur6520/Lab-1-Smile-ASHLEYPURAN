from browser import document, html, window, alert
import random

def sketch(p): #p is needed as a parameter, it will be the processing sketch itself 
  #to do things like background color
  #background(0) instead of p.background
  def setup():
    p.createCanvas(2010,860)
    p.background(255)
    p.rectMode(p.CENTER)
  
  def draw():
    colorList = ['pink', 'purple', 'yellow', 'magenta']
    p.noStroke()
    p.fill(random.choice(colorList))
    p.ellipse(p.mouseX, p.mouseY, 50,50)
    
  def mousePress(self):
    p.background(0)
    
  def keyPress(self):
    if p.key == " ":
      print("ALOHA!!")

  p.setup = setup
  p.draw = draw
  p.mousePressed = mousePress #aaa
  p.keyPressed = keyPress #aaa

myp5 = window.p5.new(sketch)