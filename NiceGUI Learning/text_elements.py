from nicegui import ui

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


# =======================
# ✅ 4. Generic Element
# =======================

#-------------📝📝📝📝Event Handlers---------------------------###
# Python Handler: To handle event on server side (mostly used where backend system comes to play)
# JS Handler: To handle it on client side (on browser itself)
# use emit : To send a part of the data to server
#---------------------------------------------------------------###

with ui.element('div').classes('p-2 bg-blue-100'):
    ui.label("inside div block with a coloured background")

#Handlers (in documentation -> will be there but in real, there is nothig in js like this,instead use =>
ui.button('Python Handlers').on('click',lambda e: ui.notify(f'click: ({e.args["clientX"]},{e.args["clientY"]})'))
ui.button('JS Handler').on('click',js_handler='(e) => alert(`click: (${e.clientX},${e.clientY})`)')
ui.button('Combined').on('click', lambda e: ui.notify(f'click:{e.args}'),
                         js_handler='(e) => emit(e.clientX,e.clientY)')

#trying card
with ui.card():
    ui.label('💡 Tip of the Day')
    ui.label('Use `ui.card` to group related UI elements with a clean design.')


# 🎯 Challenge 1. keep both cards side by side and add one button to move the text between cards
#tried many ways, both row as column and keeping both cards in one row and button in another works
with ui.column().classes('items-center space-y-4'): #to keep button in one row and both cards in one row
    #To keep labels in one row
    with ui.row().classes('gap-4'):
        card1 = ui.card().classes('w-64')
        card2 = ui.card().classes('w-64')

    with card1:
        label = ui.label("move between cards")

    in_card1 = {'status': True} #to keep track of the text in which card

    #function to move the label
    def move_label():
        if in_card1['status']:
            label.move(card2)
        else:
            label.move(card1)
        in_card1['status'] = not in_card1['status']

    ui.button('Move Label', on_click=move_label) #button which facilitates the move

# 🎯challenge 2: switch cards on clicking the button
# to keep button in one row and both cards in one row
with ui.column().classes('items-center space-y-4'):
    is_swapped = {'status': False} #to keep track of swapping

    #to keep cards in one row
    with ui.row().classes('gap-4') as card_container:
        with ui.card().classes('w-64') as cardA:
            ui.label('Card A')
        with ui.card().classes('w-64') as cardB:
            ui.label('Card B')

    #defined the swap card function
    def swap_cards():
        if is_swapped['status']:
            cardA.move(card_container, target_index=0)
            cardB.move(card_container, target_index=1)
        else:
            cardB.move(card_container, target_index=0)
            cardA.move(card_container, target_index=1)
        is_swapped['status'] = not is_swapped['status']

    ui.button("Swap Cards", on_click=swap_cards).classes('mx-auto mt-4') #button to facilitate swap



ui.run()
