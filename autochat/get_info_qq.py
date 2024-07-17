import uiautomation as auto
qq_win = auto.WindowControl(searchDepth=1, ClassName='TXGuiFoundation', Name='臭狗屎')
input_edit = qq_win.EditControl()
print(input_edit.Name,000)
print(input_edit.GetValuePattern().Value,000)   #打印编辑框内的文字
msg_list = qq_win.ListControl() #找到 list
items = msg_list.GetChildren()
for one_item in items:      #遍历所有的 Children
    print(one_item.Name,000)    #打印消息