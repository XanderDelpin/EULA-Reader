from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
import subprocess

class UploadFileApp(App):
    def build(self):
        # Create the upload file UI layout
        layout = BoxLayout(orientation='vertical')

        # Create the upload button
        upload_button = Button(text='Upload File', size_hint=(0.5, 0.2))
        layout.add_widget(upload_button)

        # Define the button press event
        def on_button_press(instance):
            # Create the file chooser widget
            file_chooser = FileChooserListView()

            # Create the popup with the file chooser widget
            popup = Popup(title='Select a file', content=file_chooser, size_hint=(0.8, 0.8))

            # Define the file chooser selection event
            def on_selection(instance):
                selected_file = file_chooser.selection and file_chooser.selection[1]
                if selected_file:
                    print('Selected file:', selected_file)
                    popup.dismiss()
                    # Display a message with the selected file name
                    message = 'Selected file: {}'.format(selected_file)
                    message_popup = Popup(title='File Selected', content=Label(text=message), size_hint=(0.5, 0.2))
                    message_popup.open()
                    # Open the selected file with the default viewer
                    subprocess.Popen(['open', selected_file])

            # Set the event handler for the file chooser
            file_chooser.bind(selection=on_selection)

            # Open the popup
            popup.open()

        # Set the event handler for the upload button
        upload_button.bind(on_press=on_button_press)

        return layout

if __name__ == '__main__':
    UploadFileApp().run()
