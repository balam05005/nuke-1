"""======================================================================================================================
DEVELOPER: Tor Andreassen - www.fxtor.net
DATE: April 06, 2020
VERSION: v1.1

DESCRIPTION:
	This file contains the python-commands and callbacks used by the toolset file: dotLinker.nk
	The toolset file references the code in this file to keep the filesize low on the toolset itself.
	This way the toolset work as efficiently as possible and don't add any unnecessary filesize to the nukescript.

USAGE:
	put this python file in your .nuke directory. Either in the root or add the pluginPath your your init.py file.
	Make sure you put the toolset file (dotLinker.nk) in your ToolSets folder


	add this to your menu.py file:
		import dotLinker

	want a keyboard shourtcut?
	you can add something like this to your menu.py file (this is to use the comma-key ',' as a shortcut):
		nuke.menu("Nodes").addCommand('Other/dotLinker',"nuke.loadToolset('path-to-your-toolset-folder/dotLinker.nk')",',',icon='Dot.png',index=6)
======================================================================================================================"""
import nuke

def zoomInput():
	if nuke.thisNode().input(0):
		inX = nuke.thisNode().input(0).xpos()
		inY = nuke.thisNode().input(0).ypos()
		nuke.zoom( 0.9, [ inX, inY ])
	else:
		nuke.message('no input node, unable to connect')
#end zoomInput()






def zoomThis():
	inX = nuke.thisNode().xpos()
	inY = nuke.thisNode().ypos()
	nuke.zoom( 0.9, [ inX, inY ])
#end zoomThis()






