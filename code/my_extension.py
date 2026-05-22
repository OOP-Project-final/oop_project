
import matplotlib.pyplot as plt #import to create figure and axes and to display them
import matplotlib.axis as maxis #imported to extened it



class MyCustomAxis(maxis.XAxis):  #inherits from a class of aaxis 
    """
      what it do:-
     It adds four new methods:
     set_custom_label() : set a custom colored label on the axis
     highlight_ticks()  : change the color of all tick marks
     reset_style()      : reset label and ticks back to default
     get_tick_count()   : return how many ticks are on the axis

    """

    def __init__(self, axes, *args, **kwargs):
        super().__init__(axes, *args, **kwargs) #to access feture of parent 
        self._custom_label_text  = ""       # stores our custom label
        self._highlight_color    = "black"  # stores current tick color
        self._original_color     = "black"  # stores original color for reset

  
    def set_custom_label(self, text, color="blue"): #for cutom lable color
        self._custom_label_text = text
        self.set_label_text(text)   #to set text of lable
        self.label.set_color(color) #to set color of lable
   
    def highlight_ticks(self, color="red"): #ths method will highlight the ticks in given color
        self._highlight_color = color    
        for tick in self.get_major_ticks():
            tick.tick1line.set_color(color)   # tick mark line color
            tick.tick2line.set_color(color)   # other side tick color
            tick.label1.set_color(color)      # tick label color

        for tick in self.get_minor_ticks():   # Change color of all minor tick marks too
            tick.tick1line.set_color(color)
            tick.tick2line.set_color(color)
            tick.label1.set_color(color)


    def reset_style(self):  #to reset to default colors
        self._custom_label_text = ""   # Reset label text to empty
        self.set_label_text("")
        self.label.set_color(self._original_color)   # Reset label color to original black

      
        for tick in self.get_major_ticks():    # Reset all tick colors back to original
            tick.tick1line.set_color(self._original_color)
            tick.tick2line.set_color(self._original_color)
            tick.label1.set_color(self._original_color)

      
        self._highlight_color = self._original_color      # Reset highlight color tracker

   


