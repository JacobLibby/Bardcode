from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
from kivy.uix.pagelayout import PageLayout
from kivy.properties import StringProperty, BooleanProperty
import discoveryGen
import playerInventory
import logging
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image

from kivy.uix.label import Label
logger = logging.getLogger(__name__)

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
        gen = discoveryGen.discovery()
        discoveryName, discoveryTable = gen.generateTable(self.validated_text)
        self.validated_text = gen.printDiscovery(discoveryName, discoveryTable)
        #### NTS ^ change from printDiscovery to fetchDiscovery
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
        gen = discoveryGen.discovery()
        discoveryName, discoveryTable = gen.generateTable(self.validated_text)
        self.validated_text = gen.printDiscovery(discoveryName, discoveryTable)
        #### NTS ^ change from printDiscovery to fetchDiscovery

        pass
    
class PageLayoutExample(PageLayout):
    pass

class ScrollViewExample(ScrollView):
    pass


class InventoryItem(FloatLayout):
    pass



class IconButton(ButtonBehavior, Image):
    def on_press(self):
        print("IcontButton:on_press")

class StackLayoutExample(StackLayout):
    showing = "Inv"

    def labelPressed(self):
        print("Label has been pressed")
        print(f"label '' '' has been pressed")

    def update(self):
        list = []
        self.clear_widgets()
        
        if self.showing == "Inv":
            color_map = {
                        'weapon': 'ff0000'
                        ,'armor': 'ffa500'
                        ,'consumable': 'ffff00'
                        ,'misc': '00ff00'
                    }
            icon_map = {
                'weapon': 'W'
                ,'armor': 'A'
                ,'consumable': 'C'
                ,'misc': 'M'
            }
            list = playerInventory.PlayerInventory().fetchInventory()
            for each in list:
                print(each)
                # b.bind(on_ref_press=self.labelPressed)
                # f = FloatLayout(size_hint=(1,None),size=(1,dp(40)))
                b_icon = Button(text=str(f"{str(icon_map[each[2]])}"),pos_hint={"left":1},size_hint=(.15,None),size=(1,dp(40)),background_color=color_map[each[2]])
                b_name = Button(text=str(f"{str(each[1])}"),pos_hint={"x":.15},size_hint=(.7,None),size=(1,dp(40)),background_color=color_map[each[2]])
                b_count = Button(text=str(f"x{each[3]}"),pos_hint={"right":1},size_hint=(.15,None),size=(1,dp(40)),background_color=color_map[each[2]])

                # f.add_widget(b_icon)
                # f.add_widget(b_name)
                # # f.add_widget(b_count)

                # self.add_widget(f)
                self.add_widget(b_icon)
                self.add_widget(b_name)
                self.add_widget(b_count)
                # b = Button(text=str(f"{str(each[1])}    count: {each[3]}"),size_hint=(1,None),size=(1,dp(40)),background_color=color_map[each[2]])
                # self.add_widget(b)
                
        elif self.showing == "Quests":
            print("Show quests")
            list = ['Quest'] 
            for each in list:
                print(each)
                b = Button(text=str(each),size_hint=(1,None),size=(1,dp(40)),background_color="0000ff")
                self.add_widget(b)
            # should quests be in player inventory?
            pass
        elif self.showing == "Stats":
            print("Show stats")
            list = ['Stats','Stats','Stats']
            for each in list:
                print(each)
                b = Button(text=str(each),size_hint=(1,None),size=(1,dp(40)),background_color="ff00ff")
                self.add_widget(b)
        
        
        
        pass

    def clear_widgets(self, children=None):
        return super().clear_widgets(children)

    def __init__(self,**kwargs):
        print("INIT")
        super().__init__(**kwargs)
        self.orientation = "lr-tb"
        for i in range(0,10):
            #size = dp(100)
            #b = Button(text=str(i+1),size_hint=(None,None),size=(size,size))
            b = Button(text=str(i+1),size_hint=(1,None),size=(1,dp(40)))
            self.add_widget(b)
    def do_layout(self, *largs):
        
        super().do_layout(*largs)
        # print("DO LAYOUT")
        # print(f'\t*largs: {largs}')
        # self.showing = widget.value
        if type(largs[0]) != float:
            self.showing = largs[0].value
            # print(f"self.showing: {self.showing}")
            self.update()
            if self.showing == "Inv":
                print("INV")
                # b = Button(text="ADDING",size_hint=(1,None),size=(1,dp(40)))
                # self.add_widget(b)
            else:
                print(self.showing)
                # self.orientation = "lr-tb"
                # for i in range(0,100):
                #     #size = dp(100)
                #     #b = Button(text=str(i+1),size_hint=(None,None),size=(size,size))
                #     b = Button(text=str(i+1),size_hint=(1,None),size=(1,dp(40)))
                #     self.add_widget(b)

    


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


    def on_inv_button_click(self):
        print("on_inv_button_click(self)")
        inv = playerInventory.PlayerInventory()
        print(inv.fetchInventory())


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
        gen = discoveryGen.discovery()
        discoveryName, discoveryTable = gen.generateTable(self.validated_text)
        fetchD = gen.fetchDiscovery(discoveryName, discoveryTable)
        discoveredNothing = False
        if discoveryTable == 'weapon':
            dI = discoveryGen.DiscoveryWeapon(*fetchD)
            self.validated_text = (f'CONGRATS, you found a new weapon, a [color=ff0000]{dI.title}[/color]!\n\n{dI.description}')
        elif discoveryTable == 'armor':
            dI = discoveryGen.DiscoveryArmor(*fetchD)
            self.validated_text = (f'CONGRATS, you found some new armor, a [color=ffa500]{dI.title}[/color]!\n\n{dI.description}')
        elif discoveryTable == 'consumable':
            dI = discoveryGen.DiscoveryConsumable(*fetchD)
            self.validated_text = (f'CONGRATS, you found some consumables, a [color=ffff00]{dI.title}[/color]!\n\n{dI.description}')
        elif discoveryTable == 'misc':
            dI = discoveryGen.DiscoveryMisc(*fetchD)
            self.validated_text = (f'CONGRATS, you found a [color=00ff00]{dI.title}[/color]!\n\n{dI.description}')
        elif discoveryTable == 'quest':
            dI = discoveryGen.DiscoveryQuest(*fetchD)
            self.validated_text = (f'WOAH, you found the quest: [color=0000ff]{dI.title}[/color]!\n\n{dI.description}')
        elif discoveryTable == 'encounter':
            dI = discoveryGen.DiscoveryEncounter(*fetchD)
            self.validated_text = (f'You stumble upon [color=ff00ff]{dI.name}[/color]!\n\n{dI.description}, I should make the Encounter and referenced tables')
        else:
            discoveredNothing = True
            self.validated_text = ('You found nothing...\n\ntry again?')
        if discoveredNothing == False:
            pass
            # self.Inv.on_inv_button_click()
            # pI = playerInventory.PlayerInventory()
            # pI.addToInventory(dI.id, discoveryTable)


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
    activeMenu = "Inv"
    def on_inv_button_click(self):
        print("on_inv_button_click(self)")
        inv = playerInventory.PlayerInventory()
        # print(inv.fetchInventory())
        self.activeMenu = "Inv"
    pass

    def hide_widget(wid, dohide=True):
            if hasattr(wid, 'saved_attrs'):
                if not dohide:
                    wid.height, wid.size_hint_y, wid.opacity, wid.disabled = wid.saved_attrs
                    del wid.saved_attrs
            elif dohide:
                wid.saved_attrs = wid.height, wid.size_hint_y, wid.opacity, wid.disabled
                wid.height, wid.size_hint_y, wid.opacity, wid.disabled = 0, None, 0, True

if __name__ == '__main__':
    logging.basicConfig(filename='Bardcode.log', level=logging.INFO)
    logger.info('Started.')
    TheLabApp().run()
    logger.info('Finished.')

