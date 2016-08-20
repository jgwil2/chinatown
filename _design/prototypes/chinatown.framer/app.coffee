# Import file "chinatown" (sizes and positions are scaled 1:3)
sketch = Framer.Importer.load("imported/chinatown@3x")

# Project Info
# This info is presented in a widget when you share.
# http://framerjs.com/docs/#info.info

Framer.Info =
	title: ""
	author: "Dang, Jon"
	twitter: ""
	description: ""


# set up default
gutter = 20
sketch.viewHome.props =
	x: 0
	y: 0
sketch.wf_home.visible = false
sketch.wf_book.x = Screen.width + gutter
sketch.wf_newExpense.x = (Screen.width + gutter) * 2

# Create PageComponent
pageScroller = new PageComponent
	size: Screen.size
	scrollVertical: false
	scrollHorizontal: false
	clip: false

sketch.viewHome.parent = pageScroller.content
sketch.wf_book.parent = pageScroller.content
sketch.wf_newExpense.parent = pageScroller.content

# set up states
sketch.viewHome.states.add
	in:
		opacity: 1
		scale: 1
	out:
		opacity: 0.5
		scale: 0.9
sketch.viewHome.states.animationOptions =
	time: 0.4


sketch.viewNewBook.center()
sketch.viewNewBook.bringToFront()
sketch.viewNewBook.y = Screen.height
sketch.viewNewBook.states.add
	open:
		y: 0
	close:
		y: Screen.height
sketch.viewNewBook.states.animationOptions =
	curve: 'spring(400,40,0)'
	
# set up click events
sketch.btnNewBook.on Events.Click, ->
	sketch.viewHome.states.switch("out")
	sketch.viewNewBook.states.switch("open")

sketch.btnNewBookCancel.on Events.Click, ->
	sketch.viewHome.states.switch("in")
	sketch.viewNewBook.states.switch("close")


###
sketch.bookBack.on Events.Click, ->
	pageScroller.snapToPreviousPage()
	
sketch.newExpense.on Events.Click, ->
	pageScroller.snapToNextPage()
	
sketch.expenseCancel.on Events.Click, ->
	pageScroller.snapToPreviousPage()
###