#make global quickList if it doenst exist
def makeGlobal():
	r = nuke.Root()

	code = "import nuke\n\ndef setSelected():\n\tr = nuke.Root()\n\tselList = []\n\tdotLinkers = []\n\n\tfor i in nuke.selectedNodes():\n\t\tselList.append (i.name())\n\n\tfor i in nuke.allNodes('Dot'):\n\t\tif i.knob('isdotLinker'):\n\t\t\tdotLinkers.append(i.name())\n\n\tselList = [x for x in selList if x not in dotLinkers] #remove dotLinker nodes\n\tselList = [x for x in selList if not x.startswith('Viewer')] #remove Viewer nodes\n\tdisplaySelList =','.join(selList)\n\tr['quickList'].setValue(displaySelList)\n\nsetSelected()"
	code2 = "import nuke\n\ndef appendSelected():\n\tr = nuke.Root()\n\tcurrentQuickList = r['quickList'].value().split(',')\n\tappendList = []\n\tdotLinkers = []\n\n\tfor i in nuke.selectedNodes():\n\t\tappendList.append (i.name())\n\n\tfor i in nuke.allNodes('Dot'):\n\t\tif i.knob('isdotLinker'):\n\t\t\tdotLinkers.append(i.name())\n\n\tin_first = set(currentQuickList)\n\tin_second = set(appendList)\n\tin_second_but_not_in_first = in_second - in_first\n\tcombinedList = currentQuickList + list(in_second_but_not_in_first) #combined lists with no duplicates\n\n\tcombinedList = [x for x in combinedList if x] #remove blanks\n\tcombinedList = [x for x in combinedList if x not in dotLinkers] #remove dotLinker nodes\n\tcombinedList = [x for x in combinedList if not x.startswith('Viewer')] #remove Viewer nodes\n\tcombinedList = sorted(combinedList)\n\n\tdisplayCombinedList =','.join(combinedList)\n\tr['quickList'].setValue(displayCombinedList)\n\nappendSelected()"
	code3 = "import nuke\n\ndef dotLinkerToDot():\n\tfor i in nuke.allNodes('Dot'):\n\t\tif i.knob('isdotLinker'):\n\n\t\t\t#kill any dotLinkers with no input\n\t\t\tif not i.input(0):\n\t\t\t\tnuke.delete(i)\n\n\t\t\telse:\n\n\t\t\t\td = nuke.createNode('Dot')\n\t\t\t\td.setXpos(i.xpos())\n\t\t\t\td.setYpos(i.ypos())\n\t\t\t\td['label'].setValue(i['label'].value())\n\t\t\t\td['note_font_size'].setValue(20)\n\t\t\t\td['tile_color'].setValue(i['tile_color'].value())\n\t\t\t\td.setInput(0, nuke.toNode(i.name()))\n\t\t\t\td['hide_input'].setValue(i['hide_input'].value())\n\t\t\t\td.setSelected(False)\n\t\t\t\tnuke.delete(i)\n\n\tfor node in nuke.allNodes():\n\t\tnode.hideControlPanel()\n\n\t\tr = nuke.Root()\n\ttry:\n\t\ttab = r.knob('dotLinker')\n\t\tlst = r.knob('quickList')\n\t\tsel = r.knob('dotlinksSelected')\n\t\tapnd = r.knob('dotlinksAppend')\n\t\tkill = r.knob('dotlinksToDots')\n\t\tdiv = r.knob('dotlinker_divider')\n\n\t\tif kill:\n\t\t\tr.removeKnob(r['dotlinksToDots'])\n\t\telse:\n\t\t\tpass\n\n\t\tif apnd:\n\t\t\tr.removeKnob(r['dotlinksAppend'])\n\t\telse:\n\t\t\tpass\n\n\t\tif sel:\n\t\t\tr.removeKnob(r['dotlinksSelected'])\n\t\telse:\n\t\t\tpass\n\n\t\tif div:\n\t\t\tr.removeKnob(r['dotlinker_divider'])\n\t\telse:\n\t\t\tpass\n\n\t\tif lst:\n\t\t\tr.removeKnob(r['quickList'])\n\t\telse:\n\t\t\tpass\n\n\t\tif tab:\n\t\t\tr.removeKnob(r['dotLinker'])\n\t\telse:\n\t\t\tpass\n\n\texcept ValueError:\n\t\tpass\n\nif nuke.ask('Are you sure you want to convert all dotLinkers to Dots?  PS: any dotLinkers that are not in use will be deleted'):\n\tdotLinkerToDot()"
	tb = nuke.Tab_Knob('dotLinker','dotLinker')
	globalQuickList = nuke.String_Knob("quickList","dotLinker","")
	btnSel = nuke.PyScript_Knob('dotlinksSelected',"set selected", code)
	btnAppend = nuke.PyScript_Knob('dotlinksAppend',"append selected", code2)
	btnToDots = nuke.PyScript_Knob('dotlinksToDots',"convert to dots", code3)
	divline = nuke.Text_Knob('dotlinker_divider','','')

	dotLinkerRoot = r.knob("quickList")
	dotLinkerKill = r.knob("dotlinksToDots")
	dotLinkerRootTab = r.knob("dotLinker")

	if dotLinkerRootTab:
		pass #it already exists, do nothing
	else:
		r.addKnob(tb)
	if dotLinkerRoot:
		pass #it already exists, do nothing
	else:
		r.addKnob(globalQuickList)
		r.addKnob(divline)
		r.addKnob(btnSel)
		r['dotlinksSelected'].setTooltip('Set selected nodes to quickList.')
		r.addKnob(btnAppend)
		r['dotlinksAppend'].setTooltip('Append selected nodes to quickList.')
		r.addKnob(btnToDots)
		r['dotlinksToDots'].setTooltip("convert all dotLinkers to Dots.\n\nIf the dotLinker python file is not installed, any dotlinker Dot's in this nukescript will act as normal Dots and the buttons in it won't do anything.\n\nSimply click this button to covert them all into regular Dots, or install the fxT_dotLinker tool to take full advantage of it.")
#end makeGlobal()






