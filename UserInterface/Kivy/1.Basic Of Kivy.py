'''
This Tutorial Guide You to Build Desktop Application using The Kivy and Python

Kivy Gaining Market because of
1.cross platform
2.Business Friendly
3.GPU Accelerated
4.Kivy is 100% free to use, under an MIT license 


Basic Installation Steps of kivy in Python

Ensure you have the latest pip and wheel:

python -m pip install --upgrade pip wheel setuptools

Install the dependencies (skip gstreamer (~120MB) if not needed, see Kivy’s dependencies):

python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
python -m pip install kivy.deps.gstreamer

Note
If you encounter a MemoryError while installing, add after pip install an option –no-cache-dir.
For Python 3.5+, you can also use the angle backend instead of glew. This can be installed with:

python -m pip install kivy.deps.angle


Install kivy:

python -m pip install kivy
(Optionally) Install the kivy examples:

python -m pip install kivy_examples


'''
from kivy.app import App
from kivy.app import App #Importing Kivy 
from kivy.uix.button import Button #Importing Button

#App name
class TestApp(App):
    def build(self):
        return Button(text='Hello World')

#calling Test App
TestApp().run()
