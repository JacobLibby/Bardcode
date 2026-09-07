from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty, BooleanProperty
import recursion

class basicTemplate(BoxLayout):
    my_text = StringProperty("How many clicks?")
    count = 0
    validated_text = StringProperty("")
    # slider_value_txt = StringProperty("50")
    count_enabled = BooleanProperty(False)
    def on_toggle_button_state(self,widget):
        print(f"toggle state: {widget.state}")
        if widget.state == "down":
            widget.text = "ON"
            self.count_enabled = True
        else:
            widget.text = "OFF"
            self.count_enabled = False


    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)
            print("Clicked")
        pass

    def on_switch_active(self,widget):
        print(f"Switch: {widget.active}")

    # def on_slider_touch_up(self,widget):
    #     # print(widget.value)
    #     pass
    # def on_slider_value(self,widget):
    #     # self.slider_value_txt = str(int(widget.value))
    #     # print(f"Slider Value: {int(widget.value)}")
    #     pass

    def on_text_validate(self,widget):
        self.validated_text = widget.text
        gen = recursion.discovery()
        discoveryName, discoveryTable = gen.generateTable(self.validated_text)
        self.validated_text = gen.printDiscovery(discoveryName, discoveryTable)

        pass

class WidgetExample(GridLayout):
    my_text = StringProperty("How many clicks?")
    count = 0
    validated_text = StringProperty("")
    # slider_value_txt = StringProperty("50")
    count_enabled = BooleanProperty(False)
    def on_toggle_button_state(self,widget):
        print(f"toggle state: {widget.state}")
        if widget.state == "down":
            widget.text = "ON"
            self.count_enabled = True
        else:
            widget.text = "OFF"
            self.count_enabled = False


    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)
            print("Clicked")
        pass

    def on_switch_active(self,widget):
        print(f"Switch: {widget.active}")

    # def on_slider_touch_up(self,widget):
    #     # print(widget.value)
    #     pass
    # def on_slider_value(self,widget):
    #     # self.slider_value_txt = str(int(widget.value))
    #     # print(f"Slider Value: {int(widget.value)}")
    #     pass

    def on_text_validate(self,widget):
        self.validated_text = widget.text
        gen = recursion.discovery()
        discoveryName, discoveryTable = gen.generateTable(self.validated_text)
        self.validated_text = gen.printDiscovery(discoveryName, discoveryTable)

        pass
    
class PageLayoutExample(PageLayout):
    pass

class ScrollViewExample(ScrollView):

    pass

class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(0,100):
            #size = dp(100)
            #b = Button(text=str(i+1),size_hint=(None,None),size=(size,size))
            b = Button(text=str(i+1),size_hint=(1,None),size=(1,dp(40)))
            self.add_widget(b)

    pass


class GridLayoutInfoList(GridLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.cols=1
        for i in range(0,100):
            size = dp(100)
            b = Button(text=str(i+1),size_hint=(None,None),size=(size,size))
            self.add_widget(b)

    pass


# class GridLayoutExample(GridLayout):
#     pass

class AnchorLayoutExample(AnchorLayout):
    pass





class BoxLayoutExample(BoxLayout):
    my_text = StringProperty("How many clicks?")
    count = 0
    validated_text = StringProperty('B A R D C O D E')
    # slider_value_txt = StringProperty("50")
    count_enabled = BooleanProperty(False)
    def on_toggle_button_state(self,widget):
        print(f"toggle state: {widget.state}")
        if widget.state == "down":
            widget.text = "ON"
            self.count_enabled = True
        else:
            widget.text = "OFF"
            self.count_enabled = False


    def on_button_click(self):
        if self.count_enabled:
            self.count += 1
            self.my_text = str(self.count)
            print("Clicked")
        pass

    def on_switch_active(self,widget):
        print(f"Switch: {widget.active}")

    # def on_slider_touch_up(self,widget):
    #     # print(widget.value)
    #     pass
    # def on_slider_value(self,widget):
    #     # self.slider_value_txt = str(int(widget.value))
    #     # print(f"Slider Value: {int(widget.value)}")
    #     pass

    def on_text_validate(self,widget):
        self.validated_text = widget.text
        gen = recursion.discovery()
        discoveryName, discoveryTable = gen.generateTable(self.validated_text)
        fetchD = gen.fetchDiscovery(discoveryName, discoveryTable)
        if discoveryTable == 'Weapon':
            dI = recursion.DiscoveryWeapon(*fetchD)
            self.validated_text = (f'CONGRATS, you found a new weapon, a [color=0000ff]{dI.title}[/color]!\n\n{dI.description}')
        elif discoveryTable == 'Armor':
            dI = recursion.DiscoveryArmor(*fetchD)
            self.validated_text = (f'CONGRATS, you found some new armor, a [color=0000ff]{dI.title}[/color]!\n\n{dI.description}')
        elif discoveryTable == 'Consumable':
            dI = recursion.DiscoveryConsumable(*fetchD)
            self.validated_text = (f'CONGRATS, you found some consumables, a [color=0000ff]{dI.title}[/color]!\n\n{dI.description}')
        elif discoveryTable == 'Misc':
            dI = recursion.DiscoveryMisc(*fetchD)
            self.validated_text = (f'CONGRATS, you found a [color=0000ff]{dI.title}[/color]!\n\n{dI.description}')
        elif discoveryTable == 'Quest':
            dI = recursion.DiscoveryQuest(*fetchD)
            self.validated_text = (f'WOAH, you found the quest: [color=00ffff]{dI.title}[/color]!\n\n{dI.description}')
        elif discoveryTable == 'Encounter':
            dI = recursion.DiscoveryEncounter(*fetchD)
            self.validated_text = (f'You stumble upon [color=ff00ff]{dI.name}[/color]!\n\n{dI.description}, I should make the Encounter and referenced tables')
        else:
            self.validated_text = ('You found nothing...\n\ntry again?')

        # discoveryData = gen.fetchDiscovery(discoveryName, discoveryTable)
        # self.validated_text = discoveryData[]

        

        widget.text = ""
    """    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        b1 = Button(text="A")
        b2 = Button(text="B")
        b3 = Button(text="C")
        self.add_widget(b1)
        self.add_widget(b2)
        self.add_widget(b3)
"""
    pass


class MainWidget(Widget):
    pass

# need to have "App" suffix AND reference
class TheLabApp(App):
    pass

TheLabApp().run()