#code for add button
def addButton():
	n = nuke.thisNode()
	r = nuke.Root()


	def addToList():

		#generate values for quickList (combining current local and global list)
		localQuickList = nuke.thisNode()['quickList'].values() #this nodes quickList
		globalQuickList =  nuke.Root()['quickList'].value().split(",") # global quickList back to list
		in_first = set(localQuickList)
		in_second = set(globalQuickList)
		in_second_but_not_in_first = in_second - in_first
		quickList = localQuickList + list(in_second_but_not_in_first) #combined lists with no duplicates

		#get non-existent nodes
		removeList = []
		for i in quickList:
			if not nuke.toNode(i):
				removeList.append(i)
		removeList = [x for x in removeList if x] #remove blanks 
		removeList = sorted(removeList)
		displayRemoveList =', '.join(removeList)

		#strip non-existent nodes from quickList
		in_firstList = set(quickList)
		in_secondList = set(removeList)
		in_first_but_not_in_second = in_firstList - in_secondList
		quickList = list(in_first_but_not_in_second)

		#strip any item starting with Viewer from quickList
		quickList = [x for x in quickList if not x.startswith('Viewer')]

		#if list is blank, reset list so it doenst have any value and a lenght of expected 0
		if quickList == ['']:
			quickList = []
		else:
			pass

		listSelected = n['quickList'].value() #get the current selection in this node's quickList dropdown

		#check if input exits and if item is not a duplicate
		if n.input(0):
			if n.input(0).name() not in localQuickList: # check for duplicates in global quickList

				if nuke.ask('are you sure you want to add ' + n['inputNode'].value() + ' to the quickList?'):
					quickList.append(n.input(0).name())
					quickList = [x for x in quickList if x] #remove blanks 
					#removing any duplicates from quickList
					quickList = list(dict.fromkeys(quickList))
					#sort list alphabetically
					quickList = sorted(quickList)

					#update local and global quickLists
					n['quickList'].setValues(quickList) #update quickConnect dropdown-list
					displayList  =','.join(quickList)
					r['quickList'].setValue(displayList) #update global quickConnect list
					n['quickList'].setValue(n.input(0).name()) #set quickConnect dropdown-list to current input

				else:
					#user cancel, only remove nonexistent nodes from global quickList
					displayList  =','.join(quickList)
					r['quickList'].setValue(displayList)

			elif n.input(0).name() in localQuickList and n.input(0).name() not in globalQuickList:
				quickList = sorted(quickList)
				displayList  =','.join(quickList)        
				r['quickList'].setValue(displayList)
				nuke.message(str(n.input(0).name()) +' already exist in list, nothing to add, global list updated')
			else:
				nuke.message(str(n.input(0).name()) +' already exist in quickList, nothing to add')
				displayList  =','.join(quickList)
				r['quickList'].setValue(displayList)
		else:
			nuke.message('there is no input node, nothing to add')

			#remove non-existent nodes from global quickList
			displayList  =','.join(quickList)
			r['quickList'].setValue(displayList)

		#if there is non-existent nodes in the global quickList, tell user they were removed.
		if len(removeList)>0 and '-----' not in removeList:
			nuke.message('The quickList had some non-existent nodes.\n\nThese nodes have been removed from the quickList:\n\n'+displayRemoveList)
	addToList()
#end addButton()






#code for remove button
def removeButton():
	n = nuke.thisNode()
	r = nuke.Root()

	def removeFromList():

		#generate values for quickList (combining current local and global list)
		localQuickList = n['quickList'].values() #this nodes quickList
		globalQuickList =  r['quickList'].value().split(",") # global quickList back to list
		in_first = set(localQuickList)
		in_second = set(globalQuickList)
		in_second_but_not_in_first = in_second - in_first
		quickList = localQuickList + list(in_second_but_not_in_first) #combined lists with no duplicates

		#get non-existent nodes
		removeList = []
		for i in quickList:
			if not nuke.toNode(i):
				removeList.append(i)
		removeList = [x for x in removeList if x] #remove blanks 
		removeList = sorted(removeList)
		displayRemoveList =', '.join(removeList)



		#strip non-existent nodes from quickList
		in_firstList = set(quickList)
		in_secondList = set(removeList)
		in_first_but_not_in_second = in_firstList - in_secondList
		quickList = list(in_first_but_not_in_second)

		#strip any item starting with Viewer from quickList
		quickList = [x for x in quickList if not x.startswith('Viewer')]

		#if list is blank, reset list so it doenst have any value and a lenght of expected 0
		if quickList == ['']:
			quickList = []
		else:
			pass


		listSelected = n['quickList'].value() #get the current selection in this node's quickList dropdown

		#ask if user want to kill item
		if len(localQuickList) > 0 and '-----' not in localQuickList:
			if nuke.ask('are you sure you want to remove ' + listSelected + ' from the quickList?'):
				quickList.remove(listSelected)
				quickList = [x for x in quickList if x] #remove blanks
				#removing any duplicates from quickList
				quickList = list(dict.fromkeys(quickList))
				#sort list alphabetically
				quickList = sorted(quickList)

				#update local and global quickLists
				n['quickList'].setValues(quickList) #update quickConnect dropdown-list
				displayList  =','.join(quickList)
				r['quickList'].setValue(displayList) #update global quickConnect list
				if len(quickList) != 0:
					n['quickList'].setValue(quickList[0]) #set quickConnect dropdown-list to the first in the list
				else:
					n['quickList'].setValues(['-----',''])
					pass

			else:
				#user cancel, only remove nonexistent nodes from global quickList
				displayList  =','.join(quickList)
				if r['quickList']:
					r['quickList'].setValue(displayList)
				else:
					pass

		else:
			nuke.message('List is blank, nothing to remove.')
			#also kill global quickList
			displayList  =','.join(quickList)
			r['quickList'].setValue('')

		if len(removeList)>0 and '-----' not in removeList:
			nuke.message('The quickList had some non-existent nodes.\n\nThese nodes have been removed from the quickList:\n\n'+displayRemoveList)
	removeFromList()
