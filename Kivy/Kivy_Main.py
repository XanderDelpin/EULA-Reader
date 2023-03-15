from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserListView
import subprocess
import os

class UploadFileApp(App):
    def build(self):
        # Create the main layout
        layout = BoxLayout(orientation='vertical')
        
        # Set the background color to a shade of blue
        layout.background_color = (0.2, 0.4, 0.6, 1)

        # Create the upload button
        upload_button = Button(text='Upload File', size_hint=(1, 0.2))
        layout.add_widget(upload_button)

        # Create the file chooser widget
        file_chooser = FileChooserListView()

        # Create the library box
        library_box = BoxLayout(orientation='vertical', size_hint=(1, 0.8))
        layout.add_widget(library_box)

        # Define the button press event
        def on_button_press(instance):
            # Add the file chooser to the layout
            layout.add_widget(file_chooser)

        # Define the file chooser selection event
        def on_selection(instance, value):
            selected_file = value and value[0]
            if selected_file:
                print('Selected file:', selected_file)
                # Remove the file chooser from the layout
                layout.remove_widget(file_chooser)
                # Open the selected file with the default viewer
                subprocess.Popen(['start', '', selected_file], shell=True)

        # Set the event handlers
        upload_button.bind(on_press=on_button_press)
        file_chooser.bind(selection=on_selection)

        # Get the list of files in the library directory
        library_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'EULA-Reader', 'EULA_Examples'))
        if os.path.isdir(library_path):
            library_files = os.listdir(library_path)
            for library_file in library_files:
                # Create a label for each file and add it to the library box
                file_label = Label(text=library_file)
                library_box.add_widget(file_label)

        return layout

if __name__ == '__main__':
    UploadFileApp().run()
