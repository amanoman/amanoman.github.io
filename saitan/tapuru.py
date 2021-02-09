menu_list = ("rice","pasta","chicken","sarad","fish")

print("レストランのメニュー表です。")
for menu in menu_list:
    print(menu.title())

menu_list = ("rice-ball","nudle","chicken","sarad","fish")

print("メニューに変更がありました。")
for menu in menu_list:
    print(menu.title())