#end removeButton()






#code for clear button
def clearButton():
	n = nuke.thisNode()
	r = nuke.Root()

	def clearList():
		quickList = n['quickList'].values()
		blankList = ['-----','']

		if len(quickList) > 0:
			if nuke.ask('are you sure you want to clear the quickList?'):
				blankList = [x for x in blankList if x] #remove blanks
				n['quickList'].setValues(blankList) #clear local quickList

				try:
					r['quickList'].setValue('') #clear global quickList
				except NameError:
					pass
			else:
				pass #no was pressed, do nothing
		elif len(quickList) == 0:
			try:
				r['quickList'].setValue('') #clear global quickList
				n['quickList'].setValues(blankList)
				nuke.message('List is already blank, nothing to clear. global list was reset.')
			except NameError:
				nuke.message('List is already blank, nothing to clear.')
				pass
	clearList()
#end clearButton()






#code for reload button
def reloadButton():
	n=nuke.thisNode()
	r = nuke.Root()

	def reloadList():

		#generate values for quikList (combining current local and global list)
		localQuickList = nuke.thisNode()['quickList'].values() #this nodes quickList
		globalQuickList =  nuke.Root()['quickList'].value().split(",") # global quickList back to list
		in_first = set(localQuickList)
		in_second = set(globalQuickList)
		in_second_but_not_in_first = in_second - in_first
		quickList = localQuickList + list(in_second_but_not_in_first) #combined lists with no duplicates

		#get non-existent nodes
		removeList = []
		for i in quickList:
			if not nuke.toNode(i):
				removeList.append(i)
		removeList = [x for x in removeList if x] #remove blanks
		removeList = sorted(removeList)
		displayRemoveList =', '.join(removeList)

		#strip non-existent nodes from quickList
		in_firstList = set(quickList)
		in_secondList = set(removeList)
		in_first_but_not_in_second = in_firstList - in_secondList
		quickList = list(in_first_but_not_in_second)

		#strip any item starting with Viewer from quickList
		quickList = [x for x in quickList if not x.startswith('Viewer')]

		#if list is blank, reset list so it doenst have any value and a lenght of expected 0
		if quickList == ['']:
			quickList = []
		else:
			pass

		quickList = [x for x in quickList if x] #remove blanks
		quickList = sorted(quickList)
		displayList  =','.join(quickList)

		listSelected = n['quickList'].value() #get the current selection in this node's quickList dropdown

		#ask
		if nuke.ask('are you sure you want to reload list?'):
			#update local and global quickLists
			n['quickList'].setValues(quickList) #update quickConnect dropdown-list
			r['quickList'].setValue(displayList) #update global quickConnect list

			if len(quickList) != 0:
				n['quickList'].setValue(quickList[0]) #set quickConnect dropdown-list to the first in the list
			else:
				n['quickList'].setValues(['-----',''])
				pass

			if len(removeList)>0 and '-----' not in removeList:
				nuke.message('The quickList had some non-existent nodes.\n\nThese nodes have been removed from the quickList:\n\n'+displayRemoveList)

		else:
			#user canceled reload process, do nothing
			pass

	reloadList()
#end reloadButton()






