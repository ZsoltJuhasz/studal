# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.1 on Sat Jan  1 12:12:53 2022
#

import wx
# begin wxGlade: dependencies
import wx.grid
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class MainForm(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: MainForm.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((900, 500))
        self.SetTitle("frame")

        # Tool Bar
        self.frame_toolbar = wx.ToolBar(self, -1)
        self.SetToolBar(self.frame_toolbar)
        self.frame_toolbar.Realize()
        # Tool Bar end

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_3, 3, wx.EXPAND, 0)

        self.studentTbl = wx.grid.Grid(self.panel_1, wx.ID_ANY, size=(1, 1))
        self.studentTbl.CreateGrid( 1, 4 )
        sizer_3.Add(self.studentTbl, 3, wx.EXPAND | wx.TOP, 10)

        sizer_4 = wx.BoxSizer(wx.VERTICAL)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)

        sizer_10 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_10, 1, wx.EXPAND | wx.TOP, 30)

        self.searchTf = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.searchTf.SetMinSize((150, 35))
        sizer_10.Add(self.searchTf, 0, wx.LEFT | wx.TOP, 10)

        self.searchBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Keresés")
        self.searchBtn.SetMinSize((110, 35))
        sizer_10.Add(self.searchBtn, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)

        sizer_9 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_9, 1, wx.EXPAND, 0)

        self.groupCb = wx.ComboBox(self.panel_1, wx.ID_ANY, choices=[], style=wx.CB_DROPDOWN)
        self.groupCb.SetMinSize((150, 35))
        sizer_9.Add(self.groupCb, 1, wx.LEFT | wx.TOP, 10)

        self.fillStudentsBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Diákok")
        self.fillStudentsBtn.SetMinSize((110, 35))
        sizer_9.Add(self.fillStudentsBtn, 0, wx.LEFT | wx.RIGHT | wx.TOP, 10)

        sizer_5 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_5, 1, wx.EXPAND, 0)

        self.manageStudentsBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Diákok kezelése")
        sizer_5.Add(self.manageStudentsBtn, 1, wx.ALIGN_BOTTOM | wx.LEFT | wx.RIGHT, 10)

        sizer_6 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_4.Add(sizer_6, 1, wx.EXPAND, 0)

        self.manageGroupBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Csoportok kezelése")
        self.manageGroupBtn.SetMinSize((110, 35))
        sizer_6.Add(self.manageGroupBtn, 1, wx.ALIGN_CENTER_VERTICAL | wx.LEFT | wx.RIGHT, 10)

        sizer_4.Add((20, 60), 0, wx.EXPAND, 0)

        self.exitBtn = wx.Button(self.panel_1, wx.ID_ANY, u"Kilépés")
        sizer_4.Add(self.exitBtn, 0, wx.ALIGN_RIGHT | wx.RIGHT, 10)

        self.statusLbl = wx.StaticText(self.panel_1, wx.ID_ANY, "Status label", style=wx.ALIGN_CENTER_HORIZONTAL)
        self.statusLbl.SetMinSize((150, 35))
        sizer_2.Add( self.statusLbl, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.TOP, 10 )

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        self.Centre()
        # end wxGlade

# end of class MainForm
