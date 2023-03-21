from kivy.lang import Builder
from kivy.config import Config
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.button import Button
from kivy.uix.filechooser import FileChooserListView
from kivy.core.window import Window
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.dialog import MDDialog
from kivy.uix.widget import Widget
import fitz
import subprocess
import os

class UploadFileApp(MDApp):

    def build(self):
        # Create the main 
        layout = MDBoxLayout(orientation='vertical', md_bg_color=[0, 0, 0, 1])
        Window.size = (414, 736) # Phone Screen Size


        # Create the file chooser widget
        file_chooser = FileChooserListView()
        # Create the library box
        library_box = MDBoxLayout(orientation='horizontal', size_hint=(1, 0.8), md_bg_color=[0.5, 0.5, 0.5, 1])
        layout.add_widget(library_box)
        
        prototype_label = MDLabel(text='Prototype', font_size=50, halign='center', valign='middle',
                              size_hint=(None, None), size=(400, 200),
                              pos_hint={'center_x': 0.5, 'center_y': 0.8},
                              color=(1, 1, 1, 0.5))
        layout.add_widget(prototype_label)
# Get the list of files in the library directory
        library_path = '//home//user//projects//EULA-Reader//EULA_Examples'
        if os.path.isdir(library_path):
            library_files = os.listdir(library_path)
            for library_file in library_files:
                # Create a label for each file and add it to the library box
                file_label = MDLabel(text=library_file, halign='center', md_bg_color=[0.5, 0.5, 0.5, 1])
                library_box.add_widget(file_label)
        # Create the upload button
        upload_button = Button(text='Upload File', size_hint=(0.5,0), pos_hint = {'center_x': 0.5, 'center_y': 0.5},
                       background_color=(1, 0, 0, 1))
        layout.add_widget(upload_button)
         # Define the button press event
        def on_button_press(instance):
            if  file_chooser.parent is None:
                layout.add_widget(file_chooser)
            else:
                layout.remove_widget(file_chooser)

        # Define the file chooser selection event
        def on_selection(instance, value):
            selected_file = value and value[0]
            if selected_file:
                print('Selected file:', selected_file)
                doc = fitz.open(selected_file)
                text = ""
                for page in doc:
                    text+=page.get_text()
                print(text)
                self.open_file(selected_file)

        # Set the event handlers
        upload_button.bind(on_press=on_button_press)
        file_chooser.bind(selection=on_selection)

        return layout

    def open_file(self, file_path):
        try:
            subprocess.Popen(['start', '', file_path], shell=True)
        except:
            self.dialog = MDDialog(title="Error", text="Could not open file.", size_hint=(0.7, 0.3), md_bg_color=[0.2, 0.2, 0.2, 0.9])
            self.dialog.open()


if __name__ == '__main__':
    UploadFileApp().run()