#code for connect button
def connectButton():
	n = nuke.thisNode()

	def connectMe():
		val = n['quickList'].values()
		sel = n['quickList'].value()
		hideValue = n['hideInput'].value()

		if len(val) == 0 or sel == '-----':
			nuke.message('quickList is empty, nothing to connect to.')
			n.setInput(0, None)
			n['hide_input'].setValue(False)
			pass
		else:

			if nuke.toNode(sel):
				n.setInput(0,nuke.toNode(sel))
				if hideValue == True:
					n['hide_input'].setValue(True)
				else:
					n['hide_input'].setValue(False)
			else:
				nuke.message(sel+' does not exist, please reload quickList.')
				n.setInput(0, None)
				n['hide_input'].setValue(False)
	connectMe()
#end reloadButton()






########################## CALLBACK'S CODE BELOW THIS LINE ##########################

#onDestroy callback, to kill global quickList knobs if no dotLinker nodes exist
def killGlobal():
	r = nuke.Root()

	try:
		tb = nuke.Tab_Knob('dotLinker','dotLinker')
		globalQuickList = nuke.String_Knob("quickList","dotLinker","")
		dotLinkerRootTab = r.knob("dotLinker")
		dotLinkerRoot = r.knob("quickList")    		
		dotLinkerRootSelected = r.knob("dotlinksSelected")
		dotLinkerRootAppend = r.knob("dotlinksAppend")
		dotLinkerKill = r.knob("dotlinksToDots")
		dotLinkerDivider = r.knob("dotlinker_divider")

		dotLinks = []
		for i in nuke.allNodes('Dot'):
			if i.knob('isdotLinker'):
				dotLinks.append(i.name())

		if len(dotLinks)==1:
			if dotLinkerKill:
				r.removeKnob(r['dotlinksToDots'])
			else:
				pass #no global 'convert to dots' button exists, do nothing

			if dotLinkerRootAppend:
				r.removeKnob(r['dotlinksAppend'])
			else: 
				pass #no global 'append selected' button exists, do nothing

			if dotLinkerRootSelected:
				r.removeKnob(r['dotlinksSelected'])
			else:
				pass #no global 'set selected' button exists, do nothing

			if dotLinkerDivider:
				r.removeKnob(r['dotlinker_divider'])
			else:
				pass #no global divider line exists, do nothing

			if dotLinkerRoot:
				r.removeKnob(r['quickList'])
			else:
				pass #no global 'quickList' exists, do nothing

			if dotLinkerRootTab:
				r.removeKnob(r['dotLinker'])
			else:
				pass #no global 'quickList' tab exists, do nothing

		else:
			pass #no dotLinker nodes in nukescript, do nothing

	except ValueError:
		pass
#end killGlobal()






#onCreate callback, #reset node on copyPaste
def resetOnPaste():
	n = nuke.thisNode()
	if n.input(0):
		pass
	else:
		n['inputNode'].setValue('')
		n["input_status"].setValue('<i style="color:yellow">No Connection</i> ')
		n["tile_color"].setValue(0)
		n['hide_input'].setValue(False)
		n['label'].setValue("<img src='Dot.png'><br /><font color='#ccc'>dotLinker</font>")
# end resetOnPaste()






