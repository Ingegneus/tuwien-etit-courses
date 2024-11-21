- some insane dude made this [[javascript]] based powerhouse [link](https://discuss.logseq.com/t/edit-and-run-javascript-code-inside-logseq-itself/20763) [link](https://discuss.logseq.com/t/edit-and-run-python-code-inside-logseq-itself/20829)
- instruction / documentation
	- Put the rest of your code directly in [[logseq]]:
	- Turn any block into code editor with `/code block` and then `javascript` (or `python`, `r` etc.) Either:
		- put some quick code in a temporary place
		- use one page per module
	- No need to restart again (unless for cleaning the memory).
	- Run your code either:
	  collapsed:: true
		- one block at a time
			- Add a child-block.
			- Type `{{evalparent}}` to get a button for running the parent’s code and showing its result.
			  ![image](https://discuss.logseq.com/uploads/default/original/2X/d/d2cc54b5fa05428c66270748f100dfe55f999d71.png)
				- The results:
					- are not saved anywhere
					- are lost when moving away
					- can be selected and copied
					- can be removed by:
						- `click` on the X-button (appears on hover) for a single one.
						- `Ctrl + click` for all the results of a code-block. #shortcut
						- `Ctrl + Shift + click` for every result everywhere. #shortcut
				- If a result is a base-64 string starting with `data:image`, it is rendered as an image.
		- one page at a time
			- Type `{{runpage}}` to get a button for running all code in the current page (of the main pane).
				- from top to bottom:
					- ignoring any content outside code-blocks of supported languages
					- auto-`await`ing each code-block before moving to the next one
				- Some other page can be specified by its name, e.g. `{{runpage mypage}}`
			- Type `{{evalpage}}` to get a button for running all visible code-blocks in parallel and showing their results.
	- Type `{{togglemsg}}` to get a button for toggling helpful (but tiring) messages.
	- Have your code run when needed from anywhere in Logseq:
		- Inside your code, register the entry function of each module with `logseq.kits.mypage = ` the function.
			- `mypage` should be the actual name of the module’s page
		- Define your own macros (like the predefined above) by adding to their attributes:
			- `class='kit'`
			- `data-kit='mypage'`
		- The system will:
			- run once the page’s code, if needed
			- call the entry function once for each macro, passing it the macro’s element
				- The macro can provide arguments to the element, read from your code with `.dataset` or `.getAttribute`
	- to use libraries in [[python]] use:
		- ```python
		  import js
		  pyodide = js.logseq.Language.python.Pyodide
		  await pyodide.loadPackage("package-name")
		  ```testing [[kits]]
	- [[file]] interactions are difficult, but maybe can be circumvented by uploading files to the internet, and then using web requests, though the standard `requests` package doesn't work in pyodide
	  id:: 664cf2b0-d577-473d-9ee0-7a82edbc3d0e
		- ```python
		  import js
		  pyodide = js.logseq.Language.python.Pyodide
		  await pyodide.loadPackage("requests")
		  
		  x=3
		  print("tst")
		  x
		  ```
			- {{evalparent}}
	- to debug your code use ((66461661-69a4-4a0b-a8a9-4e7b635edfb4)) and then scroll down until you see the python output
	- instructions for code execution
	  {{video https://www.youtube.com/watch?v=u1hi7HjG66A}}