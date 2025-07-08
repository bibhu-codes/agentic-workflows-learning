from nicegui import ui

"""
🎯 Summary:
- Learned how to create dynamic text-based status labels using class inheritance.
- Explored hyperlink creation inside text using ui.label, ui.link, ui.html.
- Studied link-target navigation and spacing tricks.
- Final experiment: Embedding image inside link to act as a button.
- Demonstrated different ways to customize ui.chat_message using HTML, multiline text, and child elements with with block.

🧠 Concepts Practiced: NiceGUI Label/Link/Row/Column, Unicode spacing, Anchor navigation
"""

# =======================
# ✅ 1. Dynamic Status Label
# =======================

class status_label(ui.label):
    def _handle_text_change(self, text: str) -> None:
        super()._handle_text_change(text)
        if text=='ok':
            self.classes(replace='text-positive')
        else:
            self.classes(replace='text-negative')

model = {'status':'error'}

def handle_switch_change(e):
    # if e.value:
    #     model['status'] = 'ok'
    # else:
    #     model['status'] = 'error'
    model.update(status = 'ok' if e.value else 'error')

status_label().bind_text_from(target_object=model,target_name='status')
#below three achieves the same. one without parameter, one by passing the parameter, another inline lambda function
# ui.switch(on_change= handle_switch_change)
# ui.switch(on_change= lambda e: handle_switch_change(e))
ui.switch(on_change= lambda e: model.update(status='ok' if e.value else 'error'))


# =======================
# ✅ 2. links
# =======================
#the whole text becomes a link
ui.link('Here is a link to Google','https://google.com',new_tab=True)

#tried to make the part of text as hyperlink but resulted in error
# ui.label("Here is a link to "+ ui.link(text='Google',target="https://www.google.com", new_tab=True))

#works but keep default gap as 4 between text and Google
with ui.row():
    ui.label("Here is a link to")
    ui.link(text='Google', target='https://google.com', new_tab=True)

#made the gap zero but have to add non-breaking space as by default all trailing spaces were truncated
with ui.row().classes('gap-x-0'):
    ui.label("Here is a link to\u00A0")
    ui.link(text='Google', target='https://google.com', new_tab=True)

#another way of achieving the same using span but have to use inline class else both of them were
#rendered as one below the other just like div blocks like <span><div>ui.label</div></span>
with ui.element('span'):
    ui.label("Here is a link to ").classes('inline')
    ui.link(text='Google', target='https://google.com', new_tab=True).classes('inline')

#directly use the html to achieve the same
ui.html('Here is a link to <a href="https://google.com" target="_blank_" class="text-blue underline">Google</a>')

#to jump specific location in a page, there is two-way of doing so.
navigation = ui.row()
ui.link_target('target_A')
ui.label('Today I am learning basic hands on of niceGUI.')

label_B = ui.link(text='https://google.com',target='https://google.com',new_tab=True)

with navigation:
    ui.link(text='Text', target='#target_A')
    ui.link(text='Link', target=label_B)

#Trying to create Search Engine Links text which on clicking should take to a list of search engine hyperlinks
with ui.column():
    ui.link(text='Search Engines: ', target='#target_links')

for i in range(5):
    ui.label("random text:")
    ui.label('hello')
    ui.html("<br><br><br><br><br><br><br><br><br>")

ui.link_target('target_links')
with ui.column():
    ui.label('Links Section:')
    ui.link(text='Google', target='https://google.com', new_tab=True)
    ui.link(text='Bing', target='https://bing.com', new_tab=True)
    ui.link(text='Yahoo', target='https://yahoo.com', new_tab=True)
    ui.link(text='DuckDuckGo', target='https://duckduckgo.com', new_tab=True)

for i in range(5):
    ui.label("random text:")
    ui.label('hello')
    ui.html("<br><br><br><br><br><br><br><br><br>")

#image as link (leave the text field empty and stack it under link command
with ui.link(target='https://google.com', new_tab=True):
    ui.image('https://cdn-icons-png.flaticon.com/512/622/622669.png').classes('w-16')

# =======================
# ✅ 3. chat messages
# =======================

#for chat message
ui.chat_message(text='Hello NiceGUI',
                name='Robot',
                stamp='now',
                avatar='https://robohash.org/ui'
                )

#customize using html \n can be used for newline
ui.chat_message(text='this text is in <b>HTML</b>', text_html=True)
#multiple messages can be sent using list of strings
ui.chat_message(text=['Hi!','How are you?'])

#adding child elements using a with command
with ui.chat_message():
    ui.label('What is this?')
    ui.image('https://robohash.org/ui').classes('w-64')


ui.run()