#code for auto setup of quickList (gets executed only if a globalList already exists..)
def autoQuickList():
	n=nuke.thisNode()
	r = nuke.Root()

	try:
		if r.knob("quickList"):

			#generate values for quikList (combining current local and global list)
			localQuickList = nuke.thisNode()['quickList'].values() #this nodes quickList
			globalQuickList =  nuke.Root()['quickList'].value().split(",") # global quickList back to list
			in_first = set(localQuickList)
			in_second = set(globalQuickList)
			in_second_but_not_in_first = in_second - in_first
			quickList = localQuickList + list(in_second_but_not_in_first) #combined lists with no duplicates

			if ('-----') in quickList: #remove '----' as it will always be present in a new node creation
				quickList.remove('-----')

			#get non-existent nodes
			removeList = []
			for i in quickList:
				if not nuke.toNode(i):
					removeList.append(i)
			removeList = [x for x in removeList if x] #remove blanks
			removeList = sorted(removeList)

			displayRemoveList =', '.join(removeList)

			#strip non-existent nodes from quickList
			in_firstList = set(quickList)
			in_secondList = set(removeList)
			in_first_but_not_in_second = in_firstList - in_secondList
			quickList = list(in_first_but_not_in_second)

			#strip any item starting with Viewer from quickList
			quickList = [x for x in quickList if not x.startswith('Viewer')]

			#if list is blank, reset list so it doenst have any value and a lenght of expected 0
			if quickList == ['']:
				quickList = []
			else:
				pass

			quickList = [x for x in quickList if x] #remove blanks
			quickList = sorted(quickList)
			displayList  =','.join(quickList)

			#update local and global quickLists
			n['quickList'].setValues(quickList) #update quickConnect dropdown-list
			r['quickList'].setValue(displayList) #update global quickConnect list

			if len(quickList) != 0:
				n['quickList'].setValue(quickList[0]) #set quickConnect dropdown-list to the first in the list
			else:
				n['quickList'].setValues(['-----',''])
				pass

			if len(removeList)>0:
				nuke.message("While auto reloading this node's quickList, some non-existent nodes were found.\n\nThese nodes have been removed from the quickList:\n\n"+displayRemoveList)

		else:
			pass #no global quickList existed, do nothing
	except ValueError:
		print ('dotLinker: there was a value error on autoQuickList execution, please reload manually')
#end autoQuickList()






def firstCreation():
	#hack to not allow input on creation
	dummyDot = nuke.createNode('Dot')
	nuke.delete(dummyDot)

	initKnob = nuke.thisNode().knob('initialized')
	if initKnob.value() == False:
		autoQuickList()

		initKnob.setValue(True)
		nuke.show(nuke.thisNode())
		nuke.thisNode()['exprBugFix'].execute() #execute blank button to kill fake expression pipes (nuke bug hack)
	else:
		pass






