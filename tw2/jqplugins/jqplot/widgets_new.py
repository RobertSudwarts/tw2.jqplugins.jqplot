
from tw2.core.resources import encoder
import tw2.core as twc

import tw2.jquery
import tw2.jqplugins.ui.base as tw2_jq_ui

import base

_pager_defaults = {'enableSearch': True, 'enableClear': True, 'gridModel': True}


class MickeyMouse(tw2_jq_ui.JQueryUIWidget):
    resources = [
        tw2.jquery.jquery_js,
        tw2_jq_ui.jquery_ui_js, tw2_jq_ui.jquery_ui_css,
        base.jqplot_js, base.jqplot_css, base.jqplot_utils_js,
    ]
    template = "tw2.jqplugins.jqplot.templates.json_pollster"

    data = twc.Param("A list of list of tuples to plot.", default=[])
    options = twc.Param("Configuration options to pass to jqplot", default={})

    def prepare(self):
        self._data = encoder.encode(self.data)
        self._options = encoder.encode(self.options)
        super(MickeyMouse, self).prepare()


        
#class JsonPollingJQPlotWidget(tw2_jq_ui.JQueryUIWidget):
#    resources = [
#        tw2.jquery.jquery_js,
#        tw2_jq_ui.jquery_ui_js, tw2_jq_ui.jquery_ui_css,
#        base.jqplot_js, base.jqplot_css, base.jqplot_utils_js,
#        base.json2_js,
#    ]
    
#    template = "tw2.jqplugins.jqplot.templates.json_pollster"

#    jsonurl = twc.Param("(string) url to poll", default='')
#    options = twc.Param("Configuration options to pass to jqplot", default={})
    #url_kwargs = twc.Param("(dict) A dict for a query str", default={})
#    interval = twc.Param("(int) milliseconds between pulls", default=0)

#    def prepare(self):
#        self._jsonurl = encoder.encode(self.jsonurl)
#        self._options = encoder.encode(self.options)
#        #self.url_kwargs = encoder.encode(self.url_kwargs)
#        super(JsonPollingJQPlotWidget, self).prepare()