def knobsUpdate():
	# detect input
	me = nuke.thisNode()
	hideValue = me['hideInput'].value()


	if nuke.thisKnob().name() == "inputChange":


		if me.input(0):
			inputName = me.input(0).name()
			me['inputNode'].setValue(inputName)
			me["input_status"].setValue('<i style="color:limegreen">'+inputName+'<br />Connected</i>')

			me.setInput(0, None) # dissconnect first to not display fake expression pipes (nuke bug hack)
			if nuke.toNode(inputName)['tile_color'].value() ==0:
				inCol = str( nuke.defaultNodeColor( nuke.toNode(inputName).Class() ) )
			else:
				inCol = nuke.toNode(inputName)['tile_color'].value()
			me["tile_color"].setValue(int(inCol))


			me.setInput(0,nuke.toNode(inputName))

			if hideValue == True:
				me['hide_input'].setValue(True)
			else:
				me['hide_input'].setValue(False)

			#set label based on dropdown label-type
			if nuke.thisNode()['extraLabel'].evaluate() is None:
				nuke.thisNode()['extraLabel'].setValue('')

			if me['labelType'].value() == 'input node':
				me['label'].setValue("<font color='#ccc'>" +str(me.input(0).name()) + "<br />"+ str(me['extraLabel'].evaluate())+ "</font>" )
			elif me['labelType'].value() == 'input label':
				if me.input(0)['label'].evaluate() is None:
					me['label'].setValue("<font color='#ccc'>" + me['extraLabel'].evaluate()+"</font>" )
				else:
					me['label'].setValue("<font color='#ccc'>" + str(me.input(0)['label'].evaluate()) +'<br />'+me['extraLabel'].evaluate() +"</font>" )
			else:
				me['label'].setValue("<font color='#ccc'>" + me['extraLabel'].evaluate()+"</font>" )



			#deny connection to dotLinkers
			denyNodes = []
			for i in nuke.allNodes('Dot'):
				if i.knob('isdotLinker'):
					denyNodes.append(i.name())    
	 
			if inputName in denyNodes:
				me['inputNode'].setValue('')
				me.setInput(0,None)
				me["input_status"].setValue('<i style="color:yellow">No Connection</i> ')
				me['hide_input'].setValue(False)
				me['label'].setValue("<img src='Dot.png'><br /><font color='#ccc'>dotLinker</font>")	

		else:
			inputName = ''
			me['inputNode'].setValue('')
			me["input_status"].setValue('<i style="color:yellow">No Connection</i> ')
			me["tile_color"].setValue(0)
			me['hide_input'].setValue(False)
			me['label'].setValue("<img src='Dot.png'><br /><font color='#ccc'>dotLinker</font>")


	if nuke.thisKnob().name() == "inputNode":
		newConnection = me['inputNode'].value()
		hideValue = me['hideInput'].value()

		#generate list of dotLinks and viewers in nukescript (to deny connection to nodes)
		denyNodes = []
		for i in nuke.allNodes('Dot'):
			if i.knob('isdotLinker'):
				denyNodes.append(i.name())
		for i in nuke.allNodes():
			if i.Class() == 'Viewer':
				denyNodes.append(i.name())

		if nuke.toNode(newConnection) and newConnection not in denyNodes:
			me.setInput(0, None) # dissconnect first to not produce temp fake link
			if nuke.toNode(newConnection)['tile_color'].value() ==0:
				inCol = str( nuke.defaultNodeColor( nuke.toNode(newConnection).Class() ) )
			else:
				inCol = nuke.toNode(newConnection)['tile_color'].value()
			me["tile_color"].setValue(int(inCol))


			me.setInput(0,nuke.toNode(newConnection))
			if hideValue == True:
				me['hide_input'].setValue(True)
			else:
				me['hide_input'].setValue(False)
			if me.Class() == 'Viewer':
				pass
			else:
				me["input_status"].setValue('<i style="color:limegreen">'+me.input(0).name()+'<br />Connected</i>')



			#set label based on dropdown label-type
			try:
				if me['labelType'].value() == 'input node':
					me['label'].setValue("<font color='#ccc'>" +str(me.input(0).name()) +"<br />"+me['extraLabel'].evaluate()+"</font>" )
				elif me['labelType'].value() == 'input label':
					if me.input(0)['label'].evaluate() is None:
						me['label'].setValue("<font color='#ccc'>" + me['extraLabel'].evaluate()+"</font>" )
					else:
						me['label'].setValue("<font color='#ccc'>" + str(me.input(0)['label'].evaluate()) +'<br />'+me['extraLabel'].evaluate() +"</font>" )
				else:
					me['label'].setValue("<font color='#ccc'>" + me['extraLabel'].evaluate()+"</font>" )
			except TypeError:
				pass


		elif me['inputNode'].value() in denyNodes:
			nuke.message('connection to dotLinker nodes and Viewers are not allowed, connection attempt aborted')
			if me.input(0):
				me['inputNode'].setValue(me.input(0).name())
			else:
				me['inputNode'].setValue('')

		elif me['inputNode'].value() == '':
			me.setInput(0, None)
			me['inputNode'].setValue('')
			me["input_status"].setValue('<i style="color:yellow">No Connection</i> ')
			me["tile_color"].setValue(0)
			me['hide_input'].setValue(False)
			me['label'].setValue("<img src='Dot.png'><br /><font color='#ccc'>dotLinker</font>")


		else:
			nuke.message(str(newConnection)+' does not exits, connection attempt aborted')
			if me.input(0):
				me['inputNode'].setValue(me.input(0).name())
			else:
				me['inputNode'].setValue('')







	if nuke.thisKnob().name() == "hideInput":
		hideValue = me['hideInput'].value()

		if hideValue == True:
			me['hide_input'].setValue(True)
		else:
			me['hide_input'].setValue(False)






	if nuke.thisKnob().name() == "labelType" or nuke.thisKnob().name() == 'extraLabel' :
		if me.input(0):
			try:
				if me['labelType'].value() == 'input node':
					me['label'].setValue("<font color='#ccc'>" + str(me.input(0).name()) +'<br />'+me['extraLabel'].evaluate() +"</font>" )
				elif me['labelType'].value() == 'input label':
					if me.input(0)['label'].evaluate() is None:
						me['label'].setValue("<font color='#ccc'>" + me['extraLabel'].evaluate() +"</font>" )
					else:
						me['label'].setValue("<font color='#ccc'>" + str(me.input(0)['label'].evaluate()) +'<br />'+me['extraLabel'].evaluate() +"</font>" )
				else:
					me['label'].setValue("<font color='#ccc'>" + me['extraLabel'].evaluate() +"</font>" )
			except TypeError:
				pass
		else:
			pass
# end knobsUpdate